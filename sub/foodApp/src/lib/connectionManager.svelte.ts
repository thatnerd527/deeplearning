import { untrack } from "svelte";

export function urlMaker(targetport: number, targetpath: string = "/"): string {
    // hostname:targetport/targetpath
    return `${window.location.hostname}:${targetport}${targetpath}`;
}

export type ConnectionManager = {
    detectionStats: {
        confidences: { [label: string]: number };
        currentImageID?: string;
    }
    socket: {
        socketConnection?: WebSocket;
        socketState?: 'connected' | 'disconnected' | 'error' | 'connecting';
        socketURL?: string;
        waitingForRetrySpeedLimit?: boolean; // true if the connection is waiting for retry speed limit
        retrySpeedLimit?: number; // in milliseconds, how long to wait before retrying connection
    }
    liveMode: {
        liveMode?: boolean;
        liveModeFPS?: number;
        liveModeStats: {
            framesSent: number;
            framesReceived: number;
            lastFrameLatencyMS: number;
        }
    }
    captureManagement: {
        currentImageCaptureBlob?: Blob;
        currentImageId?: string;
        captureNow?: boolean;
    }
}

export function createConnectionManager(): ConnectionManager {
    return {
        detectionStats: {
            confidences: {}
        },
        socket: {
            socketState: "disconnected",
            socketURL: `ws://${urlMaker(2000, "/ws/socketprocessing")}`
        },
        liveMode: {
            liveMode: true,
            liveModeFPS: 10,
            liveModeStats: {
                framesSent: 0,
                framesReceived: 0,
                lastFrameLatencyMS: 0
            }
        },
        captureManagement: {}
    };
}

export function createConnectionManagerTemplate(): ConnectionManager {
    return {
        detectionStats: {
            confidences: {}
        },
        socket: {
            socketState: "disconnected",
            socketURL: ``
        },
        liveMode: {
            liveMode: true,
            liveModeFPS: 10,
            liveModeStats: {
                framesSent: 0,
                framesReceived: 0,
                lastFrameLatencyMS: 0
            }
        },
        captureManagement: {}
    };
}

export function applyHooksToConnectionManager(cm: ConnectionManager, videoElement: HTMLVideoElement | null, canvasElement: HTMLCanvasElement | null) {
    if (!videoElement || !canvasElement) {
        console.warn("Video element or canvas element is null. Hooks not applied.");
        return;
    }
    liveModeAndSocketHooks(cm, canvasElement, videoElement);
    // capture button hook
    $effect(() => {
        if (cm.captureManagement.captureNow && cm.socket.socketState === "connected" && !cm.liveMode.liveMode) {
            cm.liveMode.liveMode = true // enable live mode, then turn off at the first received frame.
        }
    });
}

function liveModeAndSocketHooks(cm: ConnectionManager, canvasElement: HTMLCanvasElement, videoElement: HTMLVideoElement) {
    // canvas -> server hook
    $effect(() => {
        if (cm.liveMode.liveMode && cm.socket.socketState === "connected") {
            // apply live mode hooks
            let intervalId: NodeJS.Timeout;
            const ctx = canvasElement.getContext('2d');
            intervalId = setInterval(() => {
                // Draw current video frame to canvas
                ctx?.drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);

                // Convert canvas to Blob (JPEG) and send
                canvasElement.toBlob((blob) => {
                    if (blob && cm.socket.socketConnection?.readyState === WebSocket.OPEN) {
                        cm.socket.socketConnection.send(blob);
                    }
                }, 'image/png', 1); // 1 is quality (compression)

            }, 1000 / cm.liveMode.liveModeFPS!);
            return () => {
                clearInterval(intervalId);
            };
        }
    });
    // request camera 
    $effect(() => {
        if (cm.socket.socketState === "connected" && cm.liveMode.liveMode) {
            navigator.mediaDevices.getUserMedia({
                video: {
                    width: 480,
                    height: 480,
                    facingMode: "environment" // Use rear camera
                },
            }).then((stream) => {
                videoElement.srcObject = stream;
                videoElement.play();
            }).catch((error) => {
                console.error("Error accessing camera:", error);
                cm.liveMode.liveMode = false; // Disable live mode if camera access fails
            });
            return () => {
                if (videoElement.srcObject) {
                    const stream = videoElement.srcObject as MediaStream;
                    stream.getTracks().forEach(track => track.stop()); // Stop all tracks
                }
                videoElement.srcObject = null; // Clear the video source
            };
        }
    });
    // socket connectivity hook
    $effect(() => {
        if (cm.socket.socketState === "disconnected" && !cm.socket.waitingForRetrySpeedLimit) {
            cm.socket.socketConnection = new WebSocket(cm.socket.socketURL!);
            cm.socket.socketState = "connecting";
            cm.socket.socketConnection.onopen = () => {
                cm.socket.socketState = "connected";
                console.log("WebSocket connection established.");
            };
            cm.socket.socketConnection.onmessage = (event) => {
                // Handle incoming messages
                const data = JSON.parse(event.data);
                if (data.type === 'detection') {
                    cm.detectionStats.confidences = data.confidences;
                    cm.detectionStats.currentImageID = data.imageId;
                    if (cm.captureManagement.captureNow) {
                        cm.captureManagement.currentImageId = data.imageId;
                        cm.captureManagement.captureNow = false; // reset capture now
                        cm.liveMode.liveMode = false; // disable live mode after first capture
                    }
                    // Update live mode stats
                    cm.liveMode.liveModeStats.framesReceived += 1;
                    cm.liveMode.liveModeStats.lastFrameLatencyMS = data.latencyMS;
                }
            };
            cm.socket.socketConnection.onerror = (error) => {
                console.error("WebSocket error:", error);
                cm.socket.socketState = "error";
            };
            cm.socket.socketConnection.onclose = (e) => {
                console.log("WebSocket connection closed.");
                console.log(e)
                cm.socket.waitingForRetrySpeedLimit = true; // Set waiting state
                cm.socket.socketState = "disconnected";
                cm.socket.socketConnection = undefined;
                setTimeout(() => {
                    cm.socket.waitingForRetrySpeedLimit = false; // Reset waiting state
                    cm.socket.socketState = "disconnected"; // Reset state to allow reconnection
                }, cm.socket.retrySpeedLimit || 5000); // Default retry speed limit is 5000ms
            };
            return () => {
                if (cm.socket.socketConnection && cm.socket.socketState == "connected") {
                    console.log("Close requested")
                    cm.socket.socketConnection.close();
                }
            };
        }
    });
}

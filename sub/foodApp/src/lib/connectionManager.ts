export type ConnectionManager = {
    detectionStats: {
        confidences: { [label: string]: number };
        currentImageID?: string;
    }
    socket: {
        socketConnection?: WebSocket;
        socketState?: 'connected' | 'disconnected' | 'error';
        socketURL?: string;
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
    }
}

export function createConnectionManager(): ConnectionManager {
    return {
        detectionStats: {
            confidences: {}
        },
        socket: {},
        liveMode: {
            liveModeStats: {
                framesSent: 0,
                framesReceived: 0,
                lastFrameLatencyMS: 0
            }
        },
        captureManagement: {}
    };
}
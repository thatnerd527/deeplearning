<script lang="ts">
	import { applyHooksToConnectionManager, createConnectionManager, createConnectionManagerTemplate, type ConnectionManager } from "$lib/connectionManager.svelte";
	import { onMount } from "svelte";
	import "./mainpage.css";
	let connectionManager: ConnectionManager = $state(createConnectionManagerTemplate());
	let videoElement: HTMLVideoElement | null = null;
    let canvasElement: HTMLCanvasElement | null = null;
	onMount(() => {

		connectionManager = createConnectionManager();
		if (videoElement && canvasElement && connectionManager) {
			applyHooksToConnectionManager(connectionManager, videoElement, canvasElement);
		}
	});
</script>

<svelte:head></svelte:head>

<!-- frame: MainPage -->
<div class="frame main-page-397b128b1c7d">
	<!-- frame: ImageViewer -->
	<div class="shape frame image-viewe-397d93a11401">
		<video bind:this={videoElement} width="480" height="480" autoplay muted playsinline></video>

		<canvas bind:this={canvasElement} width="480" height="480" style="display: none;"></canvas>
	</div>
	<!-- frame: Socket Indicator -->
	<div class="frame socket-ind-3986abf1728a">
		<!-- frame: Connected -->
		{#if connectionManager.socket.socketState == 'connected'}
			<div class="frame connected-39875eb5be8b">
				<!-- group: check_24dp_E3E3E3_FILL1_wght400_GRAD0_opsz24 -->
				<div class="shape group check24dp-39875eb5be8e">
					<svg
						width="32"
						xmlns="http://www.w3.org/2000/svg"
						height="32"
						id="screenshot-6ec272e4-2a39-8029-8007-39875eb5be8e"
						viewBox="1358 566 32 32"
						style="-webkit-print-color-adjust::exact"
						xmlns:xlink="http://www.w3.org/1999/xlink"
						fill="none"
						version="1.1"
					>
						<g
							id="shape-6ec272e4-2a39-8029-8007-39875eb5be8e"
							style="opacity:1;fill:#000000"
							height="24"
							width="24"
							rx="0"
							ry="0"
						>
							<defs></defs>
							<g id="shape-6ec272e4-2a39-8029-8007-39875eb5be8f" style="display:none">
								<defs></defs>
								<g class="fills" id="fills-6ec272e4-2a39-8029-8007-39875eb5be8f">
									<rect
										rx="0"
										ry="0"
										x="1358"
										y="566"
										transform="matrix(1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000)"
										width="32"
										height="32"
										fill="none"
										style="fill:none"
									></rect>
								</g>
							</g>
							<g id="shape-6ec272e4-2a39-8029-8007-39875eb5be90">
								<defs></defs>
								<g class="fills" id="fills-6ec272e4-2a39-8029-8007-39875eb5be90">
									<path
										d="M1370.7332763671875,590L1363.13330078125,582.3999633789062L1365.0333251953125,580.5L1370.7332763671875,586.199951171875L1382.9666748046875,573.9666748046875L1384.86669921875,575.8666381835938L1370.7332763671875,590Z"
										style="fill:#1ea90c;fill-opacity:1"
									></path>
								</g>
							</g>
						</g>
					</svg>
				</div>
				<!-- text: Socket connected -->
				<div class="shape text socket-con-39875eb5be8d">
					<div
						class="text-node-html"
						id="html-text-node-6ec272e4-2a39-8029-8007-39875eb5be8d"
						data-x="1402"
						data-y="570"
					>
						<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
							<div class="paragraph-set root-0-paragraph-set-0">
								<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
									<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0"
										>Socket connected</span
									>
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		{/if}
		<!-- frame: Disconnected -->
		{#if connectionManager.socket.socketState == 'disconnected' || connectionManager.socket.socketState == undefined}
			<div class="frame disconnect-3986abf1728c">
				<!-- group: close_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24 -->
				<div class="shape group close24dp-3987716ddab8">
					<svg
						width="32"
						xmlns="http://www.w3.org/2000/svg"
						height="32"
						id="screenshot-6ec272e4-2a39-8029-8007-3987716ddab8"
						viewBox="1358 622 32 32"
						style="-webkit-print-color-adjust::exact"
						xmlns:xlink="http://www.w3.org/1999/xlink"
						fill="none"
						version="1.1"
					>
						<g
							id="shape-6ec272e4-2a39-8029-8007-3987716ddab8"
							style="fill:#000000"
							height="24"
							width="24"
							rx="0"
							ry="0"
						>
							<defs></defs>
							<g id="shape-6ec272e4-2a39-8029-8007-3987716e3683" style="display:none">
								<defs></defs>
								<g class="fills" id="fills-6ec272e4-2a39-8029-8007-3987716e3683">
									<rect
										rx="0"
										ry="0"
										x="1358"
										y="622"
										transform="matrix(1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000)"
										width="32"
										height="32"
										fill="none"
										style="fill:none"
									></rect>
								</g>
							</g>
							<g id="shape-6ec272e4-2a39-8029-8007-3987716e7b69">
								<defs></defs>
								<g class="fills" id="fills-6ec272e4-2a39-8029-8007-3987716e7b69">
									<path
										d="M1366.5333251953125,647.3333129882812L1364.6666259765625,645.4666748046875L1372.13330078125,638L1364.6666259765625,630.5333251953125L1366.5333251953125,628.6666870117188L1374,636.1333618164062L1381.4666748046875,628.6666870117188L1383.3333740234375,630.5333251953125L1375.86669921875,638L1383.3333740234375,645.4666748046875L1381.4666748046875,647.3333129882812L1374,639.8666381835938L1366.5333251953125,647.3333129882812Z"
										style="fill:#ec0909;fill-opacity:1"
									></path>
								</g>
							</g>
						</g>
					</svg>
				</div>
				<!-- text: Socket disconnected -->
				<div class="shape text socket-dis-3986abf17291">
					<div
						class="text-node-html"
						id="html-text-node-6ec272e4-2a39-8029-8007-3986abf17291"
						data-x="1402.0000000000005"
						data-y="626"
					>
						<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
							<div class="paragraph-set root-0-paragraph-set-0">
								<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
									<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0"
										>Socket disconnected</span
									>
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		{/if}
		<!-- frame: Error -->
		{#if connectionManager.socket.socketState == 'error'}
			<div class="frame error-3986abf1728c">
				<!-- group: error_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24 -->
				<div class="shape group error24dp-398dd043822c">
					<svg
						width="32"
						xmlns="http://www.w3.org/2000/svg"
						height="32"
						id="screenshot-6ec272e4-2a39-8029-8007-398dd043822c"
						viewBox="1358 678 32 32"
						style="-webkit-print-color-adjust::exact"
						xmlns:xlink="http://www.w3.org/1999/xlink"
						fill="none"
						version="1.1"
					>
						<g
							id="shape-6ec272e4-2a39-8029-8007-398dd043822c"
							style="fill:#000000"
							height="24"
							width="24"
							rx="0"
							ry="0"
						>
							<defs></defs>
							<g id="shape-6ec272e4-2a39-8029-8007-398dd0442bfa" style="display:none">
								<defs></defs>
								<g class="fills" id="fills-6ec272e4-2a39-8029-8007-398dd0442bfa">
									<rect
										rx="0"
										ry="0"
										x="1358"
										y="678"
										transform="matrix(1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000)"
										width="32"
										height="32"
										fill="none"
										style="fill:none"
									></rect>
								</g>
							</g>
							<g id="shape-6ec272e4-2a39-8029-8007-398dd044b639">
								<defs></defs>
								<g class="fills" id="fills-6ec272e4-2a39-8029-8007-398dd044b639">
									<path
										d="M1374,700.6666870117188C1374.3778076171875,700.6666870117188,1374.6944580078125,700.5388793945312,1374.949951171875,700.2833251953125C1375.20556640625,700.0277709960938,1375.3333740234375,699.7111206054688,1375.3333740234375,699.3333129882812C1375.3333740234375,698.95556640625,1375.20556640625,698.638916015625,1374.949951171875,698.3833618164062C1374.6944580078125,698.1278076171875,1374.3778076171875,698,1374,698C1373.6221923828125,698,1373.3055419921875,698.1278076171875,1373.050048828125,698.3833618164062C1372.79443359375,698.638916015625,1372.6666259765625,698.95556640625,1372.6666259765625,699.3333129882812C1372.6666259765625,699.7111206054688,1372.79443359375,700.0277709960938,1373.050048828125,700.2833251953125C1373.3055419921875,700.5388793945312,1373.6221923828125,700.6666870117188,1374,700.6666870117188ZM1372.6666259765625,695.3333129882812L1375.3333740234375,695.3333129882812L1375.3333740234375,687.3333129882812L1372.6666259765625,687.3333129882812L1372.6666259765625,695.3333129882812ZM1374,707.3333129882812C1372.155517578125,707.3333129882812,1370.4222412109375,706.9833374023438,1368.800048828125,706.2833251953125C1367.177734375,705.5833129882812,1365.7667236328125,704.6333618164062,1364.566650390625,703.433349609375C1363.36669921875,702.2333374023438,1362.4166259765625,700.8222045898438,1361.7166748046875,699.2000122070312C1361.0167236328125,697.5777587890625,1360.6666259765625,695.8444213867188,1360.6666259765625,694C1360.6666259765625,692.1555786132812,1361.0167236328125,690.4222412109375,1361.7166748046875,688.7999877929688C1362.4166259765625,687.1777954101562,1363.36669921875,685.7666625976562,1364.566650390625,684.566650390625C1365.7667236328125,683.3666381835938,1367.177734375,682.4166870117188,1368.800048828125,681.7166748046875C1370.4222412109375,681.0166625976562,1372.155517578125,680.6666870117188,1374,680.6666870117188C1375.844482421875,680.6666870117188,1377.5777587890625,681.0166625976562,1379.199951171875,681.7166748046875C1380.822265625,682.4166870117188,1382.2332763671875,683.3666381835938,1383.433349609375,684.566650390625C1384.63330078125,685.7666625976562,1385.5833740234375,687.1777954101562,1386.2833251953125,688.7999877929688C1386.9832763671875,690.4222412109375,1387.3333740234375,692.1555786132812,1387.3333740234375,694C1387.3333740234375,695.8444213867188,1386.9832763671875,697.5777587890625,1386.2833251953125,699.2000122070312C1385.5833740234375,700.8222045898438,1384.63330078125,702.2333374023438,1383.433349609375,703.433349609375C1382.2332763671875,704.6333618164062,1380.822265625,705.5833129882812,1379.199951171875,706.2833251953125C1377.5777587890625,706.9833374023438,1375.844482421875,707.3333129882812,1374,707.3333129882812ZM1374,704.6666870117188C1376.977783203125,704.6666870117188,1379.5,703.6333618164062,1381.566650390625,701.566650390625C1383.63330078125,699.5,1384.6666259765625,696.977783203125,1384.6666259765625,694C1384.6666259765625,691.022216796875,1383.63330078125,688.5,1381.566650390625,686.433349609375C1379.5,684.3666381835938,1376.977783203125,683.3333129882812,1374,683.3333129882812C1371.022216796875,683.3333129882812,1368.5,684.3666381835938,1366.433349609375,686.433349609375C1364.36669921875,688.5,1363.3333740234375,691.022216796875,1363.3333740234375,694C1363.3333740234375,696.977783203125,1364.36669921875,699.5,1366.433349609375,701.566650390625C1368.5,703.6333618164062,1371.022216796875,704.6666870117188,1374,704.6666870117188ZM1374,694Z"
										style="fill:#e1cd00;fill-opacity:1"
									></path>
								</g>
							</g>
						</g>
					</svg>
				</div>
				<!-- text: Socket error -->
				<div class="shape text socket-err-3986abf17291">
					<div
						class="text-node-html"
						id="html-text-node-6ec272e4-2a39-8029-8007-3986abf17291"
						data-x="1402"
						data-y="682"
					>
						<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
							<div class="paragraph-set root-0-paragraph-set-0">
								<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
									<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0"
										>Socket error</span
									>
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		{/if}
		{#if connectionManager.socket.socketState == 'connecting'}
			<!-- frame: Connecting -->
			<div class="frame connecting-3986abf1728c">
				<!-- group: pending_24dp_FFFF55_FILL0_wght400_GRAD0_opsz24 -->
				<div class="shape group pending24-3af9665096fa">
					<svg
						width="32"
						xmlns="http://www.w3.org/2000/svg"
						height="32"
						id="screenshot-722e4a11-8f35-8071-8007-3af9665096fa"
						viewBox="1358 734 32 32"
						style="-webkit-print-color-adjust::exact"
						xmlns:xlink="http://www.w3.org/1999/xlink"
						fill="none"
						version="1.1"
					>
						<g
							id="shape-722e4a11-8f35-8071-8007-3af9665096fa"
							style="fill:#000000"
							height="24"
							width="24"
							rx="0"
							ry="0"
						>
							<defs></defs>
							<g id="shape-722e4a11-8f35-8071-8007-3af966512dfb" style="display:none">
								<defs></defs>
								<g class="fills" id="fills-722e4a11-8f35-8071-8007-3af966512dfb">
									<rect
										rx="0"
										ry="0"
										x="1358"
										y="734"
										transform="matrix(1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000)"
										width="32"
										height="32"
										fill="none"
										style="fill:none"
									></rect>
								</g>
							</g>
							<g id="shape-722e4a11-8f35-8071-8007-3af96651aa70">
								<defs></defs>
								<g class="fills" id="fills-722e4a11-8f35-8071-8007-3af96651aa70">
									<path
										d="M1367.3333740234375,752C1367.8887939453125,752,1368.3612060546875,751.8056030273438,1368.75,751.4166870117188C1369.1387939453125,751.0277709960938,1369.3333740234375,750.5556030273438,1369.3333740234375,750C1369.3333740234375,749.4443969726562,1369.1387939453125,748.9722290039062,1368.75,748.5833129882812C1368.3612060546875,748.1943969726562,1367.8887939453125,748,1367.3333740234375,748C1366.77783203125,748,1366.3055419921875,748.1943969726562,1365.9166259765625,748.5833129882812C1365.52783203125,748.9722290039062,1365.3333740234375,749.4443969726562,1365.3333740234375,750C1365.3333740234375,750.5556030273438,1365.52783203125,751.0277709960938,1365.9166259765625,751.4166870117188C1366.3055419921875,751.8056030273438,1366.77783203125,752,1367.3333740234375,752ZM1374,752C1374.5555419921875,752,1375.02783203125,751.8056030273438,1375.4166259765625,751.4166870117188C1375.8055419921875,751.0277709960938,1376,750.5556030273438,1376,750C1376,749.4443969726562,1375.8055419921875,748.9722290039062,1375.4166259765625,748.5833129882812C1375.02783203125,748.1943969726562,1374.5555419921875,748,1374,748C1373.4444580078125,748,1372.97216796875,748.1943969726562,1372.5833740234375,748.5833129882812C1372.1944580078125,748.9722290039062,1372,749.4443969726562,1372,750C1372,750.5556030273438,1372.1944580078125,751.0277709960938,1372.5833740234375,751.4166870117188C1372.97216796875,751.8056030273438,1373.4444580078125,752,1374,752ZM1380.6666259765625,752C1381.22216796875,752,1381.6944580078125,751.8056030273438,1382.0833740234375,751.4166870117188C1382.47216796875,751.0277709960938,1382.6666259765625,750.5556030273438,1382.6666259765625,750C1382.6666259765625,749.4443969726562,1382.47216796875,748.9722290039062,1382.0833740234375,748.5833129882812C1381.6944580078125,748.1943969726562,1381.22216796875,748,1380.6666259765625,748C1380.1112060546875,748,1379.6387939453125,748.1943969726562,1379.25,748.5833129882812C1378.8612060546875,748.9722290039062,1378.6666259765625,749.4443969726562,1378.6666259765625,750C1378.6666259765625,750.5556030273438,1378.8612060546875,751.0277709960938,1379.25,751.4166870117188C1379.6387939453125,751.8056030273438,1380.1112060546875,752,1380.6666259765625,752ZM1374,763.3333129882812C1372.1556396484375,763.3333129882812,1370.4222412109375,762.9833374023438,1368.7999267578125,762.2833862304688C1367.177734375,761.5833129882812,1365.7666015625,760.63330078125,1364.5667724609375,759.433349609375C1363.36669921875,758.2333374023438,1362.4166259765625,756.8222045898438,1361.7166748046875,755.2000122070312C1361.0166015625,753.5778198242188,1360.6666259765625,751.844482421875,1360.6666259765625,750C1360.6666259765625,748.1555786132812,1361.0166015625,746.4221801757812,1361.7166748046875,744.7999877929688C1362.4166259765625,743.1777954101562,1363.36669921875,741.7666625976562,1364.5667724609375,740.566650390625C1365.7666015625,739.36669921875,1367.177734375,738.4166870117188,1368.7999267578125,737.7166137695312C1370.4222412109375,737.0166625976562,1372.1556396484375,736.6666870117188,1374,736.6666870117188C1375.8443603515625,736.6666870117188,1377.5777587890625,737.0166625976562,1379.2000732421875,737.7166137695312C1380.822265625,738.4166870117188,1382.2333984375,739.36669921875,1383.4332275390625,740.566650390625C1384.63330078125,741.7666625976562,1385.5833740234375,743.1777954101562,1386.2833251953125,744.7999877929688C1386.9833984375,746.4221801757812,1387.3333740234375,748.1555786132812,1387.3333740234375,750C1387.3333740234375,751.844482421875,1386.9833984375,753.5778198242188,1386.2833251953125,755.2000122070312C1385.5833740234375,756.8222045898438,1384.63330078125,758.2333374023438,1383.4332275390625,759.433349609375C1382.2333984375,760.63330078125,1380.822265625,761.5833129882812,1379.2000732421875,762.2833862304688C1377.5777587890625,762.9833374023438,1375.8443603515625,763.3333129882812,1374,763.3333129882812ZM1374,760.6666870117188C1376.9776611328125,760.6666870117188,1379.5,759.63330078125,1381.5667724609375,757.566650390625C1383.63330078125,755.5,1384.6666259765625,752.977783203125,1384.6666259765625,750C1384.6666259765625,747.022216796875,1383.63330078125,744.5,1381.5667724609375,742.433349609375C1379.5,740.36669921875,1376.9776611328125,739.3333129882812,1374,739.3333129882812C1371.0223388671875,739.3333129882812,1368.5,740.36669921875,1366.4332275390625,742.433349609375C1364.36669921875,744.5,1363.3333740234375,747.022216796875,1363.3333740234375,750C1363.3333740234375,752.977783203125,1364.36669921875,755.5,1366.4332275390625,757.566650390625C1368.5,759.63330078125,1371.0223388671875,760.6666870117188,1374,760.6666870117188ZM1374,750Z"
										style="fill:#ffff55"
									></path>
								</g>
							</g>
						</g>
					</svg>
				</div>
				<!-- text: Socket connecting -->
				<div class="shape text socket-con-3986abf17291">
					<div
						class="text-node-html"
						id="html-text-node-6ec272e4-2a39-8029-8007-3986abf17291"
						data-x="1402"
						data-y="738"
					>
						<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
							<div class="paragraph-set root-0-paragraph-set-0">
								<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
									<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0"
										>Socket connecting</span
									>
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		{/if}
	</div>
	<!-- frame: LiveMode -->
	<div class="frame live-mode-3980aa50a8b2">
		<!-- frame: Board -->
		<div class="frame board-398118cecadf">
			<!-- text: Detection stats -->
			<div class="shape text detection-398118cecae2">
				<div
					class="text-node-html"
					id="html-text-node-6ec272e4-2a39-8029-8007-398118cecae2"
					data-x="1358"
					data-y="566"
				>
					<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
						<div class="paragraph-set root-0-paragraph-set-0">
							<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
								<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0"
									>Detection stats</span
								>
							</p>
						</div>
					</div>
				</div>
			</div>
			<!-- text: Highest detection: ____________ -->
			<div class="shape text highest-de-398118cecae1">
				<div
					class="text-node-html"
					id="html-text-node-6ec272e4-2a39-8029-8007-398118cecae1"
					data-x="1358"
					data-y="602"
				>
					<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
						<div class="paragraph-set root-0-paragraph-set-0">
							<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
								<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0"
									>Highest detection: ____________</span
								>
							</p>
						</div>
					</div>
				</div>
			</div>
			<!-- frame: SwitchBoard -->
			<div class="shape frame switch-boar-398118cecae0"></div>
		</div>
		<!-- frame: Board -->
		<div class="frame board-3980aa50a8b5">
			<!-- text: Graph -->
			<div class="shape text graph-3981214a5e7e">
				<div
					class="text-node-html"
					id="html-text-node-6ec272e4-2a39-8029-8007-3981214a5e7e"
					data-x="1358"
					data-y="662.01"
				>
					<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
						<div class="paragraph-set root-0-paragraph-set-0">
							<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
								<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0">Graph</span>
							</p>
						</div>
					</div>
				</div>
			</div>
			<!-- frame: SwitchBoard -->
			<div class="shape frame switch-boar-3980aa50a8bd"></div>
		</div>
	</div>
	<!-- frame: LiveMode -->
	<div class="frame live-mode-3980a22a954b">
		<!-- frame: Board -->
		<div class="frame board-3980a22a954e">
			<!-- text: Live Mode -->
			<div class="shape text live-mode-3980a22a9557">
				<div
					class="text-node-html"
					id="html-text-node-6ec272e4-2a39-8029-8007-3980a22a9557"
					data-x="1358"
					data-y="746.0199999999998"
				>
					<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
						<div class="paragraph-set root-0-paragraph-set-0">
							<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
								<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0">Live Mode</span>
							</p>
						</div>
					</div>
				</div>
			</div>
			<!-- frame: SwitchBoard -->
			<div class="shape frame switch-boar-3980a22a9556"></div>
		</div>
		<!-- frame: Board -->
		<div class="frame board-3980a22a954d">
			<!-- text: Live mode FPS -->
			<div class="shape text live-mode-3980a22a9552">
				<div
					class="text-node-html"
					id="html-text-node-6ec272e4-2a39-8029-8007-3980a22a9552"
					data-x="1358"
					data-y="814.0199999999998"
				>
					<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
						<div class="paragraph-set root-0-paragraph-set-0">
							<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
								<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0"
									>Live mode FPS</span
								>
							</p>
						</div>
					</div>
				</div>
			</div>
			<!-- frame: TextBoard -->
			<div class="frame text-board-3980a22a9551">
				<!-- frame: Remove this -->
				<div class="frame remove-thi-3981a5c595c7">
					<!-- text: TextBox -->
					<div class="shape text text-box-3985839257db">
						<div
							class="text-node-html"
							id="html-text-node-6ec272e4-2a39-8029-8007-3985839257db"
							data-x="1492"
							data-y="814.0199999999998"
						>
							<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
								<div class="paragraph-set root-0-paragraph-set-0">
									<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
										<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0"
											>Live mode FPS</span
										>
									</p>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<!-- frame: Apply Button -->
			<div class="frame apply-butt-3980a22a9550">
				<!-- group: check_24dp_E3E3E3_FILL1_wght400_GRAD0_opsz24 -->
				<div class="shape group check24dp-39817a96df02">
					<svg
						width="32"
						xmlns="http://www.w3.org/2000/svg"
						height="32"
						id="screenshot-6ec272e4-2a39-8029-8007-39817a96df02"
						viewBox="1634 810.02 32 32"
						style="-webkit-print-color-adjust::exact"
						xmlns:xlink="http://www.w3.org/1999/xlink"
						fill="none"
						version="1.1"
					>
						<g
							id="shape-6ec272e4-2a39-8029-8007-39817a96df02"
							style="opacity:1;fill:#000000"
							height="24"
							width="24"
							rx="0"
							ry="0"
						>
							<defs></defs>
							<g id="shape-6ec272e4-2a39-8029-8007-39817a976781" style="display:none">
								<defs></defs>
								<g class="fills" id="fills-6ec272e4-2a39-8029-8007-39817a976781">
									<rect
										rx="0"
										ry="0"
										x="1634"
										y="810.0199999999998"
										transform="matrix(1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000)"
										width="32"
										height="32"
										fill="none"
										style="fill:none"
									></rect>
								</g>
							</g>
							<g id="shape-6ec272e4-2a39-8029-8007-39817a97b75b">
								<defs></defs>
								<g class="fills" id="fills-6ec272e4-2a39-8029-8007-39817a97b75b">
									<path
										d="M1646.7332763671875,834.02001953125L1639.13330078125,826.4199829101562L1641.0333251953125,824.52001953125L1646.7332763671875,830.219970703125L1658.9666748046875,817.9866943359375L1660.86669921875,819.8866577148438L1646.7332763671875,834.02001953125Z"
										style="fill:#ffffff;fill-opacity:1"
									></path>
								</g>
							</g>
						</g>
					</svg>
				</div>
			</div>
		</div>
		<!-- frame: Board -->
		<div class="frame board-3980a22a954c">
			<!-- text: Live mode stats -->
			<div class="shape text live-mode-3980a22a954f">
				<div
					class="text-node-html"
					id="html-text-node-6ec272e4-2a39-8029-8007-3980a22a954f"
					data-x="1358"
					data-y="882.0199999999998"
				>
					<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
						<div class="paragraph-set root-0-paragraph-set-0">
							<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
								<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0"
									>Live mode stats</span
								>
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<!-- frame: CaptureBox -->
	<div class="frame capture-box-397e1c64035c">
		<!-- frame: CaptureButton -->
		<div class="frame capture-but-397ef05f11fd">
			<!-- text: Capture -->
			<div class="shape text capture-397ef05f11ff">
				<div
					class="text-node-html"
					id="html-text-node-6ec272e4-2a39-8029-8007-397ef05f11ff"
					data-x="1482.5"
					data-y="982.0199999999998"
				>
					<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
						<div class="paragraph-set root-0-paragraph-set-0">
							<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
								<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0">Capture</span>
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

<style>
</style>

<script lang="ts">
	import './layout.css';
    import './additional.css';
    import Navbar from '../navbar/navbar.svelte';
    import { produce, castImmutable } from 'immer';
    import { setAppState } from '$lib/state.svelte'
	import { onMount } from 'svelte';

    onMount(async () => {
        await import('@material/web/ripple/ripple');
    });
    let { children } = $props();
    const appState = setAppState();
</script>

<!-- frame: Board -->
<!-- frame: dom -->
<div class="frame dom-36eb83d431d4">
	<!-- frame: Overlay -->
	<div
		class={`shape frame overlay-36ebed1d6c16 ${appState.data.navbarOpen ? 'overlayenabled' : 'overlaydisabled'}`}
	>
		<Navbar />
	</div>
	<!-- frame: Viewport -->
	<div
		class={`frame viewport-35344aef2900 ${appState.data.navbarOpen ? 'viewportdisabled' : 'viewportenabled'}`}
	>
		<!-- frame: AppBoard -->
		<div class="frame app-board-36e7c7e1c1d7">
			<!-- frame: Header -->
			<div class="frame header-3535b6b13164">
				<!-- frame: Board -->
				<div
					class="frame board-3535b0ded07e cursor-pointer"
					on:click={() => {
						appState.update(
							produce((state) => {
								state.navbarOpen = !state.navbarOpen;
							})
						);
					}}
				>
					<md-ripple></md-ripple>
					<!-- group: menu_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24 -->
					<div class="shape group menu24dp-3535b0ded07f">
						<svg
							width="24"
							xmlns="http://www.w3.org/2000/svg"
							height="24"
							id="screenshot-b366b59a-c959-800a-8007-3535b0ded07f"
							viewBox="540 210 24 24"
							style="-webkit-print-color-adjust::exact"
							xmlns:xlink="http://www.w3.org/1999/xlink"
							fill="none"
							version="1.1"
						>
							<g
								id="shape-b366b59a-c959-800a-8007-3535b0ded07f"
								style="fill:#000000"
								height="24"
								width="24"
								rx="0"
								ry="0"
							>
								<defs></defs>
								<g id="shape-b366b59a-c959-800a-8007-3535b0ded080" style="display:none">
									<defs></defs>
									<g class="fills" id="fills-b366b59a-c959-800a-8007-3535b0ded080">
										<rect
											rx="0"
											ry="0"
											x="540"
											y="210"
											transform="matrix(1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000)"
											width="24"
											height="24"
											fill="none"
											style="fill:none"
										></rect>
									</g>
								</g>
								<g id="shape-b366b59a-c959-800a-8007-3535b0ded081">
									<defs></defs>
									<g class="fills" id="fills-b366b59a-c959-800a-8007-3535b0ded081">
										<path
											d="M543,228L543,226.0000457763672L561,226.0000457763672L561,228L543,228ZM543,223.0000457763672L543,220.9999542236328L561,220.9999542236328L561,223.0000457763672L543,223.0000457763672ZM543,217.9999542236328L543,216L561,216L561,217.9999542236328L543,217.9999542236328Z"
											style="fill:#e3e3e3"
										></path>
									</g>
								</g>
							</g>
						</svg>
					</div>
				</div>
				<!-- frame: Board -->
				<div class="frame board-3534afa89afb">
					<!-- text: Banana Ripeness Detector -->
					<div class="shape text banana-rip-35361b4bdd13">
						<div
							class="text-node-html"
							id="html-text-node-b366b59a-c959-800a-8007-35361b4bdd13"
							data-x="594"
							data-y="210"
						>
							<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
								<div class="paragraph-set root-0-paragraph-set-0">
									<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
										<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0"
											>Banana Ripeness Detector</span
										>
									</p>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<!-- frame: Slot -->
			<div class="shape frame slot-36e7d2845c45">
				{@render children()}
			</div>
		</div>
	</div>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>

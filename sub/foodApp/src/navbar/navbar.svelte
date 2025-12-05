<script lang="ts">
    import "./style.css"
    import { onMount } from 'svelte';
    import { getAppState } from '$lib/state.svelte'
    const appState = getAppState();
</script>

<!-- frame: NavBar -->
<div
	class={`frame navbar-36fc76591ab8 ${appState.data.navbarOpen ? 'navbaropen' : 'navbarclosed'}`}
>
	<!-- frame: Board -->
	<div class="frame board-36f5cf42799e">
		<!-- frame: Board -->
		<div
			class="frame board-36fd7b9bd0cb cursor-pointer"
			on:click={() => {
				appState.update((draft) => {
					draft.navbarOpen = !draft.navbarOpen;
				});
			}}
		>
			<md-ripple></md-ripple>
			<!-- group: arrow_back_24dp_E3E3E3_FILL1_wght400_GRAD0_opsz24 -->
			<div class="shape group arrowback-36fdb1ebff17">
				<svg
					width="32"
					xmlns="http://www.w3.org/2000/svg"
					height="32"
					id="screenshot-653c8a4a-a386-8035-8007-36fdb1ebff17"
					viewBox="427 214 32 32"
					style="-webkit-print-color-adjust::exact"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					fill="none"
					version="1.1"
				>
					<g
						id="shape-653c8a4a-a386-8035-8007-36fdb1ebff17"
						style="fill:#000000"
						height="24"
						width="24"
						rx="0"
						ry="0"
					>
						<defs></defs>
						<g id="shape-653c8a4a-a386-8035-8007-36fdb1ecc8f7" style="display:none">
							<defs></defs>
							<g class="fills" id="fills-653c8a4a-a386-8035-8007-36fdb1ecc8f7">
								<rect
									rx="0"
									ry="0"
									x="427"
									y="214"
									transform="matrix(1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000)"
									width="32"
									height="32"
									fill="none"
									style="fill:none"
								></rect>
							</g>
						</g>
						<g id="shape-653c8a4a-a386-8035-8007-36fdb1ed3b89">
							<defs></defs>
							<g class="fills" id="fills-653c8a4a-a386-8035-8007-36fdb1ed3b89">
								<path
									d="M437.4333190917969,231.3333282470703L444.8999938964844,238.8000030517578L443,240.6666717529297L432.3333435058594,230L443,219.3333282470703L444.8999938964844,221.1999969482422L437.4333190917969,228.6666717529297L453.6666564941406,228.6666717529297L453.6666564941406,231.3333282470703L437.4333190917969,231.3333282470703Z"
									style="fill:#e3e3e3"
								></path>
							</g>
						</g>
					</g>
				</svg>
			</div>
		</div>
		<!-- frame: Board -->
		<div class="frame board-36f81eca3e75">
			<!-- group: home_24dp_E3E3E3_FILL1_wght400_GRAD0_opsz24 -->
			<div class="shape group home24dp-36f919f40c2f">
				<svg
					width="32"
					xmlns="http://www.w3.org/2000/svg"
					height="32"
					id="screenshot-653c8a4a-a386-8035-8007-36f919f40c2f"
					viewBox="425 216.5 32 32"
					style="-webkit-print-color-adjust::exact"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					fill="none"
					version="1.1"
				>
					<g
						id="shape-653c8a4a-a386-8035-8007-36f919f40c2f"
						style="fill:#000000"
						height="24"
						width="24"
						rx="0"
						ry="0"
					>
						<defs></defs>
						<g id="shape-653c8a4a-a386-8035-8007-36f919f4ac2e" style="display:none">
							<defs></defs>
							<g class="fills" id="fills-653c8a4a-a386-8035-8007-36f919f4ac2e">
								<rect
									rx="0"
									ry="0"
									x="425"
									y="216.5"
									transform="matrix(1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000)"
									width="32"
									height="32"
									fill="none"
									style="fill:none"
								></rect>
							</g>
						</g>
						<g id="shape-653c8a4a-a386-8035-8007-36f919f51901">
							<defs></defs>
							<g class="fills" id="fills-653c8a4a-a386-8035-8007-36f919f51901">
								<path
									d="M430.3333435058594,244.5L430.3333435058594,228.5L441,220.5L451.6666564941406,228.5L451.6666564941406,244.5L443.6666564941406,244.5L443.6666564941406,235.1666717529297L438.3333435058594,235.1666717529297L438.3333435058594,244.5L430.3333435058594,244.5Z"
									style="fill:#e3e3e3"
								></path>
							</g>
						</g>
					</g>
				</svg>
			</div>
			<!-- text: Main -->
			<div class="shape text main-36f88a234ccd">
				<div
					class="text-node-html"
					id="html-text-node-5b1fc4c2-fa6e-80fd-8007-36f88a234ccd"
					data-x="469"
					data-y="220.5"
				>
					<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
						<div class="paragraph-set root-0-paragraph-set-0">
							<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
								<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0">Main</span>
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- frame: Board -->
		<div class="frame board-36f8af9812b6">
			<!-- group: settings_24dp_E3E3E3_FILL1_wght400_GRAD0_opsz24 -->
			<div class="shape group settings2-36f920abf5f7">
				<svg
					width="32"
					xmlns="http://www.w3.org/2000/svg"
					height="32"
					id="screenshot-653c8a4a-a386-8035-8007-36f920abf5f7"
					viewBox="425 299.5 32 32"
					style="-webkit-print-color-adjust::exact"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					fill="none"
					version="1.1"
				>
					<g
						id="shape-653c8a4a-a386-8035-8007-36f920abf5f7"
						style="fill:#000000"
						height="24"
						width="24"
						rx="0"
						ry="0"
					>
						<defs></defs>
						<g id="shape-653c8a4a-a386-8035-8007-36f920ac0acb" style="display:none">
							<defs></defs>
							<g class="fills" id="fills-653c8a4a-a386-8035-8007-36f920ac0acb">
								<rect
									rx="0"
									ry="0"
									x="425"
									y="299.5"
									transform="matrix(1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000)"
									width="32"
									height="32"
									fill="none"
									style="fill:none"
								></rect>
							</g>
						</g>
						<g id="shape-653c8a4a-a386-8035-8007-36f920aca930">
							<defs></defs>
							<g class="fills" id="fills-653c8a4a-a386-8035-8007-36f920aca930">
								<path
									d="M437.3333435058594,328.8333435058594L436.79998779296875,324.5666809082031C436.5111083984375,324.45556640625,436.2388916015625,324.3222351074219,435.98333740234375,324.1666564941406C435.727783203125,324.0111083984375,435.477783203125,323.8444519042969,435.23333740234375,323.6666564941406L431.26666259765625,325.3333435058594L427.6000061035156,319L431.0333251953125,316.3999938964844C431.0111083984375,316.24444580078125,431,316.0944519042969,431,315.95001220703125L431,315.04998779296875C431,314.9055480957031,431.0111083984375,314.75555419921875,431.0333251953125,314.6000061035156L427.6000061035156,312L431.26666259765625,305.6666564941406L435.23333740234375,307.3333435058594C435.477783203125,307.1555480957031,435.73333740234375,306.9888916015625,436,306.8333435058594C436.26666259765625,306.6777648925781,436.5333251953125,306.54443359375,436.79998779296875,306.4333190917969L437.3333435058594,302.1666564941406L444.6666564941406,302.1666564941406L445.20001220703125,306.4333190917969C445.4888916015625,306.54443359375,445.7611083984375,306.6777648925781,446.01666259765625,306.8333435058594C446.272216796875,306.9888916015625,446.522216796875,307.1555480957031,446.76666259765625,307.3333435058594L450.73333740234375,305.6666564941406L454.3999938964844,312L450.9666748046875,314.6000061035156C450.9888916015625,314.75555419921875,451,314.9055480957031,451,315.04998779296875L451,315.95001220703125C451,316.0944519042969,450.977783203125,316.24444580078125,450.9333190917969,316.3999938964844L454.3666687011719,319L450.70001220703125,325.3333435058594L446.76666259765625,323.6666564941406C446.522216796875,323.8444519042969,446.26666259765625,324.0111083984375,446,324.1666564941406C445.73333740234375,324.3222351074219,445.4666748046875,324.45556640625,445.20001220703125,324.5666809082031L444.6666564941406,328.8333435058594L437.3333435058594,328.8333435058594ZM441.0666809082031,320.1666564941406C442.3555603027344,320.1666564941406,443.45556640625,319.71112060546875,444.3666687011719,318.79998779296875C445.27777099609375,317.8888854980469,445.73333740234375,316.78887939453125,445.73333740234375,315.5C445.73333740234375,314.21112060546875,445.27777099609375,313.1111145019531,444.3666687011719,312.20001220703125C443.45556640625,311.28887939453125,442.3555603027344,310.8333435058594,441.0666809082031,310.8333435058594C439.75555419921875,310.8333435058594,438.6499938964844,311.28887939453125,437.75,312.20001220703125C436.8500061035156,313.1111145019531,436.3999938964844,314.21112060546875,436.3999938964844,315.5C436.3999938964844,316.78887939453125,436.8500061035156,317.8888854980469,437.75,318.79998779296875C438.6499938964844,319.71112060546875,439.75555419921875,320.1666564941406,441.0666809082031,320.1666564941406Z"
									style="fill:#e3e3e3"
								></path>
							</g>
						</g>
					</g>
				</svg>
			</div>
			<!-- text: Settings -->
			<div class="shape text settings-36f92eee9f31">
				<div
					class="text-node-html"
					id="html-text-node-653c8a4a-a386-8035-8007-36f92eee9f31"
					data-x="471"
					data-y="303.5"
				>
					<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
						<div class="paragraph-set root-0-paragraph-set-0">
							<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
								<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0">Settings</span>
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- frame: Board -->
		<div class="frame board-36f74f2ee21f">
			<!-- group: code_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24 -->
			<div class="shape group code24dp-36f8c111a97e">
				<svg
					width="32"
					xmlns="http://www.w3.org/2000/svg"
					height="32"
					id="screenshot-653c8a4a-a386-8035-8007-36f8c111a97e"
					viewBox="425 382.5 32 32"
					style="-webkit-print-color-adjust::exact"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					fill="none"
					version="1.1"
				>
					<g
						id="shape-653c8a4a-a386-8035-8007-36f8c111a97e"
						style="fill:#000000"
						height="24"
						width="24"
						rx="0"
						ry="0"
					>
						<defs></defs>
						<g id="shape-653c8a4a-a386-8035-8007-36f8c112248e" style="display:none">
							<defs></defs>
							<g class="fills" id="fills-653c8a4a-a386-8035-8007-36f8c112248e">
								<rect
									rx="0"
									ry="0"
									x="425"
									y="382.5"
									transform="matrix(1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000)"
									width="32"
									height="32"
									fill="none"
									style="fill:none"
								></rect>
							</g>
						</g>
						<g id="shape-653c8a4a-a386-8035-8007-36f8c11253ae">
							<defs></defs>
							<g class="fills" id="fills-653c8a4a-a386-8035-8007-36f8c11253ae">
								<path
									d="M435.6666564941406,406.5L427.6666564941406,398.5L435.6666564941406,390.5L437.5666809082031,392.3999938964844L431.4333190917969,398.5333251953125L437.5333251953125,404.6333312988281L435.6666564941406,406.5ZM446.3333435058594,406.5L444.4333190917969,404.6000061035156L450.5666809082031,398.4666748046875L444.4666748046875,392.3666687011719L446.3333435058594,390.5L454.3333435058594,398.5L446.3333435058594,406.5Z"
									style="fill:#e3e3e3"
								></path>
							</g>
						</g>
					</g>
				</svg>
			</div>
			<!-- text: Developer -->
			<div class="shape text developer-36f8e1817555">
				<div
					class="text-node-html"
					id="html-text-node-653c8a4a-a386-8035-8007-36f8e1817555"
					data-x="471"
					data-y="386.5"
				>
					<div class="root rich-text root-0" xmlns="http://www.w3.org/1999/xhtml">
						<div class="paragraph-set root-0-paragraph-set-0">
							<p class="paragraph root-0-paragraph-set-0-paragraph-0" dir="ltr">
								<span class="text-node root-0-paragraph-set-0-paragraph-0-text-0">Developer</span>
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

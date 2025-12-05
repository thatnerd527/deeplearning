import adapter from '@jesterkit/exe-sveltekit';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),
	kit: {
		adapter: adapter({
			out: 'build',       // Output directory
			binaryName: 'my-app', // Name of your executable
			embedStatic: false   // Critical: embeds assets into the binary
		})
	}
};

export default config;
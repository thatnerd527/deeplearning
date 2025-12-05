import { produce } from 'immer';
import { getContext, setContext } from 'svelte';

export type AppGlobalData = {
    navbarOpen: boolean;
}


// Define a unique key for the context
const APP_STATE_KEY = Symbol('APP_STATE');

// This is the "State Factory"
export function createState() {
    // 1. Define state using Runes
    let data = $state({
        navbarOpen: false
    } as AppGlobalData)

    // 2. Return the state and updater functions
    return {
        // Use a getter so the value is read-only unless modified via methods
        get data() {
            return data;
        },

        update(fn: (draft: AppGlobalData) => void) {
            data = produce(data, fn);
        }
    };
}

// Helper functions to make usage cleaner in components
export function setAppState() {
    const appState = createState();
    setContext(APP_STATE_KEY, appState);
    return appState;
}

export function getAppState() {
    return getContext<ReturnType<typeof createState>>(APP_STATE_KEY);
}
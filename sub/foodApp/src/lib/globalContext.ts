import { createContext } from 'svelte';

export type AppGlobalData = {
    navbarOpen: boolean;
}

export type AppGlobalContext = {
    update: (fn: (draft: AppGlobalData) => void) => void;
    data: AppGlobalData;
}

export const [getAppContext, setAppContext] = createContext<AppGlobalContext>();
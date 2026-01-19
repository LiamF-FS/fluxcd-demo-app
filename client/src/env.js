// Allows for env vars set via .env file (local) or injected at run time (deployed)

export const env = {
    VITE_BASE_API_URL: window?.config?.VITE_BASE_API_URL ?? import.meta.env.VITE_BASE_API_URL ?? "",
};

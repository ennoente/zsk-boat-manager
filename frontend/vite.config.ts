import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    proxy: {
      "/api/checkins": {
        target: "http://backend:8000",
        changeOrigin: true,
        secure: false,
        ws: false,
      }
    }
  }
})

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base: '/spa-dev/',
  plugins: [react()],
    server: {
        host: true, // Needed for Docker container port mapping
        port: 5174, // You can use any port you prefer
        watch: {
            usePolling: true,
        },
    },
})


/*
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base: '/spa-dev/01JC30KVZYGPFVD4XBYDAMEJFC/01JCGCG8NK0BV2GCNV73VRBDSA/landing/',
  plugins: [react()],
    server: {
        host: true, // Needed for Docker container port mapping
        port: 5173, // You can use any port you prefer
        watch: {
            usePolling: true,
        },
    },

})
*/
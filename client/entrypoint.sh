#!/bin/sh
set -e

echo "Injecting runtime environment variables..."

# Produce Env.js at run time
envsubst '$VITE_BASE_API_URL' < /app/env.js.template > /app/env.js

exec nginx -g "daemon off;"

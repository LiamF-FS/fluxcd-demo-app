FROM node:24.8.0 AS build-stage
WORKDIR /client

ARG VITE_BASE_API_URL

ENV VITE_BASE_API_URL=$VITE_BASE_API_URL

COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

# Production Stage
FROM nginx AS production-stage
RUN mkdir /app
COPY --from=build-stage /client/dist/ /app

COPY env.js.template /app/env.js.template
COPY nginx.conf /etc/nginx/nginx.conf
COPY entrypoint.sh /entrypoint.sh

# Set permissions for user 1001
RUN chmod -R g=u /app && chmod -R a+w /app && \
    chmod +x /entrypoint.sh && \
    chmod g+rwx /var/cache/nginx /var/run /var/log/nginx

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]

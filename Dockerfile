FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
# Provide your own background.jpg alongside the Dockerfile
COPY background.jpg /usr/share/nginx/html/background.jpg

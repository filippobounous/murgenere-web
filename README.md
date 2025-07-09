# murgenere-web

A wrapper for murgenere.com and other apps.

This repository now includes a simple `index.html` that displays a fullscreen image and a dropdown menu for navigating to external services. Provide your own `background.jpg` next to the HTML file to customise the background. The menu can be customised by editing the `<select>` options in the HTML file.

To view locally, just open `index.html` in your browser.

## Docker

To run the page in a container:

```bash
docker build -t murgenere-web .
docker run -p 8080:80 murgenere-web
```

Then visit `http://localhost:8080`.

## Docker Compose

If you want to run the web page alongside other services, use the provided `docker-compose.yml`:

```bash
docker-compose up
```

This will start the web service and any additional services you define.

## Integrating with other Docker containers

Add your own services to `docker-compose.yml`. Each service joined to the
`murgenet` network can be reached by its service name from within the compose
setup. Update the dropdown links in `index.html` to point to these service
addresses.

Example snippet:

```yaml
services:
  web:
    build: .
    ports:
      - "8080:80"
    networks:
      - murgenet
  api:
    image: my-api-image
    networks:
      - murgenet
networks:
  murgenet:
```

Bring everything up with:

```bash
docker-compose up -d
```

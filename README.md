# PeerTube-Headless-Seeder

This container uses Python, Selenium, and Firefox to monitor and seed live streams of a PeerTube instance headlessly.

## :rotating_light: :rotating_light: THIS IS A WORK IN PROGRESS :rotating_light: :rotating_light:

### TO-DO:

1. Set proper pause timing for calling the API
2. Reduce the size of the docker image
3. Setup testing
4. Add metrics and logging

## Usage

### Docker Compose

```yaml
version: "3.3"

services:
  peertube-seeder:
    image: tyrsarm/peertube-headless-seeder:latest
    environment:
      peertube_url: "https://jupiter.tube/"
      ping_interval: 300
    restart: unless-stopped
```

### Docker CLI

```
docker run -d \
  --name peertube-headless-seeder
  -e peertube_url="https://jupiter.tube/" \
  -e ping_interval=300 \
  --restart=unless-stopped \
  tyrsarm/peertube-headless-seeder:latest
```

### Parameters

| Parameter     | Function                                               | Default                |
|---------------|--------------------------------------------------------|------------------------|
| peertube_url  | URL of the PeerTube instance that you want to seed     | `https://jupiter.tube` |
| ping_interval | The time between checking for live videos (in seconds) | `300`                  |

### Updating

#### Via Docker Compose

1. Update all images: `docker-compose pull`
2. Let compose update container as necessary: `docker-compose up -d`
3. You can also remove the old dangling images: `docker image prune`

#### Via Docker CLI

1. Update the image: `docker pull tyrsarm/peertube-headless-seeder:latest`
2. Stop the running container: `docker stop peertube-headless-seeder`
3. Delete the container: `docker rm peertube-headless-seeder`
4. Recreate a new container with the same docker run parameters as instructed above
5. You can also remove the old dangling images: `docker image prune`

## Source Code:

https://github.com/tyrsarm/peertube-headless-seeder

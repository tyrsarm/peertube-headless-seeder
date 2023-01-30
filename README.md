# Peertube-Headless-Seeder
This container uses Python, Selenium, and Firefox to monitor and seed live streams of a PeerTube channel headlessly. 
## THIS IS A WORK IN PROGRESS
### TO-DO:
1. Set proper pause timing for calling the API.
2. Make the scripts so they call the API once instead of three times
3. Replace the text file variables with envroment variables.
4. Do final tests.

## API Variable
The api_url environment variable is used to input the user's API URL. 
Example API URL:  https://example.tube/api/v1/accounts/channelname/videos

If the API URL is not set, the default is to follow and seed [Jupiter Broadcasting live streams on their instance](https://jupiter.tube/c/live/videos).

## How To Run
You can run the container two ways manually or thru Docker Compose.
Manually:
```
docker run --env api_url="https://example.tube/api/v1/accounts/channelname/videos" tyrsarm/peertube-headless-seeder
```

Docker Compose:
``` yaml
version: "3.3"

services:
  peertube-seeder:
    image: tyrsarm/peertube-headless-seeder:latest
    environment:
      api_url: "https://example.tube/api/v1/accounts/channelname/videos"
    restart: unless-stopped 
```

Source Code:
https://github.com/tyrsarm/peertube-headless-seeder

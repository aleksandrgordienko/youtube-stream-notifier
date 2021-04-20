# youtube-stream-notifier

**OS environment parameters:**

- STREAM_LINK - link to streamlink compatible stream, e.g. YouTube Live
- TELEGRAM_CHANNEL - Telegram ID for sending messages (bot must have right to send messages to this channel)
- TELEGRAM_TOKEN - Telegram Bot API token

**Using Docker image:**

`docker run --env STREAM_LINK="" --env TELEGRAM_CHANNEL="" --env TELEGRAM_TOKEN="" datadiving/youtube-stream-notifier`

**Links to repositories**

[GitHub repository](https://github.com/aleksandrgordienko/youtube-stream-notifier)

[DockerHub repository](https://hub.docker.com/r/datadiving/youtube-stream-notifier)
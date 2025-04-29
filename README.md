# Yet Another Youtube Downloader

A simple, cross-platform Python script to download YouTube videos or audio with customizable quality. Built on top of the powerful [yt-dlp](https://github.com/yt-dlp/yt-dlp) and saves files automatically to your system's default Downloads folder.


## Features

- Choose video quality (1080p, 480p, 144p)
- Option to download audio only (as MP3)
- Cross-platform: works on Windows, Linux, and macOS
- Automatically detects the user's Downloads folder


## Usage/Examples

```bash
git clone https://github.com/nukhes/yayd.git
cd yayd
pip install -r
python src/main.py [ARGS] [URL]
```

Download a test video
```
python src/main.py https://www.youtube.com/watch?v=xvFZjo5PgG0
```


## Requirements
- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- ffmpeg (for audio extraction)****

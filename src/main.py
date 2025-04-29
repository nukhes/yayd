import argparse
import yt_dlp

def video_quality(choice):
    if choice == '3':
        return {'format': 'bestvideo[height<=1080]+bestaudio/best'}
    elif choice == '2':
        return {'format': 'bestvideo[height<=480]+bestaudio/best'}
    elif choice == '1':
        return {'format': 'bestvideo[height<=144]+bestaudio/best'}
    else:
        print("Invalid choice, using default (best)")
        return {'format': 'best'}

parser = argparse.ArgumentParser(description='Download and fetch YT Media')
parser.add_argument('url', help='Media URL')
parser.add_argument('-a', '--audio-only', action='store_true', help='Download only video audio')
args = parser.parse_args()

ydl_opts = {}

if args.audio_only:
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
else:
    choice = input("Choose a quality:\n  [3] High (1080p)\n  [2] Medium (480p)\n  [1] Low (144p)\nEnter: ")
    ydl_opts = video_quality(choice)

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([args.url])

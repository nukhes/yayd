import os
import yt_dlp
from pathlib import Path

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_download_folder():
	"""Return user download dir"""
	if  os.name == "nt":
		return os.path.join(os.environ["USERPROFILE"], "Downloads")
	else:
		return os.path.join(Path.home(), "Downloads")

def download_task(opts, url):
	"""Start a download task"""
	clear_screen()
	print(f"Starting download (quality: {opts['format']})")
	with yt_dlp.YoutubeDL(opts) as task:
		task.download([url])
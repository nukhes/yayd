import os
import yt_dlp
import platform
from pathlib import Path

def get_download_folder():
	"""Return user download dir"""
	system = platform.system()
	if system == "Windows":
		return os.path.join(os.environ["USERPROFILE"], "Downloads")
	else:
		return os.path.join(Path.home(), "Downloads")

def download_task(opts, url):
	"""Start a download task"""
	with yt_dlp.YoutubeDL(opts) as task:
		task.download([url])
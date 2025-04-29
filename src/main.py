import os
import argparse
from utils import get_download_folder, download_task 

def video_quality(choice: str) -> dict:
	"""Return quality option"""
	options = {
		'3': {'format': 'bestvideo[height<=1080]+bestaudio/best'},
		'2': {'format': 'bestvideo[height<=480]+bestaudio/best'},
		'1': {'format': 'bestvideo[height<=144]+bestaudio/best'},
	}
	return options.get(choice, {'format': 'best'}) 

def main():
	parser = argparse.ArgumentParser(description='Download YouTube media with yt-dlp.')
	parser.add_argument('url', help='Media URL to download')
	parser.add_argument('-a', '--audio-only', action='store_true', help='Download audio only (MP3)')
	args = parser.parse_args()

	output_template = os.path.join(get_download_folder(), '%(title)s.%(ext)s')

	if args.audio_only:
		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
			}],
		}
	else:
		choice = input("Choose a video quality:\n  [3] High (1080p)\n  [2] Medium (480p)\n  [1] Low (144p)\nEnter: ")
		ydl_opts = video_quality(choice)

	ydl_opts['outtmpl'] = output_template 

	download_task(ydl_opts, args.url)

if __name__ == '__main__':
	main()

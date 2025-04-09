# This script downloads a YouTube video and converts it to an MP3 file using yt-dlp.
import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
url = input("Enter the YouTube video URL: ")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

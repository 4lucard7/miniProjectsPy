import yt_dlp

url = input("Enter your YouTube link: ").split("&")[0]
choice = input("Audio or Video: ").lower()

ydl_opts = {}

if choice == "audio":
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
elif choice == "video":
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
    }
else:
    print("Invalid choice")
    exit()

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print("Downloading...")
    ydl.download([url])
    print("Download completed!")

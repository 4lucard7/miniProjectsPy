from pytube import YouTube



try:
    url = input("Enter your YouTube link: ").strip().split("&")[0]
    choice = input("Audio or Video: ").lower().strip()

    yt = YouTube(url, use_oauth=False, allow_oauth_cache=False)

    print(f"\nTitle: {yt.title}")

    if choice == "audio":
        stream = yt.streams.get_audio_only()
        print("\nDownloading audio...")
        stream.download(filename=f"{yt.title}.mp3")
        print("Audio Download Completed ✓")

    elif choice == "video":
        stream = yt.streams.get_highest_resolution()
        print("\nDownloading video...")
        stream.download()
        print("Video Download Completed ✓")

    else:
        print("ERROR: Invalid choice")

except Exception as e:
    print(f"An error occurred: {e}")


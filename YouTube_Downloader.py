import os
from pytube import YouTube

def download_video_or_audio():
    try:
        # Get the YouTube URL from the user (can be either a video or playlist URL)
        video_url = input("Enter the YouTube video or playlist URL: ")

        # Create a YouTube object
        yt = YouTube(video_url)

        if 'playlist' in video_url.lower():
            # If it's a playlist, download all videos in the playlist
            print(f"Downloading playlist: {yt.title}")

            for video in yt.playlist_videos():
                download_single_video(video)
            
            print("Playlist download complete!")
        else:
            # If it's a single video, ask the user for their preferences
            download_single_video(yt)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def download_single_video(video):
    # Display available streams and resolutions
    print("Available Resolutions:")
    for stream in video.streams.filter(file_extension="mp4").order_by('resolution'):
        print(f"{stream.resolution} - {stream.mime_type}")

    # Get the user's preferred resolution
    preferred_resolution = input("Enter your preferred resolution (enter 'audio' for audio-only): ")

    if preferred_resolution.lower() == 'audio':
        # Download only the audio
        audio_stream = video.streams.filter(only_audio=True).first()

        if audio_stream:
            # Download the audio
            print(f"Downloading audio: {video.title}")
            audio_stream.download()
            print(f"Download complete! Audio file saved in: {os.getcwd()}")
        else:
            print("No audio stream found.")
    else:
        # Get the selected video stream
        video_stream = video.streams.filter(file_extension="mp4", resolution=preferred_resolution).first()

        if video_stream:
            # Download the video
            print(f"Downloading video: {video.title}")
            video_stream.download()
            print(f"Download complete! Video file saved in: {os.getcwd()}")
        else:
            print(f"No stream found for the specified resolution: {preferred_resolution}")

# Call the function to download the video, audio, or playlist
download_video_or_audio()

# from pytube import Playlist, YouTube
# import os

# # Function to download a YouTube video in the highest quality
# def download_video(url, output_folder):
#     try:
#         yt = YouTube(url)
#         stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
#         print(f"Downloading {yt.title} in {stream.resolution}")
#         stream.download(output_folder)
#         print(f"Downloaded {yt.title} successfully!\n")
#     except Exception as e:
#         print(f"Error downloading {url}: {e}")

# # Function to download the entire playlist
# def download_playlist(playlist_url, output_folder):
#     try:
#         playlist = Playlist(playlist_url)
#         print(f"Downloading playlist: {playlist.title}")
        
#         # Check if the output folder exists, if not, create it
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)
        
#         for video_url in playlist.video_urls:
#             download_video(video_url, output_folder)

#         print("All videos downloaded!")
#     except Exception as e:
#         print(f"Error downloading playlist: {e}")

# # Main function
# if __name__ == "__main__":
#     playlist_url = input("Enter the YouTube playlist URL: ")
#     output_folder = input("Enter the output folder path (default is current folder): ")
    
#     if output_folder == "":
#         output_folder = os.getcwd()
    
#     download_playlist(playlist_url, output_folder)


# using  new library

import yt_dlp
import os

def download_playlist(playlist_url, output_folder):
    try:
        ydl_opts = {
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Output folder and filename template
            'format': 'bestvideo+bestaudio/best',            # Download best quality
            'merge_output_format': 'mp4',                    # Merge video and audio into mp4 format
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print("Playlist downloaded successfully!")
    
    except Exception as e:
        print(f"Error downloading playlist: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    output_folder = input("Enter the output folder path (default is current folder): ")
    
    if output_folder == "":
        output_folder = os.getcwd()
    
    download_playlist(playlist_url, output_folder)

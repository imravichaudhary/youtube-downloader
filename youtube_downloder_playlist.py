import os
import re
from pytube import Playlist

x=input("Enter the URL of the playlist to be downloaded: ")
print("")
print(f"Downloading.......... {x}")

# x='https://www.youtube.com/watch?v=ijKcxo4aRV0&ab_channel=MusicStorm'

yt=Playlist(x)
print("")

print(f'Playlist..... {yt.title}')
print("")

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, re.sub(r'[\\/*?:"<>|]', "-", yt.title) )
if not os.path.exists(final_directory):
   os.makedirs(final_directory)

#for stream in yt.streams:
#    print(stream)

# Download video
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

# Download audio
# yt.streams.filter(only_audio=True).first().download()

for index, y in enumerate(yt.videos):
    # Download audio
    print(f'downloading..{index+1}... {y.title}')
    y.streams.filter(only_audio=True).first().download(final_directory)

print("")
print("Download Successful !!")

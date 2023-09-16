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

# list to store files name
filenames = next(walk(final_directory), (None, None, []))[2]  # [] if no file
# remove extension
filenames=[sub[: -4] for sub in filenames]

for index, y in enumerate(yt.videos):
    # Download audio

    if (y.title in filenames):
        print("directory already contain " + y.title + ". Skip downloading....")
    else:
        print(f'downloading..{index+1}... {y.title}')
        try:
            y.streams.filter(only_audio=True).first().download(final_directory)
        except Exception as ex:
            print(f'exception occured while downloading song: {y.title}. ', ex)

print("")
print("Download Successful !!")

from moviepy.editor import *
from pathlib import Path


FOLDER=input("Enter the folder path to convert mp4 to mp3: ")
print("")
print(f"Converting..........{FOLDER}")

def MP4TOMP3(mp4, mp3):
    try:
        FILETOCONVERT = AudioFileClip(str(mp4))
        FILETOCONVERT.write_audiofile(str(mp3))
        FILETOCONVERT.close()
        # mp4.unlink() # delete mp4 files
    except Exception as ex:
        print(f"Exception while converting {mp4} to {mp3}", ex)

print(f'Converting audio Mp4 to Mp4 in folder: {FOLDER}')

for VIDEO_FILE_PATH in Path(FOLDER).rglob('*.mp4'):
    AUDIO_FILE_PATH = Path(f'{VIDEO_FILE_PATH.parent}/{VIDEO_FILE_PATH.name[:-1]}3')
    MP4TOMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)

print("Converted Successfully!")

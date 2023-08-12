from pytube import YouTube 
x=input("Enter the URL of the video to be downloaded: ")
print("")
print(f"Downloading.......... {x}")

yt=YouTube(x)
print("")

print(yt.title)

#for stream in yt.streams:
#    print(stream)

# Download video
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

# Download audio
yt.streams.filter(only_audio=True).first().download()

print("")
print("Download Successful !!")

# Youtube downloader

Simple python script to download youtube audio, video and playlist.

# Steps

- Clone the git repo in your local
    ```
    git clone https://github.com/imravichaudhary/youtube-downloader.git
    ```

- Change directory
    ```
    cd youtube-downloader
    ```

- Install required python package
 
  Pytube requires an installation of Python 3.6 or greater, as well as pip. (Pip is typically bundled with Python installations.)

  To install from PyPI with pip:
    ```
    python -m pip install pytube
    ```

    Sometimes, the PyPI release becomes slightly outdated. To install from the source with pip:
    ```
    python -m pip install git+https://github.com/pytube/pytube
    ```

- Download single audio songs
    ```
    python ./youtube_downloder.py
    ```

    Script will ask to provide the youtube link. For .eg., https://youtube.com/watch?v=2lAe1

    - Download playlist audio songs
    ```
    python ./youtube_downloder_playlist.py
    ```
    Script will ask to provide the youtube playlist link. For e.g., https://www.youtube.com/playlist?list=PLS1QulWo1RMeUT4LFwJ-ghgoSH6n

- You can modify the script to download video. Code is commented in both files.

- To convert mp4 audio files to mp3 audio files

    - ```
      python -m pip install moviepy
      ```
    - ```
      python ./convert-audio-mp4-to-mp3.py
      ```
      Script will ask for the folder name where mp4 files are placed.

- If you are facing issue similar to 
`pytube.exceptions.RegexMatchError: __init__: could not find match for ^\\w+\\W` then find the pytube package in your system. 

    For me it was installed in `C:\Users\<username>\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages\pytube`

    Modify cipher.py file

    Find line with content `\\w+\\W` and replace with `var_regex = re.compile(r"^\$*\w+\W")`

I hope this helps!!!

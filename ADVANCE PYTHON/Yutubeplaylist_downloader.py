from pytube import Playlist
#Link="https://www.youtube.com/results?search_query=playlist+of+good+songs"
pl=Playlist("https://www.youtube.com/results?search_query=playlist+of+good+songs")
# print(f'Downlading...{pl.title}')
for video in pl.videos:
    video.streams.first().download()
print("Download")
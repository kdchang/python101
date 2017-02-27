from pytube import YouTube
yt = YouTube()

yt.url = 'https://www.youtube.com/watch?v=hNQohQBFnwI'
video = yt.get('mp4', '360p')
print(yt.get_videos())
print(yt.filename)

video.download('./')
print('Yo')
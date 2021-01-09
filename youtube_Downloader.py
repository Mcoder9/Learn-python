import pytube

url = 'https://www.youtube.com/watch?v=sJeQiOxOpKE'

youtube = pytube.YouTube(url)
video = youtube.streams.first()
# video.download()

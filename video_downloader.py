from pytube import YouTube 

DOWNLOAD_FOLDER = 'C:\\repos\\golf_2project\\video_bank1'

url = "https://www.youtube.com/shorts/vmUXMAM5JLg"

yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)


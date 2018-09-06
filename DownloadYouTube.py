# coding:utf-8
"""
@Autor : Deiner Zapata Silva
@Link  : https://codigoscomentado.blogspot.com/2018/06/descargar-videos-y-audios-de-youtube.html
pip install youtube-dl
pip install pafy
pip install pydub
ejecutable ffmpeg -> https://ffmpeg.zeranoe.com/builds/

pip install python-vlc

pip install lxml
pip install libxml2-python3

"""
import pafy
import os
import time
from pydub import AudioSegment

def showDescriptionVideo(videoShow):
    print("-----------------------------------------------------------------------------")
    print("Title\t\t:" + videoShow.title)
    print("Author\t\t:"+videoShow.author)
    print("Categoria\t:"+videoShow.category)
    print("Duracion\t:"+videoShow.duration)
    print("Nick\t\t:"+videoShow.username)
    print("ID\t\t:"+videoShow.videoid)

def downloadVideo(video2down,extension="mp4"):
    print("-----------------------------------------------------------------------------")
    print("Download video . . . [mp4]")
    best = video2down.getbest(preftype=extension)
    best.download()

def downloadAudio(audio2down):
    print("-----------------------------------------------------------------------------")
    print("Download audio . . . [mp3]")
    best = audio2down.getbestaudio()
    best.download()
    
    AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
    sound = AudioSegment.from_file("C:/Users/LENOVO/Documents/PythonCode/YouTubeDownloader/audio.webm" ) #dir+"/YouTubeDownloader\\audio.webm")
    sound.export("./audio.mp3",format="mp3",bitrate="128k")

def loadLinks2download(listLinks):
    #Leer un archivo con los links txt de los videos o audios a descargar
    print("-----------------------------------------------------------------------------")
    print(str(listLinks))
    
dir = os.getcwd() #path.abspath(__file__)
print("-----------------------------------------------------------------------------")
print("DownloadYouTube.py... ["+str(dir)+"]")
link = "https://www.youtube.com/watch?v=5Y53boWWi8g"
videoObj = pafy.new(link)
showDescriptionVideo(videoObj)
downloadVideo(videoObj)
downloadAudio(videoObj)
print("-----------------------------------------------------------------------------")


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

def downloadVideo(video2down):
    print("-----------------------------------------------------------------------------")
    print("Download video . . . [mp4]")
    best = video2down.getbest(preftype="mp4")
    best.download()

def downloadAudio(audio2down):
    print("-----------------------------------------------------------------------------")
    print("Download audio . . . [mp3]")
    best = audio2down.getbestaudio()
    best.download()
    
    AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
    nameAudioFile_webm = audio2down.title + ".webm"
    nameAudioFile_mp3 = audio2down.title + ".mp3"
    sound = AudioSegment.from_file(nameAudioFile_webm) #dir+"/YouTubeDownloader\\audio.webm")
    sound.export(nameAudioFile_mp3,format="mp3",bitrate="128k")
    os.remove(nameAudioFile_webm)

def loadLinks2download():
    #Leer un archivo con los links txt de los videos o audios a descargar
    listLinks = open("links2download.txt","r")
    links=[]
    for linea in listLinks.readlines():
        linea = linea[:-1]
        if(linea=="audio" or linea=="video"):
            formato = linea
        else:
            links.append(linea)
    return formato,links

def downloadListLinks(formato,listLinks):
    for link in listLinks:
        videoObj = pafy.new(link)
        showDescriptionVideo(videoObj)
        
        if(formato == "video"):
            downloadVideo(videoObj)
        if(formato == "audio"):
            downloadAudio(videoObj)
            
dir = os.getcwd() #path.abspath(__file__)
print("-----------------------------------------------------------------------------")
print("DownloadYouTube.py... ["+str(dir)+"]")
formato, listLinks = loadLinks2download()
downloadListLinks(formato,listLinks)
print("-----------------------------------------------------------------------------")


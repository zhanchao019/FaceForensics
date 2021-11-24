from __future__ import unicode_literals
import os
import sys
import json
from pytube import YouTube
from tqdm import tqdm
import youtube_dl

conversion_dict_file = r"./conversion_dict.json"
video_path = "./original_video"  # youtube上下载的原视频
video_info_root = "./downloaded_videos_info"
if os.path.exists(conversion_dict_file):
    f = open(conversion_dict_file, 'r')
    conversionmap = json.load(f)
    failid=""
    for id, tubeid in tqdm(conversionmap.items()):
        tubeid = tubeid[:-2]
        audioSavePath = './original_audio/' + id

        # print(tubeid)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
                
            }],
            'outtmpl': audioSavePath + ".%(ext)s",
        }
        url = "https://www.youtube.com/watch?v="+str(tubeid)
        try:
            """YouTube(url).streams.first().download(
                video_path+"/"+id)  # highest quality vide"""
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        except Exception:
            print("id: " + id+" youtubeid: " + str(tubeid)+"failed")
            failid+=id
            failid+=" "
        """        
        try:
            yt=YouTube(url)
            yt=yt.get('mp4','1080p')
            yt.download(video_path+"/"+id)
        except Exception:
            print("id: " + id+" youtubeid: " + str(tubeid)+"failed")"""

        """
    dirs=os.listdir(video_info_root)
    for videoinfo in dirs:
        videoid="default"
        for id,tubeid in conversionmap.items():
            if tubeid==videoinfo:
                videoid=id
        tmp_path=video_info_root+"/"+videoinfo #某个视频的文件夹
        #print(tmp_path)
    """
    print("================================")
    print(failid)
    f=open("./failed.txt",mode='w')
    f.write(failid,failid+"\n")
    f.close()
    # for videoid,tubeid in conversionmap.items():

else:
    print("ERROR: conversion map not exist.")

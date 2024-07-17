import requests
import re
import json
import subprocess
from pprint import pprint
import os
import tkinter as tk


def GETResponse(url):
    headers = {
        "Cookie": "_uuid=C4992879-9610F-710CB-457A-BBFADBAF939527733infoc; enable_web_push=DISABLE; home_feed_column=5; browser_resolution=1415-793; CURRENT_FNVAL=4048; rpdid=|(k|uk)uku~m0J'u~umR|mlRm; b_nut=1719409613; buvid3=7493D396-6C2B-3736-6A8B-DAFC118FDFAD13677infoc; header_theme_version=CLOSE; buvid_fp_plain=undefined; DedeUserID=402904417; DedeUserID__ckMd5=65ebded2d14e1979; CURRENT_QUALITY=80; fingerprint=b5fb8f9c8fd55b83924bb459756cdc20; bp_t_offset_402904417=950264095515344896; SESSDATA=250fa272%2C1735906891%2C81fee%2A71CjD8EBpVnZe2Rf4kBOc2jf14nevrQvJhsvgQnD63sf94iohLFE_Gg5hD4Fu3PqPRI8gSVlRFRkdXWk10MlQydDJpZWJIdEVIbThZQUg4clZVTXp1UlRjRm5pY0FSUW55cE1XdXRYOVlhWXdOajFkRUE3WkFzZW5mWFRaWWxtVk56Z3pzRGlnWkpRIIEC; bili_jct=24ff204ca3908e931671b4234a671c00; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjA2MTQwOTUsImlhdCI6MTcyMDM1NDgzNSwicGx0IjotMX0.WQdmcc5lRJXECzH175RjOiGJUOtGxNr-ZaCxV6nE7HE; bili_ticket_expires=1720614035; b_lsid=E1BF110D6_1908DDC60C5; buvid4=3E9E78AC-3696-7018-EB56-1238E265005449865-024070715-%2B8iWGFCKcue86uehHeNCYw%3D%3D; bsource=search_baidu; sid=7o48tkrr; buvid_fp=b5fb8f9c8fd55b83924bb459756cdc20; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com",
        "Referer": "https://www.bilibili.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"}
    response = requests.get(url, headers=headers)
    return response


def Xusa():
    url = Url.get()
    title = TItle.get()
    response = GETResponse(url)
    HTML = response.text
    info = re.findall("<script>window.__playinfo__=(.*?)</script>", HTML)
    if info:
        json_data = json.loads(info[0])
        audio_url = json_data["data"]["dash"]["audio"][0]["baseUrl"]
        video_url = json_data["data"]["dash"]["video"][0]["baseUrl"]
        pprint(audio_url)
        pprint(video_url)
        au = GETResponse(url=audio_url).content
        v = GETResponse(url=video_url).content
        with open('date\\' + '功夫足勤' + '.mp4', mode='wb') as video:
            video.write(v)
        with open('date\\' + '功夫足勤' + '.mp3', mode='wb') as audio:
            audio.write(au)
        input_video_path = f"date\\\\功夫足勤.mp4"
        input_audio_path = f"date\\\\功夫足勤.mp3"
        output_path = f"date\\\\{title}.mp4"
        command = f"ffmpeg -hide_banner -i {input_video_path} -i {input_audio_path} -c:v copy -c:a aac -strict experimental {output_path}"

        subprocess.run(command)
        if os.path.exists(output_path):
            os.remove(input_video_path)
            os.remove(input_audio_path)
            xsx.config(text="下载完成")
    else:
        xsx.config(text="视频地址错误或者更换cookie")

if not os.path.exists('date'):
    # 创建目录
    os.makedirs('date')
video = tk.Tk()
video.geometry("400x300")
video.title("bilibili视频下载器")
URL = tk.Label(video, text="请输入视频连接", font=("微软雅黑", 10))
URL.pack()
Url = tk.Entry(video, font=("微软雅黑", 10))
Url.pack()
Title = tk.Label(video, text="请输入视频标题", font=("微软雅黑", 10))
Title.pack()
TItle = tk.Entry(video, font=("微软雅黑", 10))
TItle.pack()
button = tk.Button(video, text="下载", font=("微软雅黑", 10), command=Xusa)
button.pack()
xsx=tk.Label(video, text="", font=("微软雅黑", 15))
xsx.pack()
video.mainloop()

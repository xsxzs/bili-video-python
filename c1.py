import requests
import re
import json
import subprocess
from pprint import pprint
import os

# 检查目录是否存在
if not os.path.exists('date'):
    # 创建目录
    os.makedirs('date')
def GETResponse(url):
    headers = {
        "Cookie": "_uuid=C4992879-9610F-710CB-457A-BBFADBAF939527733infoc; enable_web_push=DISABLE; home_feed_column=5; browser_resolution=1415-793; CURRENT_FNVAL=4048; rpdid=|(k|uk)uku~m0J'u~umR|mlRm; b_nut=1719409613; buvid3=7493D396-6C2B-3736-6A8B-DAFC118FDFAD13677infoc; header_theme_version=CLOSE; buvid_fp_plain=undefined; DedeUserID=402904417; DedeUserID__ckMd5=65ebded2d14e1979; CURRENT_QUALITY=80; fingerprint=b5fb8f9c8fd55b83924bb459756cdc20; bp_t_offset_402904417=950264095515344896; SESSDATA=250fa272%2C1735906891%2C81fee%2A71CjD8EBpVnZe2Rf4kBOc2jf14nevrQvJhsvgQnD63sf94iohLFE_Gg5hD4Fu3PqPRI8gSVlRFRkdXWk10MlQydDJpZWJIdEVIbThZQUg4clZVTXp1UlRjRm5pY0FSUW55cE1XdXRYOVlhWXdOajFkRUE3WkFzZW5mWFRaWWxtVk56Z3pzRGlnWkpRIIEC; bili_jct=24ff204ca3908e931671b4234a671c00; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjA2MTQwOTUsImlhdCI6MTcyMDM1NDgzNSwicGx0IjotMX0.WQdmcc5lRJXECzH175RjOiGJUOtGxNr-ZaCxV6nE7HE; bili_ticket_expires=1720614035; b_lsid=E1BF110D6_1908DDC60C5; buvid4=3E9E78AC-3696-7018-EB56-1238E265005449865-024070715-%2B8iWGFCKcue86uehHeNCYw%3D%3D; bsource=search_baidu; sid=7o48tkrr; buvid_fp=b5fb8f9c8fd55b83924bb459756cdc20; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com",
        "Referer": "https://www.bilibili.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"}
    response = requests.get(url, headers=headers)
    return response


def save():
    a = "https://cn-xj-ct-01-01.bilivideo.com/upgcxcode/38/89/1606798938/1606798938-1-100113.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1720374943&gen=playurlv2&os=bcache&oi=465275031&trid=0000244236c0f6244adf9364979cee1078b5u&mid=402904417&platform=pc&og=hw&upsig=3f66dd491966267a81bcd24619286f43&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=87001&bvc=vod&nettype=0&orderid=0,3&buvid=7493D396-6C2B-3736-6A8B-DAFC118FDFAD13677infoc&build=0&f=u_0_0&agrr=0&bw=132298&logo=80000000"
    b = "https://cn-xj-ct-01-01.bilivideo.com/upgcxcode/38/89/1606798938/1606798938-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1720374943&gen=playurlv2&os=bcache&oi=465275031&trid=0000244236c0f6244adf9364979cee1078b5u&mid=402904417&platform=pc&og=cos&upsig=2f7fbd06e44560f18f682547fc21cb7e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=87001&bvc=vod&nettype=0&orderid=0,3&buvid=7493D396-6C2B-3736-6A8B-DAFC118FDFAD13677infoc&build=0&f=u_0_0&agrr=0&bw=16930&logo=80000000"
    v = GETResponse(url=a).content
    au = GETResponse(url=b).content
    with open('date\\' + '功夫足勤' + '.mp4', mode='wb') as video:
        video.write(v)
    with open('date\\' + '功夫足勤' + '.mp3', mode='wb') as audio:
        audio.write(au)
    input_video_path = f"date\\\\功夫足勤.mp4"
    input_audio_path = f"date\\\\功夫足勤.mp3"
    output_path = f"date\\\\output2.mp4"

    command = f"ffmpeg -hide_banner -i {input_video_path} -i {input_audio_path} -c:v copy -c:a aac -strict experimental {output_path}"

    subprocess.run(command)
    if subprocess.run(command, check=True):
     if os.path.exists(output_path):
        os.remove(input_video_path)
        os.remove(input_audio_path)

if __name__ == '__main__':
    save()

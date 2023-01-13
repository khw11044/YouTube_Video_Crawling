from pytube import YouTube
import os

DOWNLOAD_FOLDER = './video_bank'

# if not os.path.isdir(DOWNLOAD_FOLDER):
#     os.mkdir(DOWNLOAD_FOLDER)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


url_list = [
    "https://www.youtube.com/watch?v=6A2h_6NkJyA&t=13s",
    "https://www.youtube.com/watch?v=vZ4yeGBLPEk&t=3s",
    "https://www.youtube.com/watch?v=hBTyb0yTxEc",
    "https://www.youtube.com/watch?v=RkAw4iQ3DIk&t=12s",
    "https://www.youtube.com/watch?v=MrWX1MKTnLA&t=305s",
    "https://www.youtube.com/watch?v=C-yMKcMwviM&t=240s",
    "https://www.youtube.com/watch?v=Rr_srUguvgs&t=501s",
    "https://www.youtube.com/watch?v=LHlK7RwgjX8&t=224s",
    "https://www.youtube.com/watch?v=4cLtMACs7To&t=31s",
    "https://www.youtube.com/watch?v=QLb2hDGY0n0&t=275s",
    "https://www.youtube.com/watch?v=cnAp9wtFhiQ&t=40s",
    "https://www.youtube.com/watch?v=S0X-y3o_m4U&t=205s",
    "https://www.youtube.com/watch?v=XuET97HFSOc",
    "https://www.youtube.com/watch?v=1XHkNLSY9l8&t=31s",
    "https://www.youtube.com/watch?v=s-qmRHbHVBU",
    "https://www.youtube.com/watch?v=lAF9qwR1L1U",
    "https://www.youtube.com/watch?v=diBvnIj_Dcg",
    "https://www.youtube.com/watch?v=5bOFqpbjm78",
    "https://www.youtube.com/watch?v=oawli_2CJss&t=27s",
    "https://www.youtube.com/watch?v=6PvvRJLB_pg",
    "https://www.youtube.com/watch?v=q-Pu3iNqXXc",
    "https://www.youtube.com/watch?v=WAxf8KFBUQM&t=82s",
    "https://www.youtube.com/watch?v=rPiPlol0-Aw",
    "https://www.youtube.com/watch?v=MXGA7AHYJTw&t=61s",
    "https://www.youtube.com/watch?v=IqIBjhVtKdo",
    "https://www.youtube.com/watch?v=zhdyJfKzcro",
    "https://www.youtube.com/watch?v=XNtv3t2wU8A",
    "https://www.youtube.com/watch?v=gFNC0_XQKBQ",
    "https://www.youtube.com/watch?v=aLQOR0T7LYo",
    "https://www.youtube.com/watch?v=Ke7U1hKTP2I"
    "https://www.youtube.com/watch?v=vvwQlevhyJc",
    "https://www.youtube.com/watch?v=4Oub5b467vI",
    "https://www.youtube.com/watch?v=EMzkR5XSHO8",
    "https://www.youtube.com/watch?v=_whNHQC4hCw",
    "https://www.youtube.com/watch?v=zAuzlPyaRuo&t=357s",
    "https://www.youtube.com/watch?v=p0_ASS7DX9Y",
    "https://www.youtube.com/watch?v=wzqSoRoOh08",
    "https://www.youtube.com/watch?v=799SbrTToXU",
    "https://www.youtube.com/watch?v=rTAQ2QNgRUQ",
    "https://www.youtube.com/watch?v=_rHf6dDJATY&t=394s",
    "https://www.youtube.com/watch?v=8Tx6hjBLiGs",
    "https://www.youtube.com/watch?v=CueAqbsQlds",
    "https://www.youtube.com/watch?v=Cj7jmQAyoRQ&t=18s",
    "https://www.youtube.com/watch?v=mKL8Pb8x9gU&t=355s",
    "https://www.youtube.com/watch?v=kxV7zzcamjQ",
    "https://www.youtube.com/watch?v=xt1V-oDt7Ic",
    "https://www.youtube.com/watch?v=_VWJfeH6WsM",
    "https://www.youtube.com/watch?v=Pu33qw5naBM",
    "https://www.youtube.com/watch?v=JB0xBj6VLYo",
    "https://www.youtube.com/watch?v=3UDpFSjnTU4",
    "https://www.youtube.com/watch?v=f66pcVzXzf8",
    "https://www.youtube.com/watch?v=wDV2kjjmupM",
    "https://www.youtube.com/watch?v=jVhRJq03wcs",
    "https://www.youtube.com/watch?v=G4OxV-jnyDY",
    "https://www.youtube.com/watch?v=1i0tSWkvKrU",
    "https://www.youtube.com/watch?v=OFZ0Cm6kYuQ",
    "https://www.youtube.com/watch?v=2XtVJDJZJlU",
    "https://www.youtube.com/watch?v=gW2_S1BBFqE",
    "https://www.youtube.com/watch?v=S_MYfEJx6pU",
    "https://www.youtube.com/watch?v=r7ROofzGI7Y",
    "https://www.youtube.com/watch?v=zDheOLEEmdU",
    "https://www.youtube.com/watch?v=NlRieTnBwmI",
    "https://www.youtube.com/watch?v=a5giJkDv_eU",
    "https://www.youtube.com/watch?v=KGv6rHPlU2g",
    "https://www.youtube.com/watch?v=IEVnN9ajfvk",
    "https://www.youtube.com/watch?v=EDKqBjdaG2c",
    "https://www.youtube.com/watch?v=mib7jDgfWgw",
    "https://www.youtube.com/watch?v=iEamT53A1lE",
    "https://www.youtube.com/watch?v=FY0A2heJjMc",
    "https://www.youtube.com/watch?v=K8Gnvzkv0sM",
    "https://www.youtube.com/watch?v=rxsa8x4_-Xo",
    "https://www.youtube.com/watch?v=OupEVWpttH0",
    "https://www.youtube.com/watch?v=KAVCw1QlMGY",
    "https://www.youtube.com/watch?v=gFwQlRj6QUA",
    "https://www.youtube.com/watch?v=NmxpafzSdjs",
    "https://www.youtube.com/watch?v=WxfNDYDLKOo",
    "https://www.youtube.com/watch?v=U9V9n_o1YTY",
    "https://www.youtube.com/watch?v=ZWhaGWWZ9pE",
    "https://www.youtube.com/watch?v=mph6AVLEuw4&t=26s"

]

count = 0
for url in url_list:
    try:
        print(url)
        yt = YouTube(url)
        print("제목 : ", yt.title)
        print("프레임 수: ", yt.views)
        print("비디오 길이: ", yt.length, "seconds")
        stream = yt.streams.get_highest_resolution()
        stream.download(DOWNLOAD_FOLDER)
        count += 1
        print(count)
    except:
        print('error and next')

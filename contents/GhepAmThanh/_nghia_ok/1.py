from modules.MyExecute import MyExecute
from modules.MyNewPath import MyNewPath
from modules.MyLog import MyLog


import os
import glob
import threading
from time import sleep


def HamXuLi(mp4_file):
    MyLog.Title(mp4_file)

    audio = MyNewPath(mp4_file) + ".wav"
    mp4_vn1_nghia = MyNewPath(mp4_file) + "_vn1_nghia.mp4"
    mp4_vn2_nghia = MyNewPath(mp4_file) + "_vn2_nghia.mp4"

    MyExecute(f'ffmpeg -i {mp4_file} -c:v copy -an {mp4_vn1_nghia}')
    MyExecute(
        f'ffmpeg -i {mp4_vn1_nghia} -i {audio} -c:v copy -c:a aac -strict experimental {mp4_vn2_nghia}')


def middleware(i):
    while True:
        try:
            HamXuLi(i)
            break
        except Exception as e:
            MyLog.Error(f"Object: {i}")
            MyLog.Error(f"Lỗi ghép âm thanh: {e}")


def GhepAmThanh(root_dir):
    MyLog.Infor(root_dir)

    mp4_files = glob.glob(os.path.join(
        root_dir, '**/*.mp4'), recursive=True)

    if (len(mp4_files) % 2 == 1):
        end = mp4_files.pop()
        middleware(end)

    for i in range(0, len(mp4_files)-1, 2):
        thread1 = threading.Thread(target=middleware, args=(mp4_files[i],))
        thread2 = threading.Thread(target=middleware, args=(mp4_files[i+1],))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        sleep(10)

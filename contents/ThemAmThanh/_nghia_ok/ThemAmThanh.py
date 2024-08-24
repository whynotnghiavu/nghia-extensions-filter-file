from modules.MyFile import MyFile
from modules.TinhGiay import TinhGiay
from modules.MyExecute import MyExecute
from modules.MyNoSound import MyNoSound
# from modules.FormatFileSub import FormatFileSub


from config.MyConst import MyConst


# import os

from tqdm import tqdm
import shutil

from moviepy.editor import VideoFileClip
import pysrt
import os
from modules.MyNewPath import MyNewPath
from pydub import AudioSegment


def ThemAmThanh(root_dir):

    mp4_files = MyFile.TimKiem(root_dir, MyConst.MP4)

    # for mp4_file in mp4_files:
    for mp4_file in tqdm(mp4_files, desc='Thêm âm thanh', unit='mp4_file'):
        video = VideoFileClip(mp4_file)
        time_video = video.duration
        video.close()

        sub_file = MyNewPath(mp4_file)+MyConst.V2_VVN_NGHIA

        new_folder1 = MyNewPath(
            sub_file)[:-len(MyConst.V2_VVN_NGHIA.replace(".nghia", ""))]
        # new_folder2 = os.path.join(new_folder1, "data")

        # if os.path.exists(new_folder2):
        #     shutil.rmtree(new_folder2)
        # os.makedirs(new_folder2, exist_ok=True)

        # print(sub_file)
        subs = pysrt.open(sub_file, encoding='utf-8')
        flag = pysrt.SubRipTime(hours=0, minutes=0, seconds=0, milliseconds=0)
        for sub in subs:
            # tqdm(subs, desc='Thêm âm thanh', unit='sub'):
            # for sub in tqdm(subs, desc='Thêm âm thanh', unit='sub'):
            _time = TinhGiay(sub.start - flag)
            _file = os.path.join(
                new_folder1,  f"{sub.index:0>9} - Copy{MyConst.WAV}")
            MyNoSound(time=_time, file=_file)
            flag = sub.end
        # end.wav
        _time = time_video - TinhGiay(sub.end)
        _file = os.path.join(new_folder1,  f"end{MyConst.WAV}")
        MyNoSound(_time,  _file)

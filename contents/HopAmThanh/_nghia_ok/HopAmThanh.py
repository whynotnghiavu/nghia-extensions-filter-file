from modules.MyFile import MyFile
from modules.TinhGiay import TinhGiay
from modules.MyExecute import MyExecute
# from modules.FormatFileSub import FormatFileSub


from config.MyConst import MyConst


# import os

from tqdm import tqdm
import shutil

import pysrt
import os
from modules.MyNewPath import MyNewPath
from pydub import AudioSegment


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


def HopAmThanh(root_dir):

    mp4_files = MyFile.TimKiem(root_dir, MyConst.MP4)

    for mp4_file in mp4_files:
        print(mp4_file)
        # video = VideoFileClip(mp4_file)
        # time_video = video.duration
        # video.close()
        # # print(time_video)
        # # print(time_video)

        sub_file = MyNewPath(mp4_file)+MyConst.V2_VVN_NGHIA

        # subs = pysrt.open(sub_file, encoding='utf-8')

        new_folder1 = MyNewPath(
            sub_file)[:-len(MyConst.V2_VVN_NGHIA.replace(".nghia", ""))]

        # new_folder2 = os.path.join(new_folder1, "data")

        wav_files = MyFile.TimKiem(new_folder1, MyConst.WAV)

        merged_audio = AudioSegment.empty()

        # for wav_file in wav_files:
        for wav_file in tqdm(wav_files, desc='Hợp âm thanh', unit='wav_file'):
            audio = AudioSegment.from_wav(wav_file)
            merged_audio += audio

        new_file = MyNewPath(sub_file)[
            :-len(MyConst.V2_VVN_NGHIA.replace(".nghia", ""))]+MyConst.WAV
        merged_audio.export(new_file, format="wav")

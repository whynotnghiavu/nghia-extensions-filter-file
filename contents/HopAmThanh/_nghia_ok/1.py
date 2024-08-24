from modules.MyNewPath import MyNewPath
from modules.MyLog import MyLog


import os
import glob
import shutil
from time import sleep


from pydub import AudioSegment


def HopAmThanh(root_dir):
    MyLog.Infor(root_dir)

    mp4_files = glob.glob(os.path.join(
        root_dir, '**/*.mp4'), recursive=True)

    for mp4_file in mp4_files:
        try:
            output = (MyNewPath(mp4_file))

            wav_files = glob.glob(os.path.join(
                output, '**/*.wav'), recursive=True)

            merged_audio = AudioSegment.empty()

            for wav_file in wav_files:

                MyLog.Infor(f"Hợp: {(wav_file)}")
                audio = AudioSegment.from_wav(wav_file)
                merged_audio += audio

            temp = output+".wav"
            merged_audio.export(temp, format="wav")
            sleep(1)
            shutil.rmtree(output)
            MyLog.Done(f"Đã hợp: {(temp)}")
        except Exception as e:
            MyLog.Error(f"Object: {mp4_file}")
            MyLog.Error(f"Lỗi hợp âm thanh: {e}")
            exit()

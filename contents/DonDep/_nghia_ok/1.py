import os
from modules.DoiTenFileSub import DoiTenFileSub

from modules.MyFile import MyFile
from modules.MyNewPath import MyNewPath

from config.MyConst import MyConst

import shutil

def DonDep(root_dir):
    mp4_files = MyFile.TimKiem(root_dir, MyConst.MP4)

    for mp4_file in mp4_files:
        if not mp4_file.endswith(MyConst.MP4_V2_NGHIA):
            os.remove(mp4_file)

    MyFile.Xoa(root_dir, MyConst.WAV)
    MyFile.Xoa(root_dir, MyConst.EN_VVN_NGHIA)
    MyFile.Xoa(root_dir, MyConst.MM_VVN_NGHIA)
    MyFile.Xoa(root_dir, MyConst.V1_VVN_NGHIA)

    # DoiTenFileSub(root_dir)


    # 
    mp4_files = MyFile.TimKiem(root_dir, MyConst.MP4)
    
    for mp4_file in mp4_files:
        new = MyNewPath(mp4_file)[:-len("_vn2_nghia")]

        if os.path.exists(new):
            shutil.rmtree(new) 
    # MyFile.Xoa(root_dir, ".zip")
    # MyFile.Xoa(root_dir, ".zip")
    # MyFile.Xoa(root_dir, ".zip")
    # MyFile.Xoa(root_dir, ".zip")
    # MyFile.Xoa(root_dir, ".zip")
    # MyFile.Xoa(root_dir, ".zip")
    # MyFile.Xoa(root_dir, ".zip")
    # MyFile.Xoa(root_dir, ".zip")
    # MyFile.Xoa(root_dir, ".srt")
    # MyFile.Xoa(root_dir, ".vtt")
from modules.MyNewPath import MyNewPath
from modules.MyLog import MyLog


import os
import glob


def delete_files_with_extension(root_dir, ext):
    file_paths = glob.glob(os.path.join(
        root_dir, f'**/*{ext}'), recursive=True)

    if file_paths:
        for file_path in file_paths:
            try:
                os.remove(file_path)
                MyLog.Infor(f"Đã xóa: {file_path}")
            except Exception as e:
                MyLog.Error(f"Object: {file_path}")
                MyLog.Error(f"Lỗi xóa file {ext}: {e}")
                exit()
    else:
        MyLog.Done(f"Không có file {ext}")


def DonDep(root_dir):
    MyLog.Infor(root_dir)

    delete_files_with_extension(root_dir, ".wav")

    temp = glob.glob(os.path.join(
        root_dir, "**/*.mp4"), recursive=True)

    for i in temp:
        if not i.endswith("_vn2_nghia.mp4"):
            os.remove(i)
            MyLog.Infor(f"Đã xóa: {(i)}")

    temp = glob.glob(os.path.join(
        root_dir, "**/*.vtt"), recursive=True)
    temp += glob.glob(os.path.join(
        root_dir, "**/*.srt"), recursive=True)

    for i in temp:
        if not i.endswith("_vn2_nghia.srt"):
            os.remove(i)
            MyLog.Infor(f"Đã xóa: {(i)}")

from modules.MyFile import MyFile


import os
import re


def DoiTenFile(root_dir):
    files = MyFile.TimKiem(root_dir, ".mp4")
    files += MyFile.TimKiem(root_dir, ".vtt")
    files += MyFile.TimKiem(root_dir, ".srt")

    for file in files:
        match = re.match(r'^\d+', os.path.basename(file))
        if match:
            so_thu_tu = int(match.group())
            _, ext = os.path.splitext(file)

            new_name = os.path.join(os.path.dirname(
                file), f"{so_thu_tu:0>9}{ext}")

            os.rename(file, new_name)
        else:
            print(f"Không tìm thấy số thứ tự: {file}")
            exit()

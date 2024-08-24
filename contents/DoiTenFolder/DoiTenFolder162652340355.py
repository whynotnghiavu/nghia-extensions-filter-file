from modules.MyFile import MyFile


import os
import re


def DoiTenFolder(root_dir): 
    for foldername, subfolders, filenames in os.walk(root_dir):

        for subfolder in subfolders:
            subfolder_path = os.path.join(foldername, subfolder)
            match = re.match(r'^\d+', os.path.basename(subfolder_path))
            if match:
                so_thu_tu = int(match.group())
                new_name = os.path.join(foldername, f"{so_thu_tu:0>9}")
                try:
                    if (subfolder_path != new_name):
                        os.rename(subfolder_path, new_name)
                except Exception as e:
                    print(f"Object: {subfolder_path}")
                    print(f"Lỗi đổi tên: {e}")
                    exit()
            else:
                print(f"Object: {subfolder_path}")
                print("Không tìm thấy số thứ tự.")
from modules.MyFile import MyFile
from modules.MyNewPath import MyNewPath
from modules.FormatFileSub import FormatFileSub


from config.MyConst import MyConst


import os


def TachFileSub(root_dir):
    infor_file = open("backup/infor.txt", "r", encoding="utf-8")
    sub_files = infor_file.readlines()

    merged_file = open("backup/merged.vi.srt", "r", encoding="utf-8")
    contents = merged_file.read()
    contents = contents.split("@@@")

    if len(contents) != len(sub_files):
        print(f"Lỗi: Số file và tên không bằng nhau")
        print(f"len(sub_files) = {len(sub_files)}")
        print(f"len(contents) = {len(contents)}")
        exit()

    for i, sub_file in enumerate(sub_files):
        new_file = MyNewPath(sub_file)[
            :-len(MyConst.MM_VVN_NGHIA.replace(".nghia", ""))]+MyConst.V1_VVN_NGHIA
        if not os.path.exists(new_file):
            with open(new_file, "w", encoding="utf-8") as split_file:
                split_file.write(contents[i])

    # format lại file
    sub_files = MyFile.TimKiem(root_dir,  MyConst.V1_VVN_NGHIA)

    for sub_file in sub_files:
        new_file = MyNewPath(sub_file)[
            :-len(MyConst.V1_VVN_NGHIA.replace(".nghia", ""))]+MyConst.V2_VVN_NGHIA
        if not os.path.exists(new_file):
            new_sub = FormatFileSub(sub_file)
            new_sub.save(new_file, encoding='utf-8')

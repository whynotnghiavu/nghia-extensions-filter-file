from modules.MyFile import MyFile


from config.MyConst import MyConst


import os


def HopNhatFileSub(root_dir):
    sub_files = MyFile.TimKiem(root_dir, MyConst.MM_VVN_NGHIA)

    if not os.path.exists(f"backup"):
        os.makedirs(f"backup")

    infor_file = open("backup/infor.txt", "w", encoding="utf-8")
    merged_file = open("backup/merged.srt", "w", encoding="utf-8")

    for sub_file in sub_files:
        with open(sub_file, "r", encoding="utf-8") as srt_file:
            contents = srt_file.read()

        merged_file.write("@@@\n")
        merged_file.write(contents)
        merged_file.write("\n")

        infor_file.write(f"{sub_file}\n")

    infor_file.close()
    merged_file.close()

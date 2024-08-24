from modules.MyFile import MyFile
from config.MyConfig import MyConfig

import os


def XoaFileSub(root_dir):
    exts = [

        " de",
        " es",
        " fr",
        " id",
        " it",
        " pt",


        "_de",
        "_es",
        "_fr",
        "_id",
        "_it",
        "_pt",


        "French",
        "German",
        "Spanish",
        "Italian",
        "Portuguese",
        "Arabic",
        # "Dutch",
        "French",
        "German",
        "Indonesian",
        "Italian",
        "Japanese",
        "Korean",
        "Portuguese",
        "Chinese",
        "Spanish",
        "Thai",
        "Turkish",
        "Bulgarian",
        "Czech",
        "Danish",
        "Estonian",
        "Finnish",
        "Greek",
        "Hungarian",
        "Latvian",
        "Lithuanian",
        "Romanian",
        "Slovak",
        "Swedish",
        "Ukrainian",

    ]
    option = []

    for i in exts:
        option.append(f"{i}.srt")
        option.append(f"{i}.vtt")

    sub_files = MyFile.TimKiem(root_dir, ".vtt")
    sub_files += MyFile.TimKiem(root_dir, ".srt")

    for sub_file in sub_files:
        for extension in option:
            if sub_file.endswith(extension):
                os.remove(sub_file)
                print(f"Đã xóa: {(sub_file)}")
                break

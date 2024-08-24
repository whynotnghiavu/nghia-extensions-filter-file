from modules.MyFile import MyFile
from modules.MyNewPath import MyNewPath


from config.MyConst import MyConst


import os
from datetime import timedelta

import pysrt

import shutil


def HopNhatCau(root_dir):
    sub_files = MyFile.TimKiem(root_dir, MyConst.EN_VVN_NGHIA)

    for sub_file in sub_files:
        print("🐍 File: modules/HopNhatCau.py | Line: 20 | HopNhatCau ~ sub_file",sub_file)
        new_file = MyNewPath(sub_file)[
            :-len(MyConst.EN_VVN_NGHIA.replace(".nghia", ""))]+MyConst.MM_VVN_NGHIA
        # sao chép file
        # shutil.copy2(sub_file, new_file)
        if not os.path.exists(new_file):

            subs_old = pysrt.open(sub_file, encoding='utf-8')
            subs_new = pysrt.SubRipFile()

            if (len(subs_old) == 0):
                print(f"File sub không có nội dung: {sub_file}")
                exit()

            flag = 0
            index = 1
            text = ""

            for i in range(len(subs_old)):
                text += " " + subs_old[i].text
                try:
                    condition = subs_old[i].text[-1]
                except:
                    condition = " "


                if condition in [".", "?", "..."] and len(text) > 100:
                    #             # if condition in [".", "?", "..."]:
                    #             if condition in [".", "?", "..."] and len(text) > 150:
                    #                 # if  len(text) > 500:
                    #                 # if condition in [".", "?", "..."] and len(text) > 200:
                    #                 # if condition in [".", "?", "..."]  and len(text)>300:
                    try:
                        subs_new.append(
                            pysrt.SubRipItem(
                                index=index,
                                start=subs_old[flag].start.to_time(),
                                end=subs_old[i].end.to_time(),
                                text=text.strip()
                            )
                        )
                    except:
                        subs_new.append(
                            pysrt.SubRipItem(
                                index=index,
                                start=subs_old[flag].start.to_time(),
                                end=subs_old[flag].start.to_time() ,
                                text=text.strip()
                            )
                        )


                    flag = i + 1
                    index += 1
                    text = ""

                subs_new.save(new_file, encoding='utf-8')

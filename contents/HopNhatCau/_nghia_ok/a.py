from modules.MyNewPath import MyNewPath
from modules.MyLog import MyLog


import os
import glob


import pysrt


def HopNhatCau(root_dir):
    MyLog.Infor(root_dir)

    sub_files = glob.glob(os.path.join(
        root_dir, "**/*_en_nghia.srt"), recursive=True)

    for sub_file in sub_files:

        subs_old = pysrt.open(sub_file, encoding='utf-8')
        subs_new = pysrt.SubRipFile()

        if (len(subs_old) == 0):
            MyLog.Error(f"Object: {sub_file}")
            MyLog.Error("File sub không có nội dung")
            exit()

        flag = 0
        index = 0
        text = ""

        for i in range(len(subs_old)):
            text += " " + subs_old[i].text
            condition = subs_old[i].text[-1]

            # if condition in [".", "?", "..."]:
            if condition in [".", "?", "..."] and len(text) > 150:
                # if  len(text) > 500:
                # if condition in [".", "?", "..."] and len(text) > 200:
                # if condition in [".", "?", "..."]  and len(text)>300:
                subs_new.append(
                    pysrt.SubRipItem(
                        index=index,
                        start=subs_old[flag].start.to_time(),
                        end=subs_old[i].end.to_time(),
                        text=text.strip()
                    )
                )

                flag = i + 1
                index += 1
                text = ""

        temp = MyNewPath(sub_file)[:-9]+"_m_nghia.srt"
        subs_new.save(temp, encoding='utf-8')
        MyLog.Infor(f"Đã hợp: {(temp)}")

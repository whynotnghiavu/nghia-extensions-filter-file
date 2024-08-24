from modules.MyNewPath import MyNewPath
from modules.MyLog import MyLog


import os
import glob


import pysrt


def TachFileSub(root_dir):
    MyLog.Infor(root_dir)

    infor_file = open("backup/infor.txt", "r", encoding="utf-8")
    sub_files = infor_file.readlines()

    merged_file = open("backup/merged.vi.srt", "r", encoding="utf-8")
    contents = merged_file.read()
    contents = contents.split("@@@")

    if len(contents) != len(sub_files):
        MyLog.Error(f"Lỗi: Số file và tên không bằng nhau")
        MyLog.Error(f"Object: len(sub_files) = {len(sub_files)}")
        MyLog.Error(f"Object: len(contents) = {len(contents)}")
        exit()
    else:
        MyLog.Infor(f"Số file và tên bằng nhau")

    for i, sub_file in enumerate(sub_files):
        temp = MyNewPath(sub_file)[:-8]+"_vn1_nghia.srt"

        with open(temp, "w", encoding="utf-8") as split_file:
            split_file.write(contents[i])

    # format lại file như tạo file sub
    sub_files = glob.glob(os.path.join(
        root_dir, '**/*_vn1_nghia.srt'), recursive=True)

    for sub_file in sub_files:
        try:
            file_new = pysrt.SubRipFile()

            with open(sub_file, "r", encoding="utf-8") as file_old:
                contents_old = file_old.readlines()

            # Đọc nội dung và lọc
            contents_new = []
            for i in range(len(contents_old)):
                if contents_old[i].strip() == "":
                    continue
                elif contents_old[i].strip() == "WEBVTT":
                    continue
                elif contents_old[i].strip().isnumeric():
                    continue
                elif "\ufeff" in contents_old[i].strip():
                    continue
                else:
                    contents_new.append(contents_old[i].strip())

            # Tạo file mới
            index = 0
            if not ("-->" in contents_new[0].strip()):
                MyLog.Error(f"Object: {sub_file}")
                MyLog.Error(f"Dòng đầu tiên không phải thời gian")
                # MyLog.Error(f"_{contents_new[0].strip()}_")
                exit()

            for i in range(len(contents_new)):
                line = contents_new[i].strip()

                if ("-->" in line):
                    index += 1
                    start = line.split("-->")[0].strip()
                    end = line.split("-->")[1].strip()
                    text = " "
                    for j in range(i+1, len(contents_new)):
                        if "-->" in contents_new[j].strip():
                            break
                        text += " "+contents_new[j].strip()

                    file_new.append(
                        pysrt.SubRipItem(
                            index=index,
                            start=pysrt.SubRipTime.from_string(start),
                            end=pysrt.SubRipTime.from_string(end),
                            text=text.strip()
                        )
                    )

        except Exception as e:
            MyLog.Error(f"Object: {sub_file}")
            MyLog.Error(f"Lỗi tách file sub: {e}")
            exit()

        temp = MyNewPath(sub_file)[:-10]+"_vn2_nghia.srt"
        file_new.save(temp, encoding='utf-8')
        MyLog.Infor(f"Đã tách: {temp}")

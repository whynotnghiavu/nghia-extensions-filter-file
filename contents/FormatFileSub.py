import pysrt


def convert_time(time):
    try:
        output = pysrt.SubRipTime.from_string(time)
    except:
        time = "00:" + time
        time = time.replace(".", ",")
        output = pysrt.SubRipTime.from_string(time)

    return output


def FormatFileSub(file):
    file_new = pysrt.SubRipFile()

    with open(file, "r", encoding="utf-8", errors='replace') as file_old:
        contents_old = file_old.readlines()

    # Đọc nội dung và lọc
    contents_new = []
    for i in range(len(contents_old)):
        if contents_old[i].strip() == "":
            continue
        elif contents_old[i].strip() == "WEBVTT":
            continue
        elif contents_old[i].strip() == "Kind: captions":
            continue
        elif contents_old[i].strip() == "Language: en":
            continue
        elif contents_old[i].strip().isnumeric():
            continue



        
        # elif contents_old[i].strip() == "Tipo: subtítulos":
        #     continue



        
        # elif contents_old[i].strip() == "Idioma: es":
        #     continue




        elif "\ufeff" in contents_old[i].strip():
            continue
        else:
            contents_new.append(contents_old[i].strip())

    if not ("-->" in contents_new[0].strip()):
        print(f"Dòng đầu tiên không phải thời gian: {file}")
        exit()

    # Tạo file mới
    index = 0
    for i in range(len(contents_new)):
        line = contents_new[i].strip()
        print("🐍 File: modules/FormatFileSub.py | Line: 43 | FormatFileSub ~ line",line)

        if ("-->" in line):
            line=line.replace("line:15%", "")
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
                    start=(convert_time(start)),
                    end=(convert_time(end)),
                    text=text.strip()
                )
            )

    return file_new

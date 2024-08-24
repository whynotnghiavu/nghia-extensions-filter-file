import os
import glob
import shutil







# Đường dẫn đến folder
folder_path = r"C:\Users\vvn20206205\Desktop\rrrr\HopNhatCau"


# Tạo thư mục "_nghia_ok"
_nghia_ok = os.path.join(folder_path, "_nghia_ok")
if not os.path.exists(_nghia_ok):
    os.makedirs(_nghia_ok)


# Tạo thư mục "_nghia_filter"
_nghia_filter = os.path.join(folder_path, "_nghia_filter")
if not os.path.exists(_nghia_filter):
    os.makedirs(_nghia_filter)


# Lấy danh sách tất cả các file trong folder
file_list = os.listdir(folder_path)
files_only = [f for f in file_list if os.path.isfile(os.path.join(folder_path, f))]


extensions = []
for file_name in files_only:
    # print(file_name)
    name, extension = os.path.splitext(file_name)
    extensions.append(extension)
extensions = list(set(extensions))
# print(extensions)


for extension in extensions:
    files = glob.glob(os.path.join(folder_path, f'**{extension}'))

    while len(files):
        file_path = files[0]
        files.remove(file_path)
        file_path = shutil.move(file_path, _nghia_ok)

        for other_file_path in files:
            with open(file_path, "r", encoding="utf-8") as file1:
                contents1 = file1.read()
            with open(other_file_path, "r", encoding="utf-8") as file2:
                contents2 = file2.read()
            if contents1 == contents2:

                files.remove(other_file_path)
                shutil.move(other_file_path, _nghia_filter)

 
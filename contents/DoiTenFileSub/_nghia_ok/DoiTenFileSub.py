from modules.MyFile import MyFile
from config.MyConst import MyConst
from modules.MyNewPath import MyNewPath


import os


def DoiTenFileSub(root_dir):
    sub_files = MyFile.TimKiem(root_dir, MyConst.V2_VVN_NGHIA)

    for sub_file in sub_files:
        # print(sub_file)
        new_file = MyNewPath(sub_file)[
            :-len(MyConst.V2_VVN_NGHIA.replace(".nghia", ""))]+""+MyConst.SRT
        #   :-len(MyConst.V2_VVN_NGHIA.replace(".nghia", ""))]+"_nghia"+MyConst.SRT
        # print(new_file)

  # Sử dụng hàm rename để đổi tên file
        # os.remove(  new_file)
        # os.rename(sub_file, new_file)

        # Kiểm tra xem file mới đã tồn tại chưa
        if os.path.exists(new_file):
            # Nếu file mới tồn tại, hãy xóa nó trước khi đổi tên file cũ
            os.remove(new_file)

        # Tiến hành đổi tên file cũ thành file mới
        os.rename(sub_file, new_file)

from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def addSinhVien(self):
        id = input("Nhập ID: ")
        ten = input("Nhập tên: ")
        gioi_tinh = input("Nhập giới tính: ")
        chuyen_nganh = input("Nhập chuyên ngành: ")
        dtb = float(input("Nhập điểm TB: "))
        sv = SinhVien(id, ten, gioi_tinh, chuyen_nganh, dtb)
        self.listSinhVien.append(sv)

    def showSinhVien(self):
        for sv in self.listSinhVien:
            print(f"ID: {sv.id} | Tên: {sv.ten} | Ngành: {sv.chuyen_nganh} | ĐTB: {sv.dtb} | Học lực: {sv.hoc_luc}")
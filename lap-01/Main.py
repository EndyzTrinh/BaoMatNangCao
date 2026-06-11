from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while True:
    print("\n--- QUẢN LÝ SINH VIÊN ---")
    print("1. Thêm sinh viên")
    print("2. Hiển thị danh sách")
    print("0. Thoát")
    chon = input("Chọn chức năng: ")
    if chon == '1': qlsv.addSinhVien()
    elif chon == '2': qlsv.showSinhVien()
    elif chon == '0': break
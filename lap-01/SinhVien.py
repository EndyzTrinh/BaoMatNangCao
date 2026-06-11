class SinhVien:
    def __init__(self, id, ten, gioi_tinh, chuyen_nganh, dtb):
        self.id = id
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.dtb = dtb
        self.hoc_luc = self.xep_loai()

    def xep_loai(self):
        if self.dtb >= 8: return "Giỏi"
        elif self.dtb >= 6.5: return "Khá"
        elif self.dtb >= 5: return "Trung bình"
        else: return "Yếu"
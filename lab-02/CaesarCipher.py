class CaesarCipher:
    def __init__(self, shift: int):
        # Khởi tạo khóa dịch chuyển (ví dụ: shift = 3)
        self.shift = shift

    def encrypt(self, text: str) -> str:
        """Hàm mã hóa văn bản"""
        result = ""
        for i in range(len(text)):
            char = text[i]
            # Mã hóa chữ hoa
            if char.isupper():
                result += chr((ord(char) + self.shift - 65) % 26 + 65)
            # Mã hóa chữ thường
            elif char.islower():
                result += chr((ord(char) + self.shift - 97) % 26 + 97)
            # Giữ nguyên khoảng trắng hoặc ký tự đặc biệt
            else:
                result += char
        return result

    def decrypt(self, text: str) -> str:
        """Hàm giải mã văn bản (ngược lại của mã hóa)"""
        result = ""
        for i in range(len(text)):
            char = text[i]
            # Giải mã chữ hoa
            if char.isupper():
                result += chr((ord(char) - self.shift - 65) % 26 + 65)
            # Giải mã chữ thường
            elif char.islower():
                result += chr((ord(char) - self.shift - 97) % 26 + 97)
            else:
                result += char
        return result
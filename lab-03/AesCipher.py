import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

class AesCipher:
    def __init__(self, key_str: str):
        # Đảm bảo khóa luôn có độ dài 32 bytes (256 bits) bằng cách băm hoặc điền đầy
        self.key = key_str.ljust(32, '0')[:32].encode('utf-8')

    def encrypt(self, plain_text: str) -> str:
        """Hàm mã hóa AES (Chế độ CBC)"""
        # Tạo chuỗi ngẫu nhiên IV (Initialization Vector) 16 bytes
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        # Thêm Padding để dữ liệu đủ kích thước block của AES (128 bits)
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text.encode('utf-8')) + padder.finalize()

        # Tiến hành mã hóa
        cipher_text = encryptor.update(padded_data) + encryptor.finalize()
        
        # Gộp IV và CipherText lại rồi chuyển sang chuỗi Base64 để dễ đọc/lưu trữ
        return base64.b64encode(iv + cipher_text).decode('utf-8')

    def decrypt(self, encrypted_text: str) -> str:
        """Hàm giải mã AES (Chế độ CBC)"""
        try:
            raw_data = base64.b64decode(encrypted_text.encode('utf-8'))
            iv = raw_data[:16] # Lấy 16 bytes đầu làm IV
            cipher_text = raw_data[16:] # Phần còn lại là văn bản mã hóa

            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
            decryptor = cipher.decryptor()

            # Tiến hành giải mã
            padded_data = decryptor.update(cipher_text) + decryptor.finalize()

            # Gỡ bỏ Padding để lấy lại văn bản gốc
            unpadder = padding.PKCS7(128).unpadder()
            plain_text = unpadder.update(padded_data) + unpadder.finalize()
            return plain_text.decode('utf-8')
        except Exception:
            return "Lỗi: Khóa giải mã không đúng hoặc dữ liệu bị bóp méo!"
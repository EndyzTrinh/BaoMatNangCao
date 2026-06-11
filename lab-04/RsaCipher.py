from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import base64

class RsaCipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        """Hàm tự động tạo cặp khóa Public - Private Key 2048-bit"""
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
        return "➔ Tạo cặp khóa thành công!"

    def get_public_key_pem(self) -> str:
        """Xuất khóa công khai định dạng PEM để hiển thị"""
        if not self.public_key:
            return "Chưa tạo khóa!"
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem.decode('utf-8')

    def encrypt(self, plain_text: str) -> str:
        """Hàm mã hóa bằng Khóa Công Khai (Public Key)"""
        if not self.public_key:
            return "Lỗi: Vui lòng tạo cặp khóa trước!"
        
        # Mã hóa sử dụng cấu hình OAEP bảo mật cao
        cipher_bytes = self.public_key.encrypt(
            plain_text.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return base64.b64encode(cipher_bytes).decode('utf-8')

    def decrypt(self, encrypted_text: str) -> str:
        """Hàm giải mã bằng Khóa Bí Mật (Private Key)"""
        if not self.private_key:
            return "Lỗi: Chưa có Khóa bí mật để giải mã!"
        try:
            cipher_bytes = base64.b64decode(encrypted_text.encode('utf-8'))
            plain_bytes = self.private_key.decrypt(
                cipher_bytes,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return plain_bytes.decode('utf-8')
        except Exception:
            return "Lỗi: Giải mã thất bại (Dữ liệu lỗi hoặc khóa sai)!"
import hashlib

class HashService:
    @staticmethod
    def hash_text(text: str, algorithm: str) -> str:
        """Hàm băm một chuỗi văn bản theo thuật toán chỉ định (md5, sha1, sha256)"""
        encoded_text = text.encode('utf-8')
        
        if algorithm.lower() == 'md5':
            return hashlib.md5(encoded_text).hexdigest()
        elif algorithm.lower() == 'sha1':
            return hashlib.sha1(encoded_text).hexdigest()
        elif algorithm.lower() == 'sha256':
            return hashlib.sha256(encoded_text).hexdigest()
        else:
            return "Thuật toán không được hỗ trợ!"

    @staticmethod
    def verify_integrity(original_hash: str, current_text: str, algorithm: str) -> bool:
        """Kiểm tra tính toàn vẹn: So sánh mã băm cũ với mã băm hiện tại"""
        current_hash = HashService.hash_text(current_text, algorithm)
        return original_hash.strip() == current_hash.strip()
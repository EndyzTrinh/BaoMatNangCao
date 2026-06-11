import sys
import os

# Thêm đường dẫn hiện tại vào hệ thống để tránh lỗi gạch đỏ import
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from AesCipher import AesCipher

def menu():
    # Nhập khóa bí mật ban đầu để khởi tạo hệ thống mã hóa
    print("--- KHỞI TẠO HỆ THỐNG BẢO MẬT AES ---")
    secret_key = input("Nhập khóa bí mật của bạn (ví dụ: mysecretkey123): ")
    aes = AesCipher(secret_key)
    
    while True:
        print("\n--- CHƯƠNG TRÌNH MÃ HÓA AES HIỆN ĐẠI (LAB 03) ---")
        print("1. Mã hóa văn bản (AES Encrypt)")
        print("2. Giải mã văn bản (AES Decrypt)")
        print("3. Thay đổi khóa bí mật")
        print("0. Thoát chương trình")
        
        choice = input("Chọn chức năng (0-3): ")
        
        if choice == "1":
            plain_text = input("Nhập chuỗi văn bản cần MÃ HÓA: ")
            encrypted_text = aes.encrypt(plain_text)
            print(f"➔ Chuỗi mã hóa (Base64): {encrypted_text}")
            
        elif choice == "2":
            cipher_text = input("Nhập chuỗi AES cần GIẢI MÃ: ")
            decrypted_text = aes.decrypt(cipher_text)
            print(f"➔ Kết quả sau khi giải mã: {decrypted_text}")
            
        elif choice == "3":
            secret_key = input("Nhập khóa bí mật MỚI: ")
            aes = AesCipher(secret_key)
            print("➔ Đã cập nhật khóa thành công!")
            
        elif choice == "0":
            print("Đang thoát chương trình Lab 03. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()
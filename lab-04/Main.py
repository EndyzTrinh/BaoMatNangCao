import sys
import os

# Tránh lỗi gạch đỏ import thư mục
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from RsaCipher import RsaCipher

def menu():
    rsa_system = RsaCipher()
    
    while True:
        print("\n--- CHƯƠNG TRÌNH MÃ HÓA BẤT ĐỐI XỨNG RSA (LAB 04) ---")
        print("1. Tạo cặp khóa ngẫu nhiên (Generate Key Pair)")
        print("2. Xem Khóa Công Khai hiện tại (View Public Key)")
        print("3. Mã hóa văn bản (Encrypt bằng Public Key)")
        print("4. Giải mã văn bản (Decrypt bằng Private Key)")
        print("0. Thoát chương trình")
        
        choice = input("Chọn chức năng (0-4): ")
        
        if choice == "1":
            print("Đang tạo cặp khóa 2048-bit (Vui lòng đợi giây lát)...")
            msg = rsa_system.generate_keys()
            print(msg)
            
        elif choice == "2":
            print("\n--- KHÓA CÔNG KHAI (PUBLIC KEY) ĐỊNH DẠNG PEM ---")
            print(rsa_system.get_public_key_pem())
            
        elif choice == "3":
            plain_text = input("Nhập chuỗi văn bản cần MÃ HÓA: ")
            encrypted_text = rsa_system.encrypt(plain_text)
            print(f"➔ Kết quả mã hóa RSA (Base64): {encrypted_text}")
            
        elif choice == "4":
            cipher_text = input("Nhập chuỗi RSA cần GIẢI MÃ: ")
            decrypted_text = rsa_system.decrypt(cipher_text)
            print(f"➔ Kết quả sau khi giải mã bằng Private Key: {decrypted_text}")
            
        elif choice == "0":
            print("Đang thoát chương trình Lab 04. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()
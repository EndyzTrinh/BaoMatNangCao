from CaesarCipher import CaesarCipher

def menu():
    # Khởi tạo thuật toán mã hóa Caesar với khóa mặc định là 3 bước
    shift_key = 3
    cipher = CaesarCipher(shift_key)
    
    while True:
        print("\n--- CHƯƠNG TRÌNH MÃ HÓA CAESAR (LAB 02) ---")
        print("1. Mã hóa văn bản (Encrypt)")
        print("2. Giải mã văn bản (Decrypt)")
        print("0. Thoát chương trình")
        
        choice = input("Chọn chức năng (0-2): ")
        
        if choice == "1":
            plain_text = input("Nhập chuỗi văn bản cần MÃ HÓA: ")
            encrypted_text = cipher.encrypt(plain_text)
            print(f"➔ Kết quả sau khi mã hóa: {encrypted_text}")
            
        elif choice == "2":
            cipher_text = input("Nhập chuỗi văn bản cần GIẢI MÃ: ")
            decrypted_text = cipher.decrypt(cipher_text)
            print(f"➔ Kết quả sau khi giải mã: {decrypted_text}")
            
        elif choice == "0":
            print("Đang thoát chương trình Lab 02. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    menu()
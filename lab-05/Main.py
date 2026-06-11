import sys
import os

# Tránh lỗi gạch đỏ import thư mục
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from HashService import HashService

def menu():
    # Khởi tạo một kho lưu trữ tạm thời để test tính toàn vẹn dữ liệu
    saved_hash = ""
    saved_algo = ""
    
    while True:
        print("\n--- CHƯƠNG TRÌNH BĂM DỮ LIỆU & KIỂM TRA TOÀN VẸN (LAB 05) ---")
        print("1. Băm văn bản (Tạo mã SHA-256 / SHA-1 / MD5)")
        print("2. Lưu văn bản gốc và tạo mã giám sát (Check-in)")
        print("3. Kiểm tra văn bản xem có bị thay đổi không (Verify Integrity)")
        print("0. Thoát chương trình")
        
        choice = input("Chọn chức năng (0-3): ")
        
        if choice == "1":
            text = input("Nhập chuỗi văn bản cần băm: ")
            print("Chọn thuật toán: MD5, SHA1, SHA256")
            algo = input("Nhập lựa chọn của bạn: ").strip()
            
            hash_result = HashService.hash_text(text, algo)
            print(f"➔ Kết quả băm ({algo.upper()}): {hash_result}")
            
        elif choice == "2":
            text = input("Nhập văn bản quan trọng cần bảo vệ tính toàn vẹn: ")
            saved_algo = "sha256"
            saved_hash = HashService.hash_text(text, saved_algo)
            print(f"➔ Đã tạo mã giám sát SHA-256 thành công!")
            print(f"➔ Mã băm gốc được lưu: {saved_hash}")
            
        elif choice == "3":
            if not saved_hash:
                print("Lỗi: Vui lòng chạy chức năng 2 để tạo mã giám sát trước!")
                continue
                
            text_to_check = input("Nhập lại văn bản muốn kiểm tra (Giả lập việc chỉnh sửa): ")
            is_safe = HashService.verify_integrity(saved_hash, text_to_check, saved_algo)
            
            print("\n--- KẾT QUẢ KIỂM TRA TÍNH TOÀN VẸN ---")
            if is_safe:
                print("💚 AN TOÀN: Văn bản hoàn toàn nguyên vẹn, không bị chỉnh sửa một ký tự nào!")
            else:
                print("❌ CẢNH BÁO: Dữ liệu đã bị thay đổi hoặc giả mạo bởi Hacker!")
            
        elif choice == "0":
            print("Đang thoát chương trình Lab 05. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()
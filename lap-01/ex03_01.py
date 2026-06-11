def tinh_tong_so_chan(lst):
    return sum(num for num in lst if num % 2 == 0)

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
print("Tổng các số chẵn trong List là:", tinh_tong_so_chan(numbers))
num_staff = int(input("Nhập số lượng nhân viên: "))

for i in range(num_staff):
    full_name = input("Nhập tên nhân viên: ")
    total_day = int(input("Nhập số ngày làm: "))

    if total_day < 0 or total_day > 22:
        print("Dữ liệu không hợp lệ!")
        continue

    elif total_day == 0:
        print("Nhân viên nghỉ toàn bộ tháng")
        continue

    print(full_name + ": " + "*" * total_day)

    if total_day >= 18:
        print("Làm việc chăm chỉ")

    elif total_day < 10:
        print("Làm việc ít")

    else:
        print("Làm việc bình thường")
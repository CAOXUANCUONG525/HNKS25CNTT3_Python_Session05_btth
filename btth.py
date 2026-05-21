import random

patient_name = input("Nhập tên bệnh nhân: ")
gender = input("Nhập giới tính: ")
birth_year = int(input("Nhập năm sinh: "))
phone = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
symptom = input("Nhập triệu chứng ban đầu: ")
medical_fee = float(input("Nhập chi phí khám: "))


patient_id = "BN" + str(birth_year) + str(random.randint(100, 999))

print("\nTHẺ BỆNH NHÂN")
print("-" * 35)

print("Mã BN        :", patient_id)
print("Tên          :", patient_name, f"({type(patient_name).__name__})")
print("Giới tính    :", gender, f"({type(gender).__name__})")
print("Năm sinh     :", birth_year, f"({type(birth_year).__name__})")
print("Điện thoại   :", phone, f"({type(phone).__name__})")
print("Email        :", email, f"({type(email).__name__})")
print("Triệu chứng  :", symptom, f"({type(symptom).__name__})")
print("Chi phí      :", medical_fee, "VND", f"({type(medical_fee).__name__})")

print("-" * 35)
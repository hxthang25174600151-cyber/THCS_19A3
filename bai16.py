chuoi = input("Nhập chuỗi: ")

tan_suat = {}

for i in chuoi:
    # kiểm tra xem ký tự đã có trong dict chưa
    co = False
    for key in tan_suat:
        if key == i:
            tan_suat[key] += 1
            co = True
            break
    if not co:
        tan_suat[i] = 1

print("Tần suất xuất hiện của các ký tự:")
for key in tan_suat:
    print(key, ":", tan_suat[key])
chuoi = input("Nhập chuỗi: ")

luu = ""
khoang_trang = False

for i in chuoi:
    if i == " ":
        if not khoang_trang:
            luu += i
        khoang_trang = True
    else:
        luu += i
        khoang_trang = False
print(luu)
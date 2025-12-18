chuoi = input("Nhập danh sách số nguyên: ")

ds = []
so = ""
for i in chuoi + " ":
    if i != " ":
        so += i
    else:
        if so != "":
            ds.append(int(so))
            so = ""

max1 = max2 = -999999999
for x in ds:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x

if max2 == -999999999:
    print("Không có giá trị lớn thứ hai")
else:
    print("Giá trị lớn thứ hai là:", max2)
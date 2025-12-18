chuoi = input("Nhập danh sách số nguyên: ")
target = int(input("Nhập giá trị tổng cần tìm: "))

ds = []
so = ""
for i in chuoi + " ":
    if i != " ":
        so += i
    else:
        if so != "":
            ds.append(int(so))
            so = ""

for i in range(len(ds)):
    for j in range(i+1, len(ds)):
        if ds[i] + ds[j] == target:
            print("Cặp:", ds[i], ds[j])
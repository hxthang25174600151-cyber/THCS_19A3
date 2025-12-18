chuoi = input("Nhập danh sách số nguyên: ")
k = int(input("Nhập số vị trí dịch chuyển: "))

ds = []
so = ""
for i in chuoi + " ":
    if i != " ":
        so += i
    else:
        if so != "":
            ds.append(int(so))
            so = ""

n = len(ds)
k = k % n   # tránh k quá lớn

ket_qua = [0]*n
for i in range(n):
    new_index = (i + k) % n
    ket_qua[new_index] = ds[i]

print("Danh sách sau khi dịch chuyển:", ket_qua)
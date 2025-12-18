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

ket_qua = []
for x in ds:
    co_trung = False
    for y in ket_qua:
        if x == y:
            co_trung = True
            break
    if not co_trung:
        ket_qua.append(x)

print("Danh sách sau khi loại bỏ trùng lặp:", ket_qua)
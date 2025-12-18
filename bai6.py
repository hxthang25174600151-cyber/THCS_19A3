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

tong_chan = 0
tong_le = 0
for x in ds:
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x

print("Tổng số chẵn:", tong_chan)
print("Tổng số lẻ:", tong_le)
chuoi = input("Nhập tuple số nguyên: ")

ds = []
so = ""
for i in chuoi + " ":
    if i != " ":
        so += i
    else:
        if so != "":
            ds.append(int(so))
            so = ""

tuple_chan = ()
tuple_le = ()
tong_chan = 0
tong_le = 0

for x in ds:
    if x % 2 == 0:
        tuple_chan += (x,)
        tong_chan += x
    else:
        tuple_le += (x,)
        tong_le += x

print("Tuple chẵn:", tuple_chan, "Tổng:", tong_chan)
print("Tuple lẻ:", tuple_le, "Tổng:", tong_le)
chuoi = input("nhập chuỗi: ")
n = int(input("Nhập n: "))

tu = ""
for i in chuoi + " ":
    if i != " ":
        tu += i
    else:
        if len(tu) > n:
            print(tu)
        tu = ""

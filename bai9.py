n = int(input("Nhập kích thước ma trận vuông: "))

mat = []
for i in range(n):
    dong = []
    chuoi = input("Nhập hàng thứ " + str(i+1) + ": ")
    so = ""
    for j in chuoi + " ":
        if j != " ":
            so += j
        else:
            if so != "":
                dong.append(int(so))
                so = ""
    mat.append(dong)

tong = 0
for i in range(n):
    tong += mat[i][n-1-i]

print("Tổng đường chéo phụ:", tong)
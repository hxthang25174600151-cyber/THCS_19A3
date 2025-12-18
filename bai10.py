m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

mat = []
for i in range(m):
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

max_sum = -999999999
row_index = -1

for i in range(m):
    tong = 0
    for j in range(n):
        tong += mat[i][j]
    if tong > max_sum:
        max_sum = tong
        row_index = i

print("Hàng có tổng lớn nhất là hàng", row_index+1, "với tổng =", max_sum)
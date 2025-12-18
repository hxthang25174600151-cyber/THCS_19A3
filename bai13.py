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

don_vi = True
for i in range(n):
    for j in range(n):
        if i == j and mat[i][j] != 1:
            don_vi = False
        elif i != j and mat[i][j] != 0:
            don_vi = False

if don_vi:
    print("Ma trận đơn vị")
else:
    print("Không phải ma trận đơn vị")
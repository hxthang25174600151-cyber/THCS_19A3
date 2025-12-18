m = int(input("Nhập số hàng ma trận A: "))
n = int(input("Nhập số cột ma trận A: "))
p = int(input("Nhập số cột ma trận B: "))

A = []
for i in range(m):
    dong = []
    chuoi = input("Nhập hàng A[" + str(i+1) + "]: ")
    so = ""
    for j in chuoi + " ":
        if j != " ":
            so += j
        else:
            if so != "":
                dong.append(int(so))
                so = ""
    A.append(dong)

B = []
for i in range(n):
    dong = []
    chuoi = input("Nhập hàng B[" + str(i+1) + "]: ")
    so = ""
    for j in chuoi + " ":
        if j != " ":
            so += j
        else:
            if so != "":
                dong.append(int(so))
                so = ""
    B.append(dong)

# Nhân ma trận
C = []
for i in range(m):
    dong = []
    for j in range(p):
        tong = 0
        for k in range(n):
            tong += A[i][k] * B[k][j]
        dong.append(tong)
    C.append(dong)

print("Kết quả nhân ma trận:")
for dong in C:
    print(dong)
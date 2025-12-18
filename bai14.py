chuoiA = input("Nhập tập A: ")
chuoiB = input("Nhập tập B: ")

A, B = [], []
so = ""
for i in chuoiA + " ":
    if i != " ":
        so += i
    else:
        if so != "":
            A.append(int(so))
            so = ""
so = ""
for i in chuoiB + " ":
    if i != " ":
        so += i
    else:
        if so != "":
            B.append(int(so))
            so = ""

# Hợp
hop = []
for x in A + B:
    co = False
    for y in hop:
        if x == y:
            co = True
            break
    if not co:
        hop.append(x)

# Giao
giao = []
for x in A:
    for y in B:
        if x == y:
            co = False
            for z in giao:
                if x == z:
                    co = True
                    break
            if not co:
                giao.append(x)

# Hiệu A - B
hieu_A_B = []
for x in A:
    co = False
    for y in B:
        if x == y:
            co = True
            break
    if not co:
        hieu_A_B.append(x)

# Hiệu B - A
hieu_B_A = []
for x in B:
    co = False
    for y in A:
        if x == y:
            co = True
            break
    if not co:
        hieu_B_A.append(x)

print("Hợp:", hop)
print("Giao:", giao)
print("A - B:", hieu_A_B)
print("B - A:", hieu_B_A)
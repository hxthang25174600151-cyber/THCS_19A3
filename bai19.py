n = int(input("Nhập số lượng sinh viên: "))

d = {}
for i in range(n):
    ten = input("Nhập tên sinh viên: ")
    diem = input("Nhập điểm: ")
    d[ten] = diem

nhom = {}
for ten in d:
    diem = d[ten]
    co = False
    for key in nhom:
        if key == diem:
            nhom[key].append(ten)
            co = True
            break
    if not co:
        nhom[diem] = [ten]

print("Nhóm sinh viên theo điểm:")
for diem in nhom:
    print(diem, ":", nhom[diem])
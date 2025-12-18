n = int(input("Nhập số lượng phần tử trong dictionary: "))

d = {}
for i in range(n):
    key = input("Nhập key: ")
    value = int(input("Nhập value: "))
    d[key] = value

ket_qua = {}
for key in d:
    if d[key] > 50:
        ket_qua[key] = d[key]

print("Các cặp key-value thỏa mãn điều kiện (value > 50):")
for key in ket_qua:
    print(key, ":", ket_qua[key])
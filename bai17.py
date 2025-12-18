n = int(input("Nhập số lượng phần tử trong dictionary: "))

d = {}
for i in range(n):
    key = input("Nhập key: ")
    value = int(input("Nhập value: "))
    d[key] = value

max_value = -999999999
max_key = None

for key in d:
    if d[key] > max_value:
        max_value = d[key]
        max_key = key

print("Key có giá trị lớn nhất là:", max_key, "với giá trị =", max_value)
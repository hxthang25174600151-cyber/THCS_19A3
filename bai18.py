n = int(input("Nhập số lượng phần tử trong dictionary: "))

d = {}
for i in range(n):
    key = input("Nhập key: ")
    value = input("Nhập value: ")
    d[key] = value

dao_nguoc = {}
for key in d:
    dao_nguoc[d[key]] = key

print("Dictionary sau khi đảo ngược:")
for key in dao_nguoc:
    print(key, ":", dao_nguoc[key])
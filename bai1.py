chuoi = input("Nhập vào 1 chuỗi: ")


chu,so,dac_biet = 0,0,0
for i in chuoi:
    if('a' <= i <= 'z') or ('A' <= i <= 'Z'):
      chu += 1
    elif '0' <= i <= '9':
       so += 1
    else:
       dac_biet += 1
print("Chữ cái:", chu)
print("Chữ số:", so)
print("Ký tự đặc biệt:", dac_biet)
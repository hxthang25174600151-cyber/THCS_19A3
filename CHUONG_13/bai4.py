
id_can_sua=input("Nhap ID: ")
gia_moi=input("Gia moi: ")
with open("san_pham.txt","r") as f:
    lines=f.readlines()
with open("san_pham.txt","w") as f:
    for line in lines:
        if line.startswith(id_can_sua+","):
            p=line.strip().split(",")
            f.write(f"{p[0]},{p[1]},{gia_moi}\n")
        else:
            f.write(line)

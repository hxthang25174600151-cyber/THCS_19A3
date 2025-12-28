
import csv
with open("nhan_vien.csv","w",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=["ID","Ten","Luong"])
    writer.writeheader()
    writer.writerow({"ID":1,"Ten":"An","Luong":60000})
    writer.writerow({"ID":2,"Ten":"Binh","Luong":40000})
with open("nhan_vien.csv","r") as f:
    reader=csv.DictReader(f)
    for r in reader:
        if int(r["Luong"])>50000:
            print(r)

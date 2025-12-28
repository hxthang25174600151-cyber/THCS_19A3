
with open("nguon.bin","rb") as src, open("dich.bin","wb") as dst:
    while True:
        data=src.read(1024)
        if not data: break
        dst.write(data)

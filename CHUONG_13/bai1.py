
with open("vanban.txt","w",encoding="utf-8") as f:
    f.write("Python la ngon ngu lap trinh manh me")
with open("vanban.txt","r",encoding="utf-8") as f:
    print(len(f.read().split()))

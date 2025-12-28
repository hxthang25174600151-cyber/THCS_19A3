
with open("vanban.txt","r",encoding="utf-8") as f:
    words=f.read().split()
tan_suat={}
for w in words:
    tan_suat[w]=tan_suat.get(w,0)+1
print(tan_suat)

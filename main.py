s = 0
i = 0
a = "mis temir olmos taqa mis"
c = "mis"

toshlar = a.split(" ")
olmoslar = c.split(" ")
print(toshlar)
print(olmoslar)
for i in range(len(olmoslar)):
    s += toshlar.count(olmoslar[i])

print(s)
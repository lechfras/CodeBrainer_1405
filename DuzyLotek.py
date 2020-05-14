import random

ileliczb=int(input("Podaj ilosc typowanych liczb: "))
maksliczba=int(input("Podaj maksymalna losowawna liczbe: "))
#print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))

liczby=[]
i=0
while (i < ileliczb):
    liczba=random.randint(1,maksliczba)

    if liczby.count(liczba)==0:
        liczby.append(liczba)
        i=i+1

print("Wylosowane liczby:", liczby)

print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))
typy=set()
i=0
while i < ileliczb:
    typ=input("podaj liczbe %s: " % (i+1))
    if typ not in typy:
        typy.add(typ)
        i=i+1

trafione = set(liczby) & typy
if trafione:
    print("\nilos trafien: %s" %len(trafione))
    print("trafione liczby: ", trafione)
else:
    print("Brak trafien")
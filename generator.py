liste = ["admin","login","panel"]
liste1 = []
for i in liste:
    asi = i + "2024"
    liste1.append(asi)

for b in liste:
    osi = "2024" + b
    liste1.append(osi)

for c in liste:
    aga = "2025" + c
    liste1.append(aga)

for s in liste:
    oho = s + "2025"
    liste1.append(oho)

for op in liste:
    asc = "2026"+op
    csa = op + "2026"
    liste1.append(asc)
    liste1.append(csa)
    

lisi = liste1.copy()

for l in lisi:
    p = l + "!"
    liste1.append(p)

for sayi,kelime in enumerate(liste1):
    print(sayi,"-", kelime)
    

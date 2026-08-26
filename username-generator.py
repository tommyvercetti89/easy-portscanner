kelimeler = ["admin","login","panel"]
yillar = [str(yil) for yil in range(2005,2026)]
semboller = ["@","!"]
liste = []

for kelime in kelimeler:
    for yil in yillar:
        for sembol in semboller:
            liste.append(f"{kelime}{yil}")
            liste.append(f"{yil}{kelime}")
            liste.append(f"{kelime}{yil}{sembol}")
            liste.append(f"{sembol}{kelime}{yil}")
            liste.append(f"{kelime}{sembol}{yil}")
            liste.append(f"{yil}{kelime}{sembol}")


with open(r"C:\Users\TOSHIBA\Desktop\list.txt", "w",encoding="utf-8") as dosya:
    dosya.write("\n".join(liste)+ "\n")
    
for i,b in enumerate(liste):
    print(i,"-",b)
            

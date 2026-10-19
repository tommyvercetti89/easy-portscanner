dosya = input("DOSYA YOLU: ")

dosya = dosya.strip('"')

with open(dosya,"r",encoding="utf8") as file:
   tum = []
   for satir in file:
       temiz = satir.strip()
       if temiz != "":
           tum.append(temiz)
       
benzersiz = set(tum)
       
print(f"TÜM IP ADRESLERİ --> {len(tum)}")
print(f"BENZERSİZ IP ADRESLERİ --> {len(benzersiz)}")
print(f"TEKRAR EDEN IP ADRESLERİ --> {len(tum)-len(benzersiz)}")  

gorulen = set()
kopya = set()
    
for ip in tum:
    if ip in gorulen:
        kopya.add(ip)
    else:    
        gorulen.add(ip)
          
for k in kopya:
    print("-->",k)              
    
if kopya:
    girdi = input("TEKRAR EDEN IP ADRESLERİ SİLİNSİN Mİ? [E/H]: ")
   

    if girdi.lower() =="e":
        with open(dosya,"w",encoding="utf8") as d:
            for ip in benzersiz:
                d.write(str(ip) + "\n")
            print("- ***DOSYA KAYDEDİLDİ***") 
           
    if girdi.lower() =="h":
        print("SCRİPT SONA ERDİ!") 
          
else:
    print("DOSYA TEMİZ, TEKRAR YOK!")     
    
input("ÇIKMAK İÇİN ENTER")    

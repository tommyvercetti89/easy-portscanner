import random

while True:
    
    print("*"*10,"IP ADRES OLUŞTURUCU", "*"*10)
    
    try:
        
        adet = int(input("KAÇ ADET IP ADRESİ İSTERSİN?: "))
        
        if adet == 0:
            print("ÇIKILIYOR...")
            break
            
        if adet < 0:
            print("Sayı 0'dan küçük olamaz!")
            continue
            
        ip_list = []
        
        for _ in range(adet):
            ip = ".".join(str(random.randint(0,255)) for _ in range(4))
            ip_list.append(ip)
            print(ip)
            
        girdi = input("BİR .TXT DOSYASINA KAYDET?[E,H]: ")
        
        if girdi.lower() == "e":
            with open("list.txt","a") as file:
               for ip in ip_list:
                   file.write(str(ip) + "\n")
                   
        if girdi.lower() == "h":
            continue
            
    except ValueError as e:
        print("HATA!!! --> ",e)
               

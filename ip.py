import random

while True:
    
    print("*"*10,"IP ADRES OLUŞTURUCU", "*"*10)
    
    try:
        
        adet = int(input("KAÇ ADET IP ADRESİ İSTERSİN?: "))
        
        if adet == 0:
            print("ÇIKILIYOR...")
            break
            
        if adet < 0:
            print("SAYI 0'DAN KÜÇÜK OLAMAZ!")
            continue
            
        for _ in range(adet):
            ip = ".".join(str(random.randint(0,255))for _ in range(4))
            print(ip)
    
    except ValueError as e:
        print("HATA!!!",e)
               

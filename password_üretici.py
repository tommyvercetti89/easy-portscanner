import string, secrets

havuz = string.ascii_letters + string.digits + string.punctuation

while True:
    try:
        
        sifre = ""
        girdi = int(input("KAÇ BASAMAKLI OLSUN ŞİFRE?(ÇIKMAK İÇİN '0' YAZ): "))
    
        if girdi == 0:
            print("ŞİFRE ÜRETİCİ KAPANDI..")
            break
        elif girdi < 0:
            print("ŞİFRE EKSİ BASAMAKLI OLAMAZ!")
            continue
         
        for i in range(girdi):
            sifre += secrets.choice(havuz)
        print(sifre) 
          
    except ValueError as hata:
        print("Bir sayı gir basamaklar harf olamaz!")
        continue
        

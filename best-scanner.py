import socket as sc
import time
import random

ipa = input("\nBen EasyScan! TARAMAM İÇİN BİR IP ADRESİ VEYA ALANADI VERİR MİSİN?: ")
bas = int(input("Başlangıç portu: "))
son = int(input("Bitiş portu: "))

print("*"*50)
print("TARAMAYA BAŞLADIM: ", ipa)
print("*"*50)

for port in range(bas,son +1):
    try:
        s = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
        s.settimeout(0.6)
        sonuc = s.connect_ex((ipa,port))

        if sonuc == 0:
            print("[+] AÇIK PORT",port)

            banner = s.recv(1024).decode().strip() 
            print(f"[!] PORT {port} AFİŞİ: {banner}")

        else:
            print("[-] Kapalı","-",port)

        s.close()
        time.sleep(random.randint(1,4))


    except Exception as e:
        print("HATA",e)

print("*"*50)
print("TARAMAYA BİTTİ: ", ipa)
print("*"*50)

input("ENTER - Çıkış")        

        

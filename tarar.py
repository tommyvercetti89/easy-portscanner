import time
import random
import socket as s


ipa = "192.168.1.1"
ports = [22,43,53,80,443,512]
print("*"*30,"Taranıyor: ",ipa,"-"*30)
for port in ports:
    try:
        soket = s.socket(s.AF_INET,s.SOCK_STREAM)
        soket.settimeout(0.29)
        sonuc = soket.connect_ex((ipa,port))

        if sonuc == 0:
            print("AÇIK: ",port)

            banner = soket.recv(1025).decode().strip()
            print("Banner Grabbing: ",banner)
        else:
            print("KAPALI: -",port)

        soket.close()

    except Exception as a:
         print("Hata: ", a)


print("*"*30,"Tarandı: ",ipa,"-"*30)
input("Çıkmak için Enter'a bas!: ")
         

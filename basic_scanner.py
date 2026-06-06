import socket as sc
import  sys

#IP Adresi ve taranacak portlar
IP_ADDR = "192.168.1.1"
ports = [22,53,80,443]


print("-"*30,"Taramaya başladım :",IP_ADDR, "-"*30)

for port in ports:
    try:
        s = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
        s.settimeout(1)
        cikti = s.connect_ex((IP_ADDR,port))

        if cikti == 0:
            print(f"NO'lu port açık :", port)
        else:
            print(f"NO'lu port kapalı :", port)

        s.close()

    except Exception as e:
          print("HATA OLUŞTU :", e)


input("Çıkmak için Enter'a basın")          

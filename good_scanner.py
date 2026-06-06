import socket as sc

#Kullanıcı girdisi alma ve bunu int'e dönüştürme
girdi_ip = input("Ben port tarayıcı bot. Taramam için bir IP adresi gir: ")
ports = input("Hangi portları taramamı istersin? (Başlangıç): ")
ports2 = input("Son portu da gir bakalım (Bitiş): ")
sayi_port = int(ports)
sayi_port2 = int(ports2)

print("-"*20,"Tarama başlıyor :",girdi_ip,"-"*20)
      #Tarama işlemi              
for port in range(sayi_port,sayi_port2 + 1):
    try:
        s = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
        s.settimeout(1)
        cikti = s.connect_ex((girdi_ip,port))
            
        if cikti == 0:
            print(f"Buldumm port {port} AÇIK!")
        else:
            print(f"Bu {port} nolu port KAPALI!")
        s.close()
    except Exception as e:
         print(f"Hata :", e)

input("Çıkmak için Enter'a basın!")

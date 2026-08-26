import socket as sc
import sys

ipa = sys.argv[1]
ports = sys.argv[2]
baport,biport = ports.split("-")
baslangic = int(baport)
bitis = int(biport)

print("SCANNING IP >>",ipa)

def tarama(ipa,baslangic,bitis):

    for port in range( baslangic, bitis + 1):
        try:
            s = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
            s.settimeout(0.1)
            sonuc = s.connect_ex((ipa,port))
            if sonuc == 0:
                print(f"[+] PORT >> {port} is OPEN!")
            s.close()
        except Exception as e:
            print("ERROR",e)
    
tarama(ipa,baslangic,bitis)

print("IP SCANNED >> ",ipa)
import socket as s
import requests as req

print("*"*50)
print("Port Scanner")
print("*"*50)

ipa = input("IP ADDRESS: ")
giri = int(input("START PORT: "))
endp = int(input("END PORT: "))
print("*"*20,"SCANNING: ",ipa,"*"*20)

for port in range(giri, endp + 1):
    try:
        soc = s.socket(s.AF_INET6,s.SOCK_STREAM )
        soc.settimeout(1)
        sonuc = soc.connect_ex((ipa,port))
        
        if sonuc == 0:
            try:
                banner = soc.recv(1024).decode().strip()
                print("OPEN PORT: ", port, ", BANNER: ",banner)
            except Exception:
                banner = "SOCKET COULDN'T GET!(NO RESPONSE)"
                print("OPEN PORT: ", port, ", BANNER: ", banner)

            if port == 80:
                try:
                    if ":" in ipa:
                        url = f"http://[{ipa}]"
                    else:
                        url = f"http://{ipa}"

                    ban80 = req.get(url, timeout = 3)
                    print("OPEN PORT: ",port, ", BANNER: ", ban80.headers)   
                except Exception as req_err:
                    print("OPEN PORT: ", port, ", BANNER: ",req_err)

        soc.close()                       
    except Exception as e:
        print("ERR:", e)    

print("SCAN COMPLETED: ", ipa)    
input("PRESS ENTER TO QUIT!")

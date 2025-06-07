#Made while learning requests library
import requests
import time
print('IP LOOKUP TOOL.')
retrieveurl = 'https://api.ipify.org?format=json'

def printmenu():
    var = '''
            ._____________  .____    ________   ________   ____  __.____ _____________ 
            |   \______   \ |    |   \_____  \  \_____  \ |    |/ _|    |   \______   \
            |   ||     ___/ |    |    /   |   \  /   |   \|      < |    |   /|     ___/
            |   ||    |     |    |___/    |    \/    |    \    |  \|    |  / |    |    
            |___||____|     |_______ \_______  /\_______  /____|__ \______/  |____|    
                                    \/       \/         \/        \/                  
                                     
            [01] Self IP              [02] Lookup IP             [03] Exit           
                                     
                                     '''
    print(var)



def get_self_ip():
    response = requests.get(retrieveurl)
    print(response.text)

def get_others_ip():
    ip = input("Please enter the ip address you want to search: ")
    otherurl = (f'https://api.hackertarget.com/geoip/?q={ip}')
    response2 = requests.get(otherurl)
    print(response2.text)
    print(" ")
    print("--Detailed Information--")
    otherurl3 = f'https://ipapi.co/{ip}/json/'
    response3 = requests.get(otherurl3)
    print(response3.text)

is_running = True
while is_running:
    printmenu()
    inp = input("Select the option: ")
    if inp == '1':
        get_self_ip()
    elif inp == '2':
        get_others_ip()
    elif inp == '3':
        print('Closing Menu in 5 Seconds!')
        time.sleep(5)
        break





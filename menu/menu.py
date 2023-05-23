from colorama import Fore as color
import sys
from time import sleep

def banner():
    print(color.RED+"""
███████╗███╗   ███╗███████╗██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████╗██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
╚════██║██║╚██╔╝██║╚════██║██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║███████║██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                .-------------------.
                                | developer: ali9sr |
                                '-------------------'

    """)

def menu_res():
    try:
        print(color.RED+"[1] "+ color.LIGHTYELLOW_EX+"Sms-Bomber without TOR")
        sleep(0.1)
        
        print(color.RED+"[2] "+ color.LIGHTYELLOW_EX+"Sms-Bomber with TOR")
        sleep(0.1)
        
        print(color.RED+"[0] "+ color.LIGHTYELLOW_EX+"Exit")
        sleep(0.1)
    except:
        print(color.RED+"[-] Something Went Wrong....")
        sleep(1)
        sys.exit()
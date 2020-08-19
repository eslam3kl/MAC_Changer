# MAC_Changer Tool 
This tool will help you to change your mac address of specific Interface if you perform any pentesting work and need to change it. 

**Mac_Changer will take 2 arguments**
1. The new MAC address 
2. The interface in which you want to change it (eth0, en0, etc.. ) 

**Ex** 

`python mac_changer.py -i eth0 -m 00:11:22:33:44:55`


**Notes** 

[+] Check that you have entered the correct interface 

[+] Check that the new mac address is following mac addresses query 

**Requirments**
Python 2 or 3 

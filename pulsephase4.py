#phase 4 expand the code to check ip address on the network. 

#import subprocess libaray to talk with the command line. 
import subprocess
#import date and time to add a time stamp
import datetime as dt
#importing time so the loop doesn't run every second of the day. 
import time
#importing ipaddress module to scan the ips on the net. 
import ipaddress
#creating a var to hope the ip_network
ip_test = ipaddress.ip_network("192.168.1.0/24")



multiple_target_ip = [""]

for ips in ip_test.hosts():
    ip_strings = str(ips)
    print(ip_strings)
    multiple_target_ip.append(ip_strings)
    
print(multiple_target_ip)

while True:
    #Try and except for ending the program 
    try:
        #creating time stamp
        pulse_time = dt.datetime.now()
        #interating over the dictionary. 
        for ip in multiple_target_ip:   
            #creating a ping command to test connectivity to the target ip address.
            ping_cmd = ['ping','-c','1',ip]

            #running the ping command using subprocess module and capturing the output.
            results = subprocess.run(ping_cmd, stdout= subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
            
            #check the return code to see if its 0, if 0 it is successful
            if results.returncode == 0:
                print(f"{pulse_time}: Ping to {ip} successful")
            else:
                    print(f"Ping to {ip} failed.")

        #add sleep so it doesn't run over and over again. 
        time.sleep(30) 
    except KeyboardInterrupt:
        print(" Stopping Network Pulse...")   
        exit()   
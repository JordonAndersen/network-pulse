#phase 5 have the code speed up so it doesn't take 5 minutes to run. plus a few other fun things. 

#import subprocess libaray to talk with the command line. 
import subprocess
#import date and time to add a time stamp
import datetime as dt
#importing time so the loop doesn't run every second of the day. 
import time
#importing ipaddress module to scan the ips on the net. 
import ipaddress
#creating a var to hold the ip_network
ip_address = ipaddress.ip_network("192.168.1.0/24")
#importing concurrent.futures for lauching parallel task
import concurrent.futures 




network_ips = []
discovered_hosts = {}
while True:
    try:
        for host_ips in ip_address.hosts():
            ip_strings = str(host_ips)   
            network_ips.append(ip_strings)

        def ping_host(ip):
        
            #creating a ping command to test connectivity to the target ip address. 
            ping_cmd = ['ping','-c','1', '-W', '1',ip]
            #running the ping command using subprocess module and capturing the output.
            results = subprocess.run(ping_cmd, stdout= subprocess.DEVNULL, stderr=subprocess.DEVNULL)         
            #check the return code to see if its 0, if 0 it is successful
            if results.returncode == 0:
                return (ip, "UP")
            else:
                return (ip, "DOWN")
            

        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            results = executor.map(ping_host, network_ips)

            
        for found_ips, status in results:
            if status == 'UP':
                discovered_hosts[found_ips] = "UP"

        print(discovered_hosts)
    except KeyboardInterrupt:
        print(" Stopping Network Pulse...")  
        exit()


# while True:
#     #Try and except for ending the program 
#     try:
#         #creating time stamp
#         pulse_time = dt.datetime.now()
#         #interating over the dictionary. 
#         for ip in network_ips:   
#             #creating a ping command to test connectivity to the target ip address.
#             ping_cmd = ['ping','-c','1',ip]

#             #running the ping command using subprocess module and capturing the output.
#             results = subprocess.run(ping_cmd, stdout= subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
            
#             #check the return code to see if its 0, if 0 it is successful
#             if results.returncode == 0:
#                 print(f"{pulse_time}: Ping to {ip} successful")
#             else:
#                     print(f"Ping to {ip} failed.")

#         #add sleep so it doesn't run over and over again. 
#         time.sleep(30) 
#     except KeyboardInterrupt:
#         print(" Stopping Network Pulse...")   
#         exit()   
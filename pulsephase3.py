#phase 3 expand the code so it automatically checks ip address. 

#import subprocess libaray to talk with the command line. 
import subprocess
#import date and time to add a time stamp
import datetime as dt
#importing time so the loop doesn't run every second of the day. 
import time



#phase 1 we used a var to hold one static IP address (target_ip = '8.8.8.8'). Here we will use a dictionary to hold multiple IP's (the values) and give the IP a name (the keys). For learning purposes I will be using Google, CloudFlare, and Quad9 

multiple_target_ip = {"Google" : "8.8.8.8", "Cloudflare" : "1.1.1.1", "Quad9" : "9.9.9.9" }

while True:
    #Try and except for ending the program 
    try:
        #creating time stamp
        pulse_time = dt.datetime.now()
        #interating over the dictionary. 
        for name, ip in multiple_target_ip.items():   
            #creating a ping command to test connectivity to the target ip address.
            ping_cmd = ['ping','-c','1',ip]

            #running the ping command using subprocess module and capturing the output.
            results = subprocess.run(ping_cmd, stdout= subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
            
            #check the return code to see if its 0, if 0 it is successful
            if results.returncode == 0:
                print(f"{pulse_time}: Ping to {name}, {ip} successful")
            else:
                    print(f"Ping to {name}, {ip} failed.")

        #add sleep so it doesn't run over and over again. 
        time.sleep(30) 
    except KeyboardInterrupt:
        print(" Stopping Network Pulse...")   
        exit()   
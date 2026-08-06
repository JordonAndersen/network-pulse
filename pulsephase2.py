#phase 2 is to expand to multiple devices. 

#import subprocess libaray to talk with the command line. 
import subprocess
#import date and time to add a time stamp
import datetime as dt

#creating time stamp
pulse_time = dt.datetime.now()

#phase 1 we used a var to hold one static IP address (target_ip = '8.8.8.8'). Here we will use a dictionary to hold multiple IP's (the values) and give the IP a name (the keys). For learning purposes I will be using Google, CloudFlare, and Quad9 

multiple_target_ip = {"Google" : "8.8.8.8", "Cloudflare" : "1.1.1.1", "Quad9" : "9.9.9.9" }

#interating over the dictionary. 
for name, ip in multiple_target_ip.items():   

    # #creating a ping command to test connectivity to the target ip address.
    ping_cmd = ['ping','-c','1',ip]

    # #running the ping command using subprocess module and capturing the output.
    results = subprocess.run(ping_cmd, stdout= subprocess.DEVNULL, stderr=subprocess.DEVNULL)


    # #seeing what the results are printed and args bing passed. Used for debugging as well during learning. No need to run everytime. 
    # print(name, results)


    #check the return code to see if its 0, if 0 it is successful
    if results.returncode == 0:
        print(f"{pulse_time}: Ping to {name}, {ip} successful")
    else:
        print(f"Ping to {name}, {ip} failed.")

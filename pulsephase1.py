#phase 1 is to create a ping in python and have it return codes on a static ip address. 

#import subprocess libaray to talk with the command line. 
import subprocess

#setting var to  a static ip address to test.
target_ip = '8.8.8.8'

#creating a ping command to test connectivity to the target ip address.
ping_cmd = ['ping','-c','4',target_ip]

#running the ping command using subprocess module and capturing the output.
results = subprocess.run(ping_cmd, stdout= subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#seeing what the results are printed and args bing passed. Used for debugging as well during learning  No need to run everytime. 
# print(results)

#check the return code to see if its 0, if 0 it is successful
if results.returncode == 0:
    print(f"Ping to {target_ip} successful.")
else:
    print(f"Ping to {target_ip} failed.")





import csv
import concurrent.futures
from queue import Queue
from getpass import getpass
from netmiko import ConnectHandler

routers = ['10.10.1.1','10.10.1.2','10.10.1.3']
a = ''
cisco_command = ['show ip int brief','show version | inc uptime']
def ssh_session(router, output_q):
 try:
    # Place what you want each thread to do here, for example connect to SSH, run a command, get output
    output_dict = {}
    hostname = router
    router = {'device_type': 'cisco_ios', 'ip': router, 'username': 'username', 'password': 'password#', 'verbose': False, }
    ssh_session = ConnectHandler(**router)
	  
 except Exception as e:
    print (e)
	
 for cmd in cisco_command:
      output = ssh_session.send_command(cmd)
      output_dict[hostname] = output
      output_q.put(output_dict) 
	
output_q = Queue()
	
with concurrent.futures.ThreadPoolExecutor() as executor:
     results = [executor.submit(ssh_session,router,output_q) for router in routers]

 
while not output_q.empty():
   my_dict = output_q.get()
   for k, val in my_dict.items():
       print (k)
       print (val)
   

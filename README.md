# Netmiko_multithreading
Using threadpool executor, list comprehension and netmiko to SSH into Network devices 

# Threadpool Executor

with concurrent.futures.ThreadPoolExecutor() as executor:
     results = [executor.submit(ssh_session,router,output_q) for router in routers]7

I have used threadpool executor instead of traditional multithreading method. This helps to keep the code short and we don't need to worry about join() and start() multithreading methods.

# List Comprehension

[executor.submit(ssh_session,router,output_q) for router in routers]

I have used list comprehension instead of for loop. This prevents iteration over loop again and again. 

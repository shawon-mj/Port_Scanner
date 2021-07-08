#import modules
import sys
import socket
import time
import threading
from queue import Queue
import os
########################
#Time Set
time1 = time.time()
########################
#Auto Connect Close
socket.setdefaulttimeout(1)
lock = threading.Lock()
##################################
#User Guide Print
user_guide = 'Python3 PORT_SCAN.py Target_IP Starting_Port Ending_Port\n'
example = 'Example: Python3 PORT_SCAN.py 191.121.13.30 1 100'
###########################################################################
#Argument Check
if(len(sys.argv)!=4):
    print(user_guide)
    print(example)
    sys.exit()
############################################################################
#Target Input
try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
     print("Name Resulation Error!")
     sys.exit()
#############################################################################
#Input Start And End POrt
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
###########################################################################################################
#Printing Some Impormation
os.system("figlet Advance Port Scanner V 0 . 0 2")
print("\n\t\t\t\tContact With Owner")
Creator = " Name: Shakhawat Hosen Shawon\n"
git0 = "GitHub: https://www.github.com/shawon-mj\n"
facebook = "Facebook: www.facebook.com/shakhawat.shawon.3133\n"
ema = "Email: mdshawon29@yahoo.com"
print(Creator,git0,facebook,ema)
print("*"*80)
print("\t\t[+]Start Scanning Target: {}.".format(target))
tport = (end_port - start_port)+1
print("\t\t[+]Target Total {} Port.".format(tport))
print("*"*80)
time.sleep(3)
##############################################################################################################
def baners(target):
    return target.recv(1024)
#Scan Function
def scanning(port):
    connections = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    try:
        connect = connections.connect((target,port))
        with lock:
            try:
                banner = baners(connections)
                print("\n\t\t[+]Port {} Is Open : {}".format(port, (banner).decode().strip('\n')))
            except:
                print("\n\t\t[+]Port {} Is Open But Banner Not Found".format(port))
        connections.close()
    except:
        pass
#################################################################################################################
#Boosting Scan
q = Queue()
def threat():
    while True:
        get1 = q.get()
        scanning(get1)
        q.task_done()
for i in range(1000):
    th = threading.Thread(target = threat)
    th.daemon = True
    th.start()
for pt in range(start_port,end_port+1):
    q.put(pt)
q.join()
##################################################################################################################
#Excuted Time Taken
end_time = time.time()
print("\nTime Estemeted: " + str(end_time - time1) + " Sec\n")
#Complite



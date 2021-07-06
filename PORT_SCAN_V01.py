#import modules
import sys
import socket
import time
import threading
from queue import Queue
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
print("*"*80)
print("Start Scanning Target: {}.##########CREATED BY########################".format(target))
tport = (end_port - start_port)+1
print("Target Total {} Port.##########################SHAWON##########################".format(tport))
print("*"*80)
##############################################################################################################
#Scan Function
def scanning(port):
    connections = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    try:
        connect = connections.connect((target,port))
        with lock:
            print("Port {} Is Open".format(port))
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
print("Time Estemeted: " + str(end_time - time1) + " Sec\n")
#Complite



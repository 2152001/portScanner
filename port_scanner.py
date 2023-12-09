#!/bin/python3

import sys
import socket
from datetime import datetime as dt

if len(sys.argv)==2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of argument")
    print ("Syntax: python3 scanner.py")


#pretty banner 

print("-"*50)
print("Scanning port "+target)
print("Time Started "+str(dt.now()))
print("-"*50)


try:
    for port in range(0,200):
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target ,port))

        if result == 0:
            print(f"Port {port} is open")
        s.close() 

except KeyboardInterrupt:
    print("\nExisting program")
    sys.exit()
except socket.gaierror:
    print("Hostname couldn't be resolved")
except socket.error:
    print("could not connect to server")
    sys.exit()
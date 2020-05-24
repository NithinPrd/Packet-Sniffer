#Testing socket creation in python 3

import socket
import sys
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
if(s):
    print("Socket successfully created.")
else:
    print("Unable to create socket.")
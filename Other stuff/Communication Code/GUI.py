#Packet sniffer in python
#For Linux - Sniffs all incoming and outgoing packets

import socket, sys
from struct import *

#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
  b = '%.2x:%.2x:%.2x:%.2x:%.2x:%.2x' % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
  return b

#create a AF_PACKET type raw socket (thats basically packet level)
#define ETH_P_ALL    0x0003          /* Every packet (be careful!!!) */
try:
	s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
except socket.error , msg:
	print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

# receive a packet
def startIt():
    print 'Hello world'

    while True:
        print 'Code is inside while loop'

        packet = s.recvfrom(65565)
        
        #packet string from tuple
        packet = packet[0]
        
        #parse ethernet header
        eth_length = 14
        
        eth_header = packet[:eth_length]
        eth = unpack('!6s6sH' , eth_header)
        eth_protocol = socket.ntohs(eth[2])
        T.insert(tk.END, '\n\nDestination MAC : ' + eth_addr(packet[0:6]) + '\n\n Source MAC : ' + eth_addr(packet[6:12]) 
        + '\n\n Protocol : ' + str(eth_protocol))

        #Parse IP packets, IP Protocol number = 8
        if eth_protocol == 8 :
            #Parse IP header
            #take first 20 characters for the ip header
            ip_header = packet[eth_length:20+eth_length]
            
            #now unpack them
            iph = unpack('!BBHHHBBH4s4s' , ip_header)

            version_ihl = iph[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF

            iph_length = ihl * 4

            ttl = iph[5]
            protocol = iph[6]
            s_addr = socket.inet_ntoa(iph[8]);
            d_addr = socket.inet_ntoa(iph[9]);

            T.insert(tk.END, '\n Version : ' + str(version) + '\n IP Header Length : ' + str(ihl) + '\n TTL : ' + str(ttl) 
            + '\n Protocol : ' + str(protocol) + '\n Source Address : ' + str(s_addr) + '\n Destination Address : ' + str(d_addr))

            #TCP protocol
            if protocol == 6 :
                t = iph_length + eth_length
                tcp_header = packet[t:t+20]

                #now unpack them
                tcph = unpack('!HHLLBBHHH' , tcp_header)
                
                source_port = tcph[0]
                dest_port = tcph[1]
                sequence = tcph[2]
                acknowledgement = tcph[3]
                doff_reserved = tcph[4]
                tcph_length = doff_reserved >> 4
                
                T.insert(tk.END, '\n Source Port : ' + str(source_port) + '\n Dest Port : ' + str(dest_port) + '\n Sequence Number : ' 
                + str(sequence) + '\n Acknowledgement : ' + str(acknowledgement) + '\n TCP header length : ' + str(tcph_length))
                
                h_size = eth_length + iph_length + tcph_length * 4
                data_size = len(packet) - h_size
                
                #get data from the packet
                data = packet[h_size:]
                
                #T.insert(tk.END, '\n\tData : ' + data)

            #ICMP Packets
            elif protocol == 1 :
                u = iph_length + eth_length
                icmph_length = 4
                icmp_header = packet[u:u+4]

                #now unpack them
                icmph = unpack('!BBH' , icmp_header)
                
                icmp_type = icmph[0]
                code = icmph[1]
                checksum = icmph[2]
                
                T.insert(tk.END, '\n Type : ' + str(icmp_type) + '\n Code : ' + str(code) + '\n Checksum : ' + str(checksum))
                
                h_size = eth_length + iph_length + icmph_length
                data_size = len(packet) - h_size
                
                #get data from the packet
                data = packet[h_size:]
                
                #T.insert(tk.END, '\n\tData : ' + data)

            #UDP packets
            elif protocol == 17 :
                u = iph_length + eth_length
                udph_length = 8
                udp_header = packet[u:u+8]

                #now unpack them
                udph = unpack('!HHHH' , udp_header)
                
                source_port = udph[0]
                dest_port = udph[1]
                length = udph[2]
                checksum = udph[3]
                
                #T.insert(tk.END, '\n Source Port : ' + str(source_port) + '\n Dest Port : ' + str(dest_port) + '\n Length : ' + str(length) + '\n Checksum : ' + str(checksum)
                
                h_size = eth_length + iph_length + udph_length
                data_size = len(packet) - h_size
                
                #get data from the packet
                data = packet[h_size:]
                
                #T.insert(tk.END, '\n\tData : ' + data)

            #some other IP packet like IGMP
            else :
                T.insert(tk.END, 'Protocol other than TCP/UDP/ICMP')
                
            T.insert(tk.END, '\n')


from struct import *

#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
  b = '%.2x:%.2x:%.2x:%.2x:%.2x:%.2x' % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
  return b

#create a AF_PACKET type raw socket (thats basically packet level)
#define ETH_P_ALL    0x0003          /* Every packet (be careful!!!) */
try:
	s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
except socket.error , msg:
	print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

# receive a packet
def startIt():
        print 'Hello world'

    #while True:
        print 'Code is inside while loop'

        packet = s.recvfrom(65565)
        
        #packet string from tuple
        packet = packet[0]
        
        #parse ethernet header
        eth_length = 14
        
        eth_header = packet[:eth_length]
        eth = unpack('!6s6sH' , eth_header)
        eth_protocol = socket.ntohs(eth[2])
        #T.insert(tk.END, '\n\nDestination MAC : ' + eth_addr(packet[0:6]) + '\n\n Source MAC : ' + eth_addr(packet[6:12]) + '\n\n Protocol : ' + str(eth_protocol)

        #Parse IP packets, IP Protocol number = 8
        if eth_protocol == 8 :
            #Parse IP header
            #take first 20 characters for the ip header
            ip_header = packet[eth_length:20+eth_length]
            
            #now unpack them
            iph = unpack('!BBHHHBBH4s4s' , ip_header)

            version_ihl = iph[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF

            iph_length = ihl * 4

            ttl = iph[5]
            protocol = iph[6]
            s_addr = socket.inet_ntoa(iph[8]);
            d_addr = socket.inet_ntoa(iph[9]);

            T.insert(tk.END, '\n Version : ' + str(version) + '\n IP Header Length : ' + str(ihl) + '\n TTL : ' + str(ttl) + '\n Protocol : ' + str(protocol)
             + '\n Source Address : ' + str(s_addr) + '\n Destination Address : ' + str(d_addr))

            #TCP protocol
            if protocol == 6 :
                t = iph_length + eth_length
                tcp_header = packet[t:t+20]

                #now unpack them
                tcph = unpack('!HHLLBBHHH' , tcp_header)
                
                source_port = tcph[0]
                dest_port = tcph[1]
                sequence = tcph[2]
                acknowledgement = tcph[3]
                doff_reserved = tcph[4]
                tcph_length = doff_reserved >> 4
                
                T.insert(tk.END, '\n Source Port : ' + str(source_port) + '\n Dest Port : ' + str(dest_port) 
                + '\n Sequence Number : ' + str(sequence) + '\n Acknowledgement : ' + str(acknowledgement) + '\n TCP header length : ' + str(tcph_length))
                
                h_size = eth_length + iph_length + tcph_length * 4
                data_size = len(packet) - h_size
                
                #get data from the packet
                data = packet[h_size:]
                
                #T.insert(tk.END, '\n\tData : ' + data)

            #ICMP Packets
            elif protocol == 1 :
                u = iph_length + eth_length
                icmph_length = 4
                icmp_header = packet[u:u+4]

                #now unpack them
                icmph = unpack('!BBH' , icmp_header)
                
                icmp_type = icmph[0]
                code = icmph[1]
                checksum = icmph[2]
                
                T.insert(tk.END, '\n Type : ' + str(icmp_type) + '\n Code : ' + str(code) + '\n Checksum : ' + str(checksum))
                
                h_size = eth_length + iph_length + icmph_length
                data_size = len(packet) - h_size
                
                #get data from the packet
                data = packet[h_size:]
                
                #T.insert(tk.END, '\n\tData : ' + data)

            #UDP packets
            elif protocol == 17 :
                u = iph_length + eth_length
                udph_length = 8
                udp_header = packet[u:u+8]

                #now unpack them
                udph = unpack('!HHHH' , udp_header)
                
                source_port = udph[0]
                dest_port = udph[1]
                length = udph[2]
                checksum = udph[3]
                
                #T.insert(tk.END, '\n Source Port : ' + str(source_port) + '\n Dest Port : ' + str(dest_port) + '\n Length : ' + str(length) + '\n Checksum : ' + str(checksum)
                
                h_size = eth_length + iph_length + udph_length
                data_size = len(packet) - h_size
                
                #get data from the packet
                data = packet[h_size:]
                
                #T.insert(tk.END, '\n\tData : ' + data)

            #some other IP packet like IGMP
            else :
                T.insert(tk.END, 'Protocol other than TCP/UDP/ICMP')
                
            T.insert(tk.END, '\n')

from ctypes import *

def newLog():
    so_file = "./dlsniffer.so"
    res = CDLL(so_file)
    res.main()

import Tkinter as tk

m = tk.Tk()
m.geometry("700x500")
frame = tk.Frame(m)
frame.pack()

def startLog():
    T.insert(tk.END, "logged message")

m.title("Sample Packet Tracer")
button1 = tk.Button(frame, text='Start Intercept', command=startIt)
button1.pack(side = tk.LEFT)
T = tk.Text(m)
T.pack()

button2 = tk.Button(frame, text='Log Intercept', command=newLog)
button2.pack(side = tk.LEFT)
T.insert(tk.END, "Log Text:\n")
m.mainloop()
#!/usr/bin/env python3
import argparse
import socket
import struct
import time

from ethernet import *

messages = ['hi','hello','testing', 'joe','mutiny']

def main(target, interface):
    # Create a layer 2 raw socket
    with socket.socket(socket.AF_PACKET, socket.SOCK_RAW) as client_socket:
        # Bind an interface
        client_socket.bind((interface, 0))
        # Send a frame

        index = 0

        while index<5:
            
            client_socket.sendall(
                # Pack in network byte order

                struct.pack(f'!6s6sH{len(messages[index])}s',
                            eui48_to_bytes(target),             # Destination MAC address
                            get_hardware_address(interface),    # Source MAC address
                            ETH_P_802_EX1,                      # Ethernet type
                            messages[index].encode()))                     # Payload
            print('Sent!')
            index+=1
            time.sleep(1)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Client')
    parser.add_argument('target', type=str, help='target MAC address')
    parser.add_argument('interface', type=str, help='source interface name')
    args = parser.parse_args()
    main(args.target, args.interface)

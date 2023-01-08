#!/usr/bin/bash

'''
@function my_tcp
Build Your Own TCP
@target_host: target host
@target_port: target port
return response from TCP request
'''

import socket
import sys

target_host = 'https://www.google.com'
target_port = 80

def my_tcp(target_host: str,  target_port: int):
    """ function my_tcp"""
    target_host = target_host if target_host and isinstance(target_host, str) else str(target_host)
    target_host = target_port if target_port and isinstance(target_port, int) else int(target_port)
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(target_host, target_port)
    client.send(f"GET /HTTP/1.1\r\n HOST: google.com\r\n\r\n")

    response = client.recv(4096)

    print(response)

    return response


if __name__ == '__main__':
    li = sys.argv

    if len(li) != 3:
        print(f'Usage: `./byo-tcp address port` \n')
        sys.exit(1)
    else:
        _, target_port, target_host = li
        my_tcp(target_host, target_port)
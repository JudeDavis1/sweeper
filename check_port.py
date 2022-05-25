import socket

from colorama import Fore

import logger


PATH = 'online_ips.txt'
PORT = 80

def check_port():
    sock = socket.socket()
    sock.settimeout(1)

    with open(PATH, 'r') as f:
        ips = f.readlines()
        n_ips = len(ips)

        logger.INFO(f'Found {Fore.BLUE}{n_ips}{Fore.GREEN} ONLINE IPs so far...')

        for i in range(n_ips):
            ip = ips[i].strip('\n')
            if sock.connect_ex((ip, PORT)) == 0:
                print(ip)


def is_open(sock, host, port):
    return sock.connect_ex((host, port)) == 0

if __name__ == '__main__':
    check_port()

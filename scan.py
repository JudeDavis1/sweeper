import os
import sys
import ctypes
import socket

from colorama import Fore
from scapy.all import ICMP

# Local files
import utils
import logger

from check_port import is_open


def scan():
    utils.verify_os()
    if not utils.is_root():
        logger.CRITICAL('User MUST run as root!\n')
        sys.exit(1)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.settimeout(.01)

    f = open('online_ips.txt')
    contents = f.readlines()

    classes = contents[-1].strip('\n').split('.') if len(contents) else "0.0.0.0".split('.')
    f.close()
    f = open('online_ips.txt', 'a')

    try:
        logger.INFO('Scanning records for online servers...')
        for i in range(int(classes[0]), 255):
            for j in range(int(classes[1]), 255):
                for k in range(int(classes[2]), 255):
                    for l in range(int(classes[3]) + 1, 255):
                        ip = f'{i}.{j}.{k}.{l}'
                        
                        if is_online(sock, ip):
                            f.write(ip + '\n')
                            logger.INFO(f'Online - {Fore.BLUE}{ip}{Fore.RESET}')
    except KeyboardInterrupt:
        f.close()
        logger.INFO('\n\n[*] Saved IP addresses!\n')
    
    f.close()


def is_online(sock: socket.socket, ip: str) -> bool:
    try:
        sock.sendto(bytes(ICMP()), (ip, 0))
    except OSError:
        return False

    try:
        if sock.recvfrom(65565)[0] != None:
            return True
    except socket.timeout:
        return False
    return False


if __name__ == '__main__':
    scan()

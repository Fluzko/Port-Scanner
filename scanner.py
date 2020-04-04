#!/bin/python
import sys
import socket
from datetime import datetime


def helpScreen():
    print('-' * 50)
    print('Python port scanner')
    print('- Basic usage')
    print('    python3 scanner.py <ip> ')
    print('- Optional parameters')
    print('   -i initial port, >=1 if not provided starts at 1')
    print('   -f final port, <=65535 if not provided ends at 65535')
    print('-' * 50)


initport = 1
finalport = 65535

if len(sys.argv) == 2:
    if sys.argv[1] in ['-help', '--help', '-h', '--h']:
        helpScreen()
        sys.exit()
    try:
        target = socket.gethostbyname(sys.argv[1])
    except:
        print('Ip error')
        sys.exit()

if len(sys.argv) > 2:
    try:
        target = socket.gethostbyname(sys.argv[1])
    except:
        print('Ip error')
        sys.exit()
    if len(sys.argv) == 4 and sys.argv[2] in ['-i', '-f']:
        if sys.argv[2] == '-i':
            try:
                initport = int(sys.argv[3])
            except:
                print('Port type error')
                sys.exit()
        if sys.argv[2] == '-f':
            try:
                finalport = int(sys.argv[3])
            except:
                print('Port type error')
                sys.exit()
    if len(sys.argv) == 6 and sys.argv[2] in ['-i', '-f'] and sys.argv[4] in ['-i', '-f']:
        if sys.argv[2] == '-i':
            try:
                initport = int(sys.argv[3])
                finalport = int(sys.argv[5])
            except:
                print('Port type error')
                sys.exit()
        else:
            try:
                finalport = int(sys.argv[3])
                initport = int(sys.argv[5])
            except:
                print('Port type error')
                sys.exit()

if initport >= finalport:
    print('Initial port can\'t be higher than thefinal one')
    sys.exit()

print('-' * 50)
print('Scanning taget ' + target)
print('from: {}'.format(initport) + ' to: {}'.format(finalport))
initTime = datetime.now()
print('Time started: ' + str(initTime))
print('-' * 50)


for port in range(initport, finalport):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print('Port {} is open'.format(port))
        s.close()
    except KeyboardInterrupt:
        print('\nExiting program...')
        sys.exit()

    except socket.gaierror:
        print('Hostname could no be resolved')
        sys.exit()

    except socket.error:
        print('Could not connect to server')
        sys.exit()



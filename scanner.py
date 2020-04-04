#!/bin/python
import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Syntax error')
    print('python3 scanner.py <ip>')
    sys.exit()


print('-' * 50)
print('Scanning taget ' + target)
initTime = datetime.now()
print('Time started: ' + str(initTime))
print('-' * 50)


for port in range(1,65000):
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

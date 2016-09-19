#!/usr/bin/env python

from time import strftime, sleep

try:
    while True:
        print('\r{}'.format(strftime('%d.%m.%Y %H:%M:%S')), end = '')
        sleep(1)
except KeyboardInterrupt:
    print('\r')
    print('Exit!!!')

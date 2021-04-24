
"""
    Timer usage A small app that displays date
"""

import time
import os
import platform


def clear():
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')


while True:

    timer = time.localtime()
    year = timer[0]
    mount = timer[1]
    day = timer[2]
    hour = timer[3]
    minute = timer[4]
    second = timer[5]

    time.sleep(1)
    clear()

    print("""
        tarih: {}/{}/{}
        saat : {}:{}:{}
        """.format(day, mount, year, hour, minute, second))
        

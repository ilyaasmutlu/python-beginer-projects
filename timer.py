
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
    Timer = time.localtime()
    year = Timer[0]
    mount = Timer[1]
    day = Timer[2]
    hour = Timer[3]
    minute = Timer[4]
    second = Timer[5]

    time.sleep(1)
    clear()

    print("""
        date:{}/{}/{}
        clock:{}:{}:{}
    
    """.format(day,mount,year,hour,minute,second))




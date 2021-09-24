import os

import subprocess
import time


def dateChange(count):
    file = open('date.bat', 'w')
    p = 'date 9-' + str(count) + '-2021'
    print(p)
    file.write(p)
    file.close()


def runner(count):
    dateChange(count)
    os.system('cmd /c "start op"')
    print("done")


for i in range(1, 30):
    runner(i)


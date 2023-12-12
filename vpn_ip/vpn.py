#!/usr/bin/env python3

import os
from time import sleep
import random

codeList = ["TR","US","DE","NL","CH","GB"]

try:
    os.system("windscribe connect")
    while True:
        codeChoice = random.choice(codeList)
        sleep(random.randrange(120,300))
        print("#changing the IP Address...")
        os.system("windscribe connect " + codeChoice)

except:
    os.system("windscribe disconnect")
    print("ERROR occured")
    
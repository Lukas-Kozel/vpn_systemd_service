#!/usr/bin/env python3

import os
from time import sleep
import random
import subprocess

codeList = ["TR","US","DE","NL","CH","GB"]
log_file_path = "output.txt"


def ip_change_validation(code)-> bool:
    return True if code==0 else False

def write_to_file(filepath,stdout,stderr,returncode):
    with open('output.txt', 'w') as file:
        file.write("Standard Output:\n")
        file.write(stdout)   
        file.write("\nStandard Error:\n")
        file.write(stderr)
        file.write("\nReturn Code: ")
        file.write(str(returncode))

def main():
    try:
        os.system("windscribe connect")
        while True:
            codeChoice = random.choice(codeList)
            sleep(random.randrange(12,30))
            print("changing the IP Address...")
            command = ["windscribe", "connect", codeChoice]
            result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = result.communicate(60)
            write_to_file(log_file_path,stdout=stdout,stderr=stderr,returncode=result.returncode)
            ip_change_validation(result.returncode)
    except:
        os.system("windscribe disconnect")
        print("ERROR occured")


if __name__ == "__main__":
    main()
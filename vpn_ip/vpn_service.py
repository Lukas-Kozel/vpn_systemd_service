#!/usr/bin/env python3

import os
from time import sleep
import random
import subprocess
import requests   

codeList = ["TR","US","DE","NL","CH","GB"]
log_file_path = "output.txt"

def ip_change_validation(code)-> bool:
    return True if int(code)==0 else False

def get_public_ip():
    response = requests.get('https://api.ipify.org').text
    return response

def save_and_extract_expected_current_ip_address(stdout)-> str:
    public_ip =""
    for char in stdout[::-1]:
        if char:
            public_ip+=char
    public_ip = ''.join(reversed(public_ip))
    print(public_ip)
    #TODO there is issue with extracting the IP address, maybe just try to find substring in the stdout?
    with open('output.txt', 'w') as file:
        file.write(public_ip)
    return public_ip


def main():
    try:
        os.system("windscribe connect")
        while True:
            codeChoice = random.choice(codeList)
            sleep(random.randrange(12,30))
            command = ["windscribe", "connect", codeChoice]
            result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = result.communicate(10)
            #TODO merge all following methods together
            if ip_change_validation(result.returncode) and get_public_ip() == save_and_extract_expected_current_ip_address(stdout):
                print("change was succesful")
                
    except:
        #TODO add subprocess.Popen and wait for keyword "Disconneted" as the output from windscribe disconect command and if it do not occure within timeout then try to call the command again
        os.system("windscribe disconnect")
        print("ERROR occured")


if __name__ == "__main__":
    main()
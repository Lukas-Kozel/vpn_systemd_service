#!/usr/bin/env python3

import os
from time import sleep
import random
import subprocess
import requests   

codeList = ["TR","US","DE","NL","CH","GB"]
log_file_path = "output.txt"
current_ip_address = ""


def get_public_ip():
    response = requests.get('https://api.ipify.org').text
    return response


def ip_changed_validation(stdout,code)->bool:
    global current_ip_address
    current_address = get_public_ip()
    if stdout.find(current_address) != -1:
        current_ip_address = current_address
        save_ip_address(current_ip_address)
        return True if int(code)==0 else False
    else:
        return False
    
    
def save_ip_address(current_ip_address):
    with open('output.txt', 'a') as file:
        file.write(current_ip_address+"\n")


def main():
    try:
        os.system("windscribe connect")
        while True:
            codeChoice = random.choice(codeList)
            sleep(random.randrange(200,300))
            command = ["windscribe", "connect", codeChoice]
            result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = result.communicate(10)
            if ip_changed_validation(stdout=stdout,code=result.returncode):
                print("IP was changed successfully")
                print(f"Current IP address is: {current_ip_address}")
                
                
    except:
        print("ERROR occured")
        code = os.system("windscribe disconnect")
        print(f"Exit code:{code}")
        if code != 0:
            os.system("windscribe disconnect")


if __name__ == "__main__":
    main()
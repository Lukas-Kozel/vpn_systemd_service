import requests   
import time

def get_public_ip():
    response = requests.get('https://api.ipify.org').text
    return response

interval = 5  # Interval in seconds
while True:
    public_ip = get_public_ip()
    print(f'Public IP: {public_ip}')
    time.sleep(interval)
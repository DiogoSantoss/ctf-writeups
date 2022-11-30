import requests

URL = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22053/"

session = requests.session()

r = session.get(URL+"hello")
lines = r.text.split("<br>")

target = lines[0].split(" ")[-1][:-1]
current = lines[1].split(" ")[-1]

while current != target:
    r = session.get(URL+"more")
    lines = r.text.split("<br>")
    current = lines[2].split(" ")[-1]

r = session.get(URL+"finish")
flag = r.text.split(" ")[-1]
print(flag)

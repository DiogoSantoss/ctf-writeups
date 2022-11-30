import requests

URL = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22052"

session = requests.session()
session.get(URL)

min = 0
max = 100000

while True:
    number = (min+max)//2
    r = session.get(URL + "/number/" + str(number))

    if r.text.find("Higher!") != -1:
        min = number
    elif r.text.find("Lower!") != -1:
        max = number
    else:
        print(r.text)
        break
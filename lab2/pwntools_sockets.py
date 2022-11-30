from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22055

s = remote(SERVER, PORT)

s.recvuntil(b'get to ')
total = s.recvuntil(b'.')[:-1].decode()

s.recvuntil(b'CURRENT = ')
current = s.recvuntil(b'.')[:-1].decode()

while current != total:
    s.send(b'MORE\n')
    s.recvuntil(b'CURRENT = ')
    current = s.recvuntil(b'.')[:-1].decode()

s.send(b'FINISH\n')
s.recvuntil(b'GREAT JOB: ')
flag = s.recvuntil(b'\n')[:-1].decode()
print(flag)
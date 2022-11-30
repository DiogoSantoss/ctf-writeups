# Challenge `PwnTools Sockets` Writeup

- Vulnerability: 
  - brute-force attack
- Where:
  - `/more` endpoint
- Impact:
  - allows to find the server's guess by enumeration

## Analyzing the server

This challenge is similar to the [previous one](python_requests.md) but this time it uses sockets instead of HTTP requests.


## Exploit

First we connect to the server using the `pwntools` library.
```python
s = remote(SERVER, PORT)
```
Then we read the current value and the target value.
```python
s.recvuntil(b'get to ')
total = s.recvuntil(b'.')[:-1].decode()

s.recvuntil(b'CURRENT = ')
current = s.recvuntil(b'.')[:-1].decode()
```
If the current value isn't equal to the target value, we send a `MORE\n` message to the socket and repeat until we reach the target value.
```python
s.send(b'MORE\n')
s.recvuntil(b'CURRENT = ')
current = s.recvuntil(b'.')[:-1].decode()
```
Finally we send the `FINISH\n` message to the socket and read the flag.
```python
s.send(b'FINISH\n')
s.recvuntil(b'GREAT JOB: ')
flag = s.recvuntil(b'\n')[:-1].decode()
```

## Implementation

These code snippets and full implementation can be found [here](pwntools_sockets.py).

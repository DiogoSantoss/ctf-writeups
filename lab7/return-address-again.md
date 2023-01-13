# Challenge `Return Address Again` Writeup

- Vulnerability: 
  - Format strings
- Where:
  - printf function
- Impact:
  - allows to return to other functions

## Analyzing the server

The main function calls a function which reads the user input to a buffer.

## Exploit

By running `gdb` its possible to find the address of the `win` function. 
Using `info f` we can find the address where `eip` is stored.
Sending the following format string
```
"AAAA.%08x.%08x.%08x.%08x.%08x.%08x.%08x"
```
and verifying that the 7th register is filled with `41` (the value of `A`) tell us that we control the 7th register.
To call the `win` function we need to overwrite the `eip` value with the address of the `win` function.
However the address of the `eip` can change from machine to machine but the offset between the `buffer` and the `eip` is constant.
So we can locally compute the offset between the `buffer` and the `eip` using `gdb` and then remotely use formatted string to find the address of the `buffer` variable and then compute the address of the `eip` using the offset.
```
# (to get the buffer address)
payload = b'%08x' 
# (to write in eip)
payload =  p32(saved_eip+2) + b'%007$hhn'                        
payload += p32(saved_eip+3) + b'%010$hhn'                   
payload += p32(saved_eip+1) + b'%000120c' + b'%013$hhn'     
payload += p32(saved_eip+0) + b'%000094c' + b'%018$hhn'     
```
Revealing the flag `SSof{Returning_to_the_same_old_things}`

## Implementation

Full implementation can be found [here](return-address-again.py).

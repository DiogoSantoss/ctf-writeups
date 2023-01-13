# Challenge `Write Specific Value` Writeup

- Vulnerability: 
  - Format strings
- Where:
  - printf function
- Impact:
  - allows to write in arbitrary memory

## Analyzing the server

The main function reads the user input to a buffer then based on the target value it prints the flag or writes an error message.

## Exploit

By running `gdb` its possible to find the address of the `target` variable. 
Sending the following format string
```
"AAAA.%08x.%08x.%08x.%08x.%08x.%08x.%08x"
```
and verifying that the 7th register is filled with `41` (the value of `A`) tell us that we control the 7th register.
Now we can write the address of the target variable to this register and then use the `%n` specifier to write anything there. However this time we must write a specific value. Since the `%n` specifier writes the number of bytes written so far, we can use padding to write any amount of bytes we want and then write the value to the target address: 
```
p32(0x804a040) + "%64x" + "%7\$n"
```
In this case we want to write 68 bytes so by sending the address we are writing 4 bytes and then we write 64 bytes of padding which together will make 68 bytes.
Revealing the flag `SSof{And_what_I_want}`

## Implementation

Full implementation can be found [here](write-specific-value.sh).

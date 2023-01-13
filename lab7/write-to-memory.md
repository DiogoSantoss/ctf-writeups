# Challenge `Write to Memory` Writeup

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
Now we can write the address of the target variable to this register and then use the `%n` specifier to write anything there:
```
p32(0x804a040) + "%7$n"
```
Revealing the flag `SSof{Write_where_I_want}`

## Implementation

Full implementation can be found [here](write-to-memory.sh).

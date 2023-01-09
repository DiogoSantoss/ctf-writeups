# Challenge `Match an exact value` Writeup

- Vulnerability: 
  - Buffer overflow
- Where:
  - test and buffer variables
- Impact:
  - allows to bypass if test

## Analyzing the server

The main function creates two variables `test` and `buffer` and initializes 
`test` to zero and `buffer` to the user input. This input is read using the 
`gets` function.

## Exploit

Since the `gets` function does not check the length of the input, we can
overflow the `buffer` variable and overwrite the `test` variable.
This only works because the `test` variable was initialized first which means
that the `buffer` variable is located "on top" of the `test` variable in stack.
To overflow compute the offset of the `test` variable from the `buffer` variable
and then write any value "offset+1" times.
Using GDB we can place a breakpoint, run the program and read the address of `test` 
and `buffer` variables by using the `p &variable` command.
The offset equals to `0x40`.
Since this time we want to write a specific value we must fill the buffer first
with `0x40` characters and then write the `dcba` value to the `test` variable to 
pass the `test == 0x61626364` condition, revealing the flag `SSof{Buffer_Overflow_can_change_values_to_wh4t_you_want}`.

## Implementation

Full implementation can be found [here](match-an-exact-value.py).

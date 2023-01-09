# Challenge `Simple Overflow` Writeup

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
Using GDB we can place a breakpoint at `*main+71` (before the gets function) and
read the address of `test` and `buffer` variables by using the `p &variable` command.
This gives us `0x80` meaning that to overflow we need to write a string with
the length of `0x81` characters to pass the `test != 0` condition, 
revealing the flag `SSof{Buffer_Overflow_and_you_control_local_variables}`.

## Implementation

Full implementation can be found [here](simple-overflow.py).

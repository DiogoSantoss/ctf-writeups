# Challenge `Calling Functions` Writeup

- Vulnerability: 
  - Buffer overflow
- Where:
  - fp and buffer variables
- Impact:
  - allows to change function pointer

## Analyzing the server

The main function creates two variables `fp` and `buffer` and initializes 
`fp` to zero and `buffer` to the user input. This input is read using the 
`gets` function.

## Exploit

Since the `gets` function does not check the length of the input, we can
overflow the `buffer` variable and overwrite the `fp` variable.
This only works because the `fp` variable was initialized first which means
that the `buffer` variable is located "on top" of the `fp` variable in stack.
To overflow compute the offset of the `fp` variable from the `buffer` variable
and then write any value "offset+1" times.
Using GDB we can place a breakpoint, run the program and read the address of `fp` and 
`buffer` variables and the address of `win` function by using the `p &variable` command.
The offset is `0x20` and the function address is `0x080486f1`.
Since this time we want to write a specific value we must fill the buffer first
with `0x20` characters and then write the function address value.
Now when the program calls the `fp` function it will call the `win` function,
revealing the flag `SSof{Buffer_Overflow_on_function_pointers}`.

## Implementation

Full implementation can be found [here](calling-functions.py).

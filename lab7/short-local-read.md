# Challenge `Short Local Read` Writeup

- Vulnerability: 
  - Format strings
- Where:
  - printf function
- Impact:
  - allows to read arbitrary memory

## Analyzing the server

The main function reads the user input to a buffer then reads the flag to a variable and finally calls the `printf` function with the user input as argument.

## Exploit

By running `gdb` and placing a breakpoint before `printf` is called, its possible to see that the flag is stored on the 7th register. We can use this information to read the flag by sending a format string that will print the value of the 7th register. However the buffer only has 5 characters so it's necessary to use the `%n$s` specifier to print the value of the nth register:
```
"%7$s"
```
Revealing the flag `SSof{Just_use_positional_arguments}` 

## Implementation

Full implementation can be found [here](short-local-read.sh).

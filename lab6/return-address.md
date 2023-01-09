# Challenge `Return Address` Writeup

- Vulnerability: 
  - Buffer overflow
- Where:
  - challenge function return address
- Impact:
  - allows to return to other address

## Analyzing the server

The challenge function creates one variables `buffer` and initializes `buffer` to the
user input. This input is read using the `gets` function.
The main function calls the `challenge` function but not the `win` function.

## Exploit

Since the `gets` function does not check the length of the input, we can
overflow the `buffer` variable and change the return address of `challenge` function.
It's known that the stack keeps the `saved eip` in the stack so that the function
knows where to return after it finishes.
In GDB place a break point somewhere in the `challenge` function and run the program.
When the breakpoint is reached, run the `info f` command to see at what address the
`eip` is located.
Then compute the offset between the `eip` address and the `buffer` address which is
`0x16`.
Since we want to jump to the `win` function we must fill the buffer first with `0x16`
characters and then write the `win` function address value (`0x080486f1`).
Now when the programs returns from the `challenge` function it will return to the
`win` function, revealing the flag `SSof{Overflow_of_r37urn_address}`.

## Implementation

Full implementation can be found [here](return-address.py).
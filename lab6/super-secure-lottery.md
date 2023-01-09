# Challenge `Super Secure Lottery` Writeup

- Vulnerability: 
  - Buffer overflow
- Where:
  - run_lottery function in read call
- Impact:
  - allows to change variable value

## Analyzing the server

The server create a `lottery` string and fills it with random values.
Then reads user input to `guess` and if the `guess` is equal to `lottery` the user wins.
This read is done using the `read` function but the length of the input is `GUESS_SIZE` 
while the `guess` string has a `LOTTERY_LEN` length which is smaller, so we can overflow the string.

## Exploit

While the use of canaries will prevent some stack overflows, they are
only checked when the function return but this `run_lottery` function
never returns so we can change the value of a canary and the program 
won't notice.
By analysing the disassemble code we can conclude that the stack after
performing the `memcmp` function should look something like this:
```
-- prize                  --
-- guess                  --
-- LOTTERY_LEN            --  --> 3 arguments for memcmp
-- 0                      --
-- guess                  --
-- GUESS_SIZE             --  --> 3 arguments for read
-- "What is your guess: " --  --> 1 argument for printf
-- ebx                    --  
-- ebp                    --
-- eip                    -- 
-- lottery                --  --> 1 argument for run_lottery
```
By computing the offset between the `guess` variable and the `lottery` variable
we can input a string big enough to overflow the `guess` variable and overwrite
the `lottery` variable so that they have the same value.
To do so, first input 8 characters for the `guess` value then 40 random characters
and finally the same 8 characters for the `lottery`.
This will reveal the flag `SSof{You_will_never_guess_a_totally_random_lottery}`.

## Implementation

Full implementation can be found [here](super-secure-lottery.sh).
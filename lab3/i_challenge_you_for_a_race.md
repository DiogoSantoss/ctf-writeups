# Challenge `I challenge you for a race` Writeup

- Vulnerability: 
  - Time-of-check Time-of-use / Race condition
- Where:
  - `access` and `fopen` functions
- Impact:
  - allows access to protected files

## Analyzing the server

This challenge consists in accessing a protected file named flag.
The server has a folder `challenge` with the following files:
- `flag` - the flag
- `challenge` - the read_file.c compiled
- `Makefile` - the Makefile used to compile the challenge
- `read_file.c` - the source code of the challenge  

The binary receives a file name as input and uses the `access` function to checks if the user has access to the file (using the real UID).  
If it does, prints the content to the stdout using the `fopen` function to open the file (by verifying the permissions with the effective UID).   
Notice that the challenge file has the `S bit` set, meaning that the file runs with the permissions of the owner, which is root.

## Exploit

Start by creating a dummy file and a symbolic link to this file.
```bash
touch dummy
ln -sf dummy not_flag
```
Then, call the binary with this symbolic link by using `echo` and pipes
At the same time, using fork, create a symbolic link to the flag file with the same name as the symbolic link previously created.
```bash
echo "/tmp/95562/not_flag" | /challenge/challenge &  
ln -sf /challenge/flag not_flag
```
If the timing is right, the `access` function will return true then we change the link to the flag file and `fopen` will read it and reveal the flag `SSof{Time_of_Check_Time_of_Use_or_tuctuc_racing}`.
This works because `fopen` uses the effective UID (which is root because of the `S bit` in the binary) to check the permissions of the file, while `access` uses the real UID.

## Implementation

These code snippets and full implementation can be found [here](i_challenge_you_for_a_race.sh).
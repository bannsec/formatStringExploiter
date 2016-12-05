========================
Quickstart
========================

Concept
========================
The concept behind ``formatStringExploiter`` is to give you a class object that
abstracts a format string exploit. In general, what you will need to do as a
user is to simply provide the base class of ``FormatString`` with a function
that takes in a single argument of a string and returns the results of the
format string on that string. As a user, you don't have to worry about the
details of how the format string vulnerability works, you simply provide a
function to allow the FormatString class to interact with it.

Once the ``FormatString`` class is instantiated, it will attempt to
automatically discover the offset and padding required for this particular
vulnerability. Once done, it returns you a class object that you can use to
interact with this vulnerability.

Note that, for now, these calls are `immediate`. This means that once you make
the call, that information is immediately being sent to the vulnerable
application.


Instantiating a Class
=====================
Instantiating a class is simple. You need three things. First, create a
function that will allow the ``FormatString`` class to interact with this
vulnerability, such as the following:

.. code-block:: python

  def exec_fmt(s):
    p.sendline(s)
    out = p.recvuntil("myVar value is:",drop=True)
    p.recvuntil("Input: ")
    return out

Notice that we didn't define anything about this vulnerability. All this
function does is take in arbitrary input, executes said input, then returns the
output of the format string.

Next, determine the details of the binary. You can do this manually, however
the easier way to do it if you have the binary is to use pwntools to parse out
the relevant information:

.. code-block:: python

  from pwn import *
  elf = ELF("./a.out")

Now we have a pwntools object that contains the relevant information that
``FormatString`` needs. Finally, let's instantiate a ``FormatString`` class
object.

.. code-block:: python

  from formatStringExploiter.FormatString import FormatString
  fmtStr = FormatString(exec_fmt,elf=elf)
  

Reading
========
The ``FormatString`` class provides a means for leaking (or attempting to leak)
a given address. Note that this may or may not be possible given various
nuances of the format string. When deciding to leak data, you need to
understand what type of data you wish to leak. By default, ``FormatString``
will leak raw bytes as a string. However, the leaker is built on top of
pwntools Memleak helper, and you will likely wish to use those function as they
provide caching and other smart features to the leak. The following are the
functions that are recommended:

.. code-block:: python

  fmtStr.leak.b(addr) # Leak one byte from address addr
  fmtStr.leak.w(addr) # Leak one word from address addr
  fmtStr.leak.d(addr) # Leak one dword from address addr
  fmtStr.leak.q(addr) # Leak one qword from address addr
  fmtStr.leak.s(addr) # Leak one string from address addr
  fmtStr.leak.p(addr) # Leak one pointer from address addr


Writing
========
The ``FormatString`` class also provides you the ability to attempt to
abitrarily write a value to a given address. Similar to reading, when writing
you need to inform the ``FormatString`` class what the length of the write you
wish to do is. Effectively, the syntax is the same as for reading, aside for
replacing the "." with a "_".

.. code-block:: python

  fmtStr.write_b(addr,value) # Write value byte to addr
  fmtStr.write_w(addr,value) # Write value word to addr
  fmtStr.write_d(addr,value) # Write value dword to addr
  fmtStr.write_q(addr,value) # Write value qword to addr
  fmtStr.write_s(addr,value) # Write value string to addr

Remember, if you want to query the same location you just modified, you will
want to dump the Memleak cache after writing. This is because the Memleak
utilizes a caching sceme that assumes once it reads a place in memory that
place won't change. Thus, since you have changed it, you need to tell the
leaker to forget the old value so that you can get the new one.

This is done by using ``fmtStr.leak.clear[bwdq]`` method calls.

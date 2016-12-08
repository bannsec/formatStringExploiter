=======
Gotchas
=======

Hanging on Write
================
There are a few reasons for hanging on write. Check the following:

* Check your format string harness waiting on input.
* Check your ``badChars`` input to the FormatString class. Depending on how your program recieves input, it may have different characters to avoid.
* If you are using ``pwntools`` to communicate with the application, be sure to add ``buffer_fill_size=0xffff`` to the setup line, such as ``p = process("./a.out",buffer_fill_size=0xffff``.

On the last, there is currently a limitation in how ``pwntools`` handles recieving input where it will only recieve a maximum of 4096 characters. When writing large values, you will write up to 65535 characters, thus this argument is needed. At time of writing, this change is in a pull request and not yet in ``pwntools`` proper. If you are having issues, use my fork of ``pwntools`` as it has this change integrated. https://github.com/owlz/pwntools

Be Careful About Your ``exec_fmt`` Function!!
=============================================
You need to be careful about where you are starting your input for your ``exec_fmt`` function. This is because there are many things that ``FormatString`` infers based off of what you return to it. If you do not return the format string from the actual start of the return, then your writes or reads may be off.

When in doubt, break at the vulnerable format function to ensure you're getting all the data. Sometimes there is data before the actual return data in the buffer (such as "hello, " or whatever). That output must be accounted for and so must be returned to ``FormatString``.

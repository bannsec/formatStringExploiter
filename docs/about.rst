===============================
About ``formatStringExploiter``
===============================

Introduction to ``formatStringExploiter``
=========================================
``formatStringExploiter`` is a library written in python to help simplify the
exploitation of format string vulnerabilities. It does this by abstracting away
the notion of how to exploit these vulnerabilities for reading and writing into
simple class properties.

As a user of ``formatStringExploiter``, your job is simply to create a python
function that will interact with the program and return the results of any
string that is given to it. You do not have to understand what offsets or
padding is required, you can simply utilize it as if it were a primitive
operation.


Supported Architectures
=======================
Unlike the first version, this version supports and has been tested against
i386 and amd64. In the future it's possible that it can work against other
architectures such as ARM and MIPS, but they are untested as of now.

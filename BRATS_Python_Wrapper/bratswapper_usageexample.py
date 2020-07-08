#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import brats
import multiprocessing as mult # Only needed for the MP example


# Bind the BRATS install location
test = brats.Bind("/soft/brats/brats") 

# As we are now bound to the class we can run multiple files and/or methods either in series with execfile()...
retvalsingle = test.execfile("testcommands.txt") # This is an instance
#test.execfile("testcommands_2.txt") # This is another instance
print(retvalsingle)

# Or in parallel with multiexec...
files = ["./testcommands.txt", "./testcommands_2.txt"] # List of files e.g. read from a directory
retvalmulti = test.multiexec(files,) # Syntax: multiexec(list ["files", "to", "process"], int number_of_cores)
print(retvalmulti)
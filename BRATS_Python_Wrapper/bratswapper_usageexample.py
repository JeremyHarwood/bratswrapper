#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import brats

# Bind the BRATS install location
test = brats.Bind("/soft/brats/brats")

# As we are now bound to the class we can run multiple files and/or methods either in series with execfile()...
return_val_1 = test.execfile("testcommands_1.txt") # This is an instance
return_val_2 = test.execfile("testcommands_2.txt") # This is another instance
print(return_val_1) # Returns a dictionary {file : returncode}. Returns 0 on success, else returns an error code.
print(return_val_2)

# Or in parallel with multiexec...
files = ["./testcommands_1.txt", "./testcommands_2.txt"] # List of files e.g. read from a directory
return_val_multi = test.multiexec(files,2) # Syntax: multiexec(list ["files", "to", "process"], int number_of_cores)
print(return_val_multi) # Returns a dictionary {commandfilename : returncode}. Returns 0 on success, else returns an error code.

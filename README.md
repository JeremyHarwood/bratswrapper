# bratswrapper

This is the first iteration of the Python wrapper for BRATS.

This early version currently only supports the running of command files in which
BRATS commands, tasks, and parameters should be placed in the order by which they
are to be processed, with one command per line.

Single core and multiprocessing are both supported.

Only brats.py is required to allow usage, which can then be imported in the
standard manner (#import brats).

See bratswrapper_usageexample.py and accompanying .txt files for example usage.

***************************** IMPORTANT PLEASE READ *****************************

Note there is no BRATS command and syntax error checking in this early version!
Only Python errors are handled. Incorrect commands are ignored which may lead to
unexpected results or failure to complete the run, particularly when setting
paramaters within a task.
It is therefore suggested that a manual test run is performed on a sample dataset
by simply running BRATS, then copying and pasting the contents of the command 
file into the terminal.

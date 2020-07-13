"""
######### Python wrapper for the Broadband Radio Astronomy Tools (BRATS) ########

This is the first iteration of the Python wrapper for BRATS.

This early version currently only supports the running of command files in which 
BRATS commands, tasks, and parameters should be placed in the order by which they
are to be processed, with one command per line.

Single core and multiprocessing are both supported.

See bratswrapper_usageexample.py and accompanying .txt files for example usage.

***************************** IMPORTANT PLEASE READ  *****************************

 Note there is no BRATS command and syntax error checking in this early version!
 Only Python errors are handled. Incorrect commands are ignored which may lead to
 unexpected results or failure to complete the run, particularly when setting
 paramaters within a task.
 It is therefore suggested that a manual test run is performed on a sample dataset
 by simply running BRATS, then copying and pasting the contents of the file into
 the terminal.

 *********************************************************************************


@author: Jeremy Harwood
@email: jeremy.harwood@physics.org

##################################################################################
"""

import sys
import os.path
import subprocess
import multiprocessing as mult 

# Base class for the BRATS wrapper
class Bind:

    def __init__(self, install_dir: str):
        self._install = install_dir

    def execfile(self, file_loc: str) -> dict:
        return _Script._execfile(self, file_loc)

    def multiexec(self, file_list: list, num_proc: int) -> dict:
        return _Multiexec._multiexec(self, file_list, num_proc)

# Child class: processes command files and executes 
class _Script(Bind):
     
    def __init__(self): 
        super(_Script, self).__init__()

    def _execfile(self, file_loc: str) -> dict:

        try:
            commandsfile = open(file_loc, "r")
        except FileNotFoundError:
            print("\n*** Error: File not found. Ensure the commands file %s exists ***\n" % (file_loc))
            return {file_loc: 404}
        except Exception as e:
            print("\n*** Error: %s ***\n*** Unable to open the commands file %s for reading. Check the file exists and the appropriate permissions are set ***\n" % (str(e), file_loc))
            return {file_loc: 401}

        try:
            __process = subprocess.Popen([self._install], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            data = commandsfile.read()
            __process.communicate(input=data.strip())
            commandsfile.close()
            return {file_loc: 0}
        except Exception as e:
            print("\n*** Error: %s ***\n*** BRATS processing failed***\n" % (e))
            return {self._install: 404}

# Child class: handles multiprocessing for command files
class _Multiexec(_Script):
    
    def __init__(self): 
        super(Multiexec, self).__init__()

    def _multiexec(self, file_list: list, num_proc: int) -> dict:

        if os.path.exists(self._install) == False:
            print("\n*** Error: File not found. Ensure the brats installation %s exists ***\n" % (self._install))
            return {"Error": 404}
        try: 
            pool = mult.Pool(num_proc) # Run on 2 cores
            returnvalue = pool.map(self.execfile, file_list)
            pool.close()
            pool.join()
            return returnvalue
        except Exception as e:
            print("\n*** Error: %s ***\n*** BRATS processing failed***\n" % (e))
            return {"Error": str(e)}

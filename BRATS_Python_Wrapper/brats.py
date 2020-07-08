"""

Notes:
    
    There should only be one polarization intent per observation i.e one leakege cal, one angle cal. If this is not the case, it should be split off to make it so before the pipeline is run.
    Polarisation calibration currently setup for L, S, and C band
    Stokes I currently setup for P, L, S, C, and X band

@author: Jeremy Harwood
@email: jeremy.harwood@physics.org
"""

#pragma once
import sys
import os.path
import subprocess
import multiprocessing as mult 

class Bind:
    """description of class"""

    def __init__(self, installdir: str):
        self._install = installdir

    def execfile(self, fileloc: str) -> int:
        return _Script._execfile(self, fileloc)

    def multiexec(self, filelist: list):
        return _Multiexec._multiexec(self, filelist)


class _Script(Bind):

    def __init__(self): 
        super(_Script, self).__init__()

    def _execfile(self, fileloc: str) -> int:

        try:
            commandsfile = open(fileloc, "r")
        except FileNotFoundError:
            print("\n*** Error: File not found. Ensure the commands file %s exists ***\n" % (fileloc))
            return {fileloc: 404}
        except Exception as e:
            print("\n*** Error: %s ***\n*** Unable to open the commands file %s for reading. Check the file exists and the appropriate permissions are set ***\n" % (str(e), fileloc))
            return {fileloc: 401}

        try:
            __process = subprocess.Popen([self._install], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            data = commandsfile.read()
            __process.communicate(input=data.strip())
            commandsfile.close()
            return {fileloc: 0}
        except Exception as e:
            print("\n*** Error: %s ***\n*** BRATS processing failed***\n" % (e))
            return {self._install: 404}


class _Multiexec(_Script):

    def __init__(self): 
        super(Multiexec, self).__init__()

    def _multiexec(self, filelist: list):

        if os.path.exists(self._install) == False:
            print("\n*** Error: File not found. Ensure the brats installation %s exists ***\n" % (self._install))
            return {"Error": 404}

        file_list = ["./testcommands.txt", "./testcommands_2.txt"] # Something we would probably create by reading  a directory

        try: 
            pool = mult.Pool(processes=2) # Run on 2 cores
            returnvalue = pool.map(self.execfile, file_list)
            pool.close()
            pool.join()
            return returnvalue
        except Exception as e:
            print("\n*** Error: %s ***\n*** BRATS processing failed***\n" % (e))
            return {"Error": str(e)}

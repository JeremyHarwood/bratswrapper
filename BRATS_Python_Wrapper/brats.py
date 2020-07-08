"""

Notes:
    
    There should only be one polarization intent per observation i.e one leakege cal, one angle cal. If this is not the case, it should be split off to make it so before the pipeline is run.
    Polarisation calibration currently setup for L, S, and C band
    Stokes I currently setup for P, L, S, C, and X band

@author: Jeremy Harwood
@email: jeremy.harwood@physics.org
"""

#pragma once
import subprocess

class bind:
    """description of class"""

    def __init__(self, installdir: str):
        self.__install = installdir

    def execfile(self, fileloc: str) -> int:

        try:
            commandsfile = open(fileloc, "r")
        except FileNotFoundError:
            print("\n*** Error: File not found. Ensure the commands file %s exists ***\n" % (fileloc))
            return 404
        except Exception as e:
            print("\n*** Error: %s ***\n*** Unable to open the commands file %s for reading. Check the file exists and the appropriate permissions are set ***\n" % (str(e), fileloc))
            return 404

        try:
            __process = subprocess.Popen([self.__install], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            data = commandsfile.read()
            __process.communicate(input=data.strip())
            commandsfile.close()
            return 0
        except Exception as e:
            print("\n*** Error: %s ***\n*** BRATS processing failed***\n" % (e))
            return 100

pexamine
========

PEXAMINE displays PE sectional data, imports for specific DLL's and checks for packing.

#####Created by Tristan aka R3OATH (www.r3oath.com)

###Requirements:
PEXAMINE makes use of [Pefile](http://code.google.com/p/pefile/) and [PrettyTable](https://pypi.python.org/pypi/PrettyTable). Make sure to grab and install these before using.

###Examples:

####Usage

Running `python pexamine.py` will display the usage syntax.

![Usage](http://www.r3oath.com/images/pexamine/usage.jpg)

####Listing loaded/imported DLL's

Specifying the optional `d` arugment will list all of the DLL's loaded/imported in the EXE.

![DLLs](http://www.r3oath.com/images/pexamine/dlls.jpg)

####Listing Imported functions from a specific DLL

Giving a specific DLL name will make the script search for it inside of the EXE. 
If the DLL exists it's import table will be displayed as well, with each functions address.

![Imports](http://www.r3oath.com/images/pexamine/imports.jpg)

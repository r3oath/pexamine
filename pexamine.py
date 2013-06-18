# Author: Tristan Strathearn
# Website: www.r3oath.com
# Copyright (C) 2013 All Rights Reserved.

import sys
import pefile
import peutils
import prettytable

def PrettyPrint(text):
    print '[+] ' + text

def usage():
    PrettyPrint('Usage: ./pexamine.py <exe-file> <dll-name>')

def about():
    PrettyPrint('PEXAMINE: Created by Tristan aka R3OATH')
    PrettyPrint('Website: www.r3oath.com')
    PrettyPrint('~')

def main(args):
    if len(args) != 3:
        usage()
        sys.exit(1)

    # Mention the Author/Website :)
    about()

    exe = str(args[1]) # Eg: 'C:\\Windows\\notepad.exe'
    dll = str(args[2]) # Eg: 'USER32.dll'

    PrettyPrint('Examining EXE: %s' % exe)
    PrettyPrint('Using DLL: %s' % dll)

    try:
        pe = pefile.PE(exe)
        renderSectionData(pe)
        renderPackerStatus(pe)
        renderImportsData(pe, dll)
    except:
        PrettyPrint('Error: Please check argument 1 <exe-file>.')

def renderSectionData(pe):
    section_names       = []
    section_addresses   = []
    section_data_sizes  = []

    for section in pe.sections:
        section_names.append(section.Name.strip('\x00'))
        section_addresses.append('0x%08x' % section.Misc_PhysicalAddress)
        section_data_sizes.append('0x%08x' % section.SizeOfRawData)

    pt = prettytable.PrettyTable()
    pt.add_column('Section Name', section_names, align='l')
    pt.add_column('Physical Address', section_addresses, align='r')
    pt.add_column('Raw Data Size', section_data_sizes, align='r')
    PrettyPrint('EXE Sectional Data:')
    print pt

def renderImportsData(pe, dll_name):
    match = False

    for table in pe.DIRECTORY_ENTRY_IMPORT:
        if table.dll.lower() != dll_name.lower():
            continue

        PrettyPrint('The DLL "%s" was found in the imports table!' %
                    dll_name)
        match = True

        import_functions    = []
        import_addresses    = []
        import_dll_name     = table.dll

        for function in table.imports:
            import_functions.append(function.name)
            import_addresses.append('0x%08x' % function.address)

        pt = prettytable.PrettyTable()
        pt.add_column('Function Name', import_functions, align='l')
        pt.add_column('Address', import_addresses, align='r')
        PrettyPrint('DLL Imports for %s:' % import_dll_name)
        print pt

    if not match:
        PrettyPrint('The DLL "%s" could not be found.' % dll_name)

def renderPackerStatus(pe):
    if peutils.is_probably_packed(pe) == True:
        PrettyPrint('EXE has been packed!')
    else:
        PrettyPrint('EXE is not packed.')

if __name__ == '__main__':
    main(sys.argv)

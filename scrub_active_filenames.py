# Importing libraries
import csv
import os
import os.path
from os import listdir
from os.path import join, isfile
NAMEOFFILE = 'filenames_in_active.cvs'
NAMEOFDIR = 'active'
print('getting path...')
path = os.getcwd()
print('path: {0}'.format(path))
print('Directory to be scanned should be named \'{0}\' in {1}'.format(NAMEOFDIR,path))
# data to be written row-wise in csv file
path_active = join(path,NAMEOFDIR)

if os.path.isdir(path_active):
    active_file_names = []
    for f in listdir(path_active):  # for f in listdir(path_active) ie, for (potential filename in directory)
           if isfile(join(path_active,f)): # if filename joined to path is actually a file
               active_file_names.append(("{0}\t{1}").format(f,f)) #append new row with filename coppied twice to that row.
               
    # opening the csv file in 'w+' mode
    if os.path.exists(NAMEOFFILE):
        print('{0} already exists.'.format(NAMEOFFILE))
        choice = input('Do you want to overwrite? Type y for yes...')
        if (choice != 'y'):
            print('Aborting...')
            exit()
    
    file = open(NAMEOFFILE, 'w+', newline ='')
    print('Writing...')  
    # writing the data into the file
    with file:    
        writer = csv.writer(file, dialect='excel', delimiter =',')
        writer.writerows([c.strip() for c in r.split(',')] for r in active_file_names)
        file.write('\n') #append newline at end of file.
        
        print('Names of files in \'{0}\' directory output to file.'.format(NAMEOFFILE))
        file.close()
else:
    print('Files to be scanned should be located in a directory named \'{0}\' located in the current directory. Aborting...'.format(NAMEOFDIR)) 
exit()

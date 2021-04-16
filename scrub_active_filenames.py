# Importing library
import csv
import os
from os import listdir
from os.path import join, isfile
print('getting path...')
path = os.getcwd()
print('path: %s',path)
print('Directory to be scanned should be named \'active\' in %s',path)
# data to be written row-wise in csv file
path_active = join(path,'active')
if os.path.isdir(path_active):
    active_file_names = [f for f in listdir(path_active) if isfile(join(path_active,f))]
    # opening the csv file in 'w+' mode
    file = open('filenames_in_active' +'.cvs', 'w+', newline ='')
    print('Writing...')  
    # writing the data into the file
    with file:    
        writer = csv.writer(file, dialect='excel', delimiter =",")
        writer.writerows([c.strip() for c in r.split(',')] for r in active_file_names)
    print('Names of files in \'active\' directory output to file.')
    file.close()
else:
    print('Files to be scanned should be located in a directory named \'active\' located in the current directory.')
print('Exiting') 
exit()

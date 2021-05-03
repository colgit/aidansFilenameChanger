

# The purpose of this program is to rename the files in the active folder which 
# match the names in the first column, a_column to match the names in the second column, b_column.
# If there are duplicate names in b_column they will be renamed such that 
# (1),(2),(3)...etc is appended to the name.

# Open Names file for reading
# Load dictionary with A_column:b_column pairs.
# For each element in b_column
    #find all duplicate strings and save keys in rename list
    #i=1
    #while keys remain in renameList,
        #append "("+ i + ")"
        #pop off list
        #i++

# While keys remain in dictionary
    #change filename of matching key to renamed version.
    #remove key/pair from dictionary


import csv
import os
import os.path
from csv import DictReader
from os import listdir
from os.path import join, isfile
NAMEOFFILE = 'filenames_in_active.cvs'
NAMEOFDIR = 'active'
print('getting path...')
path = os.getcwd()
print('path: {0}'.format(path))
path_active = join(path,NAMEOFDIR)

filename_dict = {}

if os.path.isdir(path_active):                                                              #check that program can find a directory called "Active"
    active_file_names = [f for f in listdir(path_active) if isfile(join(path_active,f))]
    # opening the csv file in 'wr' mode
    if os.path.exists(NAMEOFFILE):
        with open(NAMEOFFILE, 'r', newline = '') as file_name_strings:
            print("loading dictionary...")

            file_data = csv.reader(file_name_strings)
            for row in file_data:
                row_split_list = row[0].split('\t')
                filename_dict[row_split_list[0]] = row_split_list[1]
            # file_data = csv.DictReader(file_name_strings, delimiter = '\t')
            # for name_string in file_data:
            #     filename_list.append(name_string)
        print(filename_dict,sep = '\n')

        for f in listdir(path_active):
            if (isfile(join(path_active,f))) & (f != filename_dict.get(f)):
                print("Found name change in {0}, \n changing name to {1}".format(f,{filename_dict.get(f)}))
                os.rename(join(path_active,f),join(path_active,filename_dict.get(f)))

    else:
        print('file does not exist')
else:
    print('Looking for directory named "active." ')    
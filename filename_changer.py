

# The purpose of this program is to rename the files in the active folder which 
# match the names in the first column, a_column, to match the names in the second column, b_column.
# If there are duplicate names in b_column they will be renamed such that 
# (2),(3),(4)...etc is appended to the name.


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
path_active = join(path,NAMEOFDIR)

def create_dictionary():
    filename_dict = {}
    if os.path.isdir(path_active):              #check that program can find a directory called "Active"
        if os.path.exists(NAMEOFFILE):          #check that cvs file of name changes exists. 
            with open(NAMEOFFILE, 'r', newline = '') as file_name_strings:      
                print("loading dictionary...")

                file_data = csv.reader(file_name_strings)

                for row in file_data:
                    row_split_list = row[0].split('\t')
                    filename_dict[row_split_list[0]] = row_split_list[1]
        else:
            print('CSV file {0} does not exist in current directory'.format(NAMEOFFILE))
    else:
        print('Looking for directory named "active." ')
    return filename_dict

def change_names():
    for entry in listdir(path_active):
        if filename_dict.get(entry) != None:
            new_filename = filename_dict.get(entry)
            try:
                print("Changing name from {0}, \n to {1}".format(entry,{new_filename}))
                os.rename(join(path_active,entry),join(path_active,new_filename))
            except FileExistsError:
                print("That name already exists.")
                append_num(1, new_filename, entry)

def append_num(num, filename, entry):
    flag = False
    while flag == False:
        root, ext = os.path.splitext(filename)
        new_filename = "{0}({1}){2}".format(root,num + 1,ext)
        print("Changing name from {0}, \n to {1}".format(entry,{new_filename}))
        try:
            os.rename(join(path_active,entry),join(path_active,new_filename))  
        except FileExistsError:
            print("That name already exists.")
            num = num + 1
        else:
            flag = True

filename_dict = create_dictionary()
change_names()
print("complete")
'''
@author: selenewaide
'''

import os

def check_file_exists(file_name):
    return os.path.isfile(file_name)

def open_file_and_read(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    return lines
    


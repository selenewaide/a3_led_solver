'''
@author: selenewaide
'''

import os

def check_file_exists(file_name):
    return os.path.isfile(file_name)

# open files and read it into 'lines'
def open_file_and_read(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    return lines

# create a grid - two dimensional list
def create_grid(grid_dimension):
    led_grid = [[False]*grid_dimension for _ in range(grid_dimension)]
    return led_grid
    

def parse_commands(each_line):
    
    command = ""
    params = ""
    
    if each_line.startswith("switch"):
        command = "switch"
        params = each_line.replace(command,"")
        params = params.strip()
    elif each_line.startswith("turn on"):
        command = "turn on"
        params = each_line.replace(command,"")
        params = params.strip()
    elif each_line.startswith("turn off"):
        command = "turn off"
        params = each_line.replace(command,"")
        params = params.strip()
        
    return command, params
    
def shlug(name):
    if name is None:
        return False
    return name.endswith('Shlug')
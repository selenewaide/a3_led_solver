'''
@author: selenewaide
'''

import os
import numpy as np

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
    else:
        return
    
    params_list = params.split(" ")  
    coordinates_1 = params_list[0]
    coordinates_2 = params_list[2]
        
    return command, coordinates_1, coordinates_2

def change_lights(command, coordinates1, coordinates2):
    led_grid = [[False]*10 for _ in range(10)]
    
    coordinates1_split = coordinates1.split(",")
    x1 = int(coordinates1_split[0])
    y1 = int(coordinates1_split[1])
    
    coordinates2_split = coordinates2.split(",")
    x2 = int(coordinates2_split[0])
    y2 = int(coordinates2_split[1])
    
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            led_grid[i][j] = True
            the_test_c = (i, j, led_grid[i][j])
                
    #grid_sum = np.size(led_grid) - np.count_nonzero(led_grid)
    grid_sum = np.count_nonzero(led_grid)          
    
    return led_grid, the_test_c, grid_sum

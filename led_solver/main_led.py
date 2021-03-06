'''
@author: selenewaide
'''

import os
import numpy as np
import sys
from numpy.core.defchararray import startswith

# check file exits
def check_file_exists(file_name):
    if not os.path.isfile(file_name):
        if file_name.startswith("http"):
            print("http is not supported. Use curl to download the file.")
        
        return
    else:
        return file_name

# open files and read it into 'lines'
def open_file_and_read(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    return lines

# create a grid - two dimensional list
def create_grid(grid_dimension):
    led_grid = [[False]*grid_dimension for _ in range(grid_dimension)]
    return led_grid
    
# split each valid instruction line into command, coordinates one and two
# returns command, coordinates one and two
# if the line is not properly formed, None is returned for all three variables
def parse_commands(each_line):
    
    command = ""
    params = ""
    
    # checks command is valid
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
        return None, None, None
    
    params_list = params.split(" ")  
    
    # checks coordinates are valid
    if len(params_list) == 3:
        coordinates_1 = params_list[0]
        coordinates_2 = params_list[2]
        
        coordinates1_split = coordinates_1.split(",")
        coordinates2_split = coordinates_2.split(",")
        
        int_x1 = int(coordinates1_split[0])
        int_y1 = int(coordinates1_split[1])
        
        int_x2 = int(coordinates2_split[0])
        int_y2 = int(coordinates2_split[1])
        
        x1_check = isinstance(int_x1,int)
        y1_check = isinstance(int_y1,int)
        
        x2_check = isinstance(int_x2,int)
        y2_check = isinstance(int_y2,int)
        
        if x1_check and y1_check and x2_check and y2_check:
            return command, coordinates_1, coordinates_2
        else:
            return None, None, None
    else:
        return None, None, None


# changes the grid elements as directed by the command and coordinates
# returns a grid and the sum
def change_lights(led_grid, command, coordinates1, coordinates2):
    coordinates1_split = coordinates1.split(",")
    x1 = int(coordinates1_split[0])
    y1 = int(coordinates1_split[1])
    
    coordinates2_split = coordinates2.split(",")
    x2 = int(coordinates2_split[0])
    y2 = int(coordinates2_split[1])
    
    # to deal with coordinates that are outside the grid
    x1 = max(0,x1)
    x2 = max(0,x2)
    y1 = max(0,y1)
    y2 = max(0,y2)
    x1 = min(len(led_grid)-1,x1)
    x2 = min(len(led_grid)-1,x2)
    y1 = min(len(led_grid)-1,y1)
    y2 = min(len(led_grid)-1,y2)
    
    if (command == "turn on"):
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                led_grid[i][j] = True
    elif (command == "turn off"):
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                led_grid[i][j] = False
    elif (command == "switch"):
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if (led_grid[i][j] == False):
                    led_grid[i][j] = True
                elif (led_grid[i][j] == True):
                    led_grid[i][j] = False
        
                
    #grid_sum = np.size(led_grid) - np.count_nonzero(led_grid)
    grid_sum = np.count_nonzero(led_grid)          
    
    return led_grid, grid_sum


# main function that calls the other functions above
# returns the grid and the count of 'true' (i.e. light count)
def main_led(file_path):
    light_count = 0
    
    check_for_file = check_file_exists(file_path)
    
    if check_for_file is None:
        print("File does not exist.")
        sys.exit()
    
    source_data = open_file_and_read(check_for_file)
    grid = create_grid(int(source_data[0]))
    
    for line in source_data[1:]:
        command, coordinates1, coordinates2 = parse_commands(line)
        if command is None or coordinates1 is None or coordinates2 is None:
            #print("Can't parse line: " + line)
            continue
        try:
            grid, light_count = change_lights(grid, command, coordinates1, coordinates2)
        except Exception:
            raise Exception("Error on line: " + line)
        
    return grid, light_count

'''
@author: selenewaide
'''

# test.py
import pprint
import sys
from nose.tools import *
from led_solver.main_led import check_file_exists, open_file_and_read, create_grid, parse_commands, change_lights, main_led

def test_fileExists_validfile():
    test_file_exists = check_file_exists("source_files/input_assign3_a.txt")
    eq_("source_files/input_assign3_a.txt",test_file_exists,"Error, not a valid output")
    #ok_(check_file_exists("source_files/input_assign3_a.txt"), "This is an invalid path or file name.")

def test_fileExists_notvalidfile():
    test_file_exists = not check_file_exists("thhffft.txt")
    eq_(True,test_file_exists,"Error, not a valid output")
    #ok_(not check_file_exists("source_files/input_assign3_aXX.txt"), "This is a valid file name and path.")

def test_open_file_and_read():
    lines = open_file_and_read("source_files/input_assign3_primary_test.txt")
    eq_(5,len(lines),"This is not the correct number of lines.")
    eq_("10",lines[0],"This is not a valid output.")
    eq_("turn off 3,2 through 4,4",lines[1],"This is not a valid output.")
    eq_("turn on 4,2 through 4,2",lines[-1],"This is not a valid output.")

def test_create_grid():
    test_grid = create_grid(10)
    eq_(10,len(test_grid),"Error, this is not the size of the grid.")
    #pprint.pprint(test_grid) -> prints the grid

def test_parse_commands():
    myString = parse_commands("switch 1,2 through 4,3")
    eq_(('switch', '1,2', '4,3'), myString, "Error, this is not the correct output")
    #print(myString)
    
def test_parse_commands_notvalid():
    myString = parse_commands("xx turn off this is my str")
    eq_(None, myString, "Error, this is not the correct output")
    #print(myString)
    
def test_change_lights():
    test_grid = create_grid(3)
    Result = change_lights(test_grid, "switch", "0,0", "2,2")
    eq_(([[True, True, True], [True, True, True], [True, True, True]], 9),  Result, "Error, this is not the correct output")
    #pprint.pprint(change_lights(test_grid, "switch", "0,0", "2,2"))
    
def test_main_led():
    grid, light_count = main_led("source_files/input_assign3_primary_test.txt")   
    eq_(34,light_count,"Error, this is not the correct number of lights.")
    #pprint.pprint(grid)
    
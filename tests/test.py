'''
@author: selenewaide
'''

# test.py
import pprint
import sys
from nose.tools import *
from led_solver.main_led import check_file_exists, open_file_and_read, create_grid, parse_commands, change_lights

def test_fileExists_validfile():
    ok_(check_file_exists("source_files/input_assign3_a.txt"), "This is an invalid path or file name.")

def test_fileExists_notvalidfile():
    ok_(not check_file_exists("source_files/input_assign3_aXX.txt"), "This is a valid file name and path.")

def test_open_file_and_read():
    lines = open_file_and_read("source_files/input_assign3_primary_test.txt")
    eq_(9,len(lines),"This is not the correct number of lines.")
    eq_("5000",lines[0],"This is not a valid output.")
    eq_("turn off 3990,2730 through 4692,4333",lines[1],"This is not a valid output.")
    eq_("turn on 4511,2123 through 4512,2125",lines[-1],"This is not a valid output.")

def test_create_grid():
    test_grid = create_grid(10)
    eq_(10,len(test_grid),"Error, this is not the size of the grid.")
    #pprint.pprint(test_grid) -> prints the grid

def test_parse_commands():
    myString = parse_commands("switch 1685,2653 through 4969,3361")
    print(myString)
    
def test_parse_commands_notvalid():
    myString = parse_commands("xx turn off this is my str")
    print(myString)
    
def test_change_lights():
    pprint.pprint(change_lights("turn on", "0,0", "2,2"))
    #pprint(a2d[3][5])
    
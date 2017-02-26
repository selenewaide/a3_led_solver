'''
@author: selenewaide
'''

# test.py
import sys
from nose.tools import *
from led_solver.main_led import check_file_exists, open_file_and_read

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
    
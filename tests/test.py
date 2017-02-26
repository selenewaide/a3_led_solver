'''
@author: selenewaide
'''

# test.py
import sys
from nose.tools import *
from led_solver.main_led import check_fileExists

def test_fileExists_validfile():
    ok_(check_fileExists("/Users/selenewaide/Dropbox/Semester1/COMP10280-Python/COMP10280_L6.pdf"), "This is an invalid path or file name.")

def test_fileExists_notvalidfile():
    ok_(not check_fileExists("/Users/selenewaide/Dropbox/Semester1/COMP10280-Python/COMP10280_L6x.pdf"), "This is an invalid path or file name.")

#===============================================================================
# def test_calculate():
#     ok_(calculate(2,3) == 6, 'calculation is incorrect')
# 
# def test_version():
#     eq_(sys.version_info[0], 3, 'Python is not version 3')
#===============================================================================

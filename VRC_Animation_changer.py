
import os
import sys
import re
from shutil import *

TC_path = 'D:\git\VRCSDK3_Koyuki\Assets\Koyuki\TTT system'
'''memory started directory'''
cd = os.getcwd()
x_size = 10
y_size = 10
def reset_TC():
    print("reset_TC")
    os.chdir(TC_path)
    for i in range(1,x_size+1):
        os.remove("X\X" + str(i) + ".anim")
        os.remove("Y\Y" + str(i) + ".anim.meta")
    for i in range(1,y_size+1):
        os.remove("Y\Y" + str(i) + ".anim")
        os.remove("Y\Y" + str(i) + ".anim.meta")
    os.remove("X\X.anim")
    os.remove("Y\Y.anim")
    os.remove("X\X.anim.meta")
    os.remove("Y\Y.anim.meta")
def set_TC():
    copyfile(cd + "\X.anim", TC_path + "\X\X.anim")
    copyfile(cd + "\Y.anim", TC_path + "\Y\Y.anim")
def TC_X():
    print("TC_X")
    os.chdir(TC_path + "\X")
    for i in range(1,x_size+1):
        copyfile("X.anim", TC_path + "\X\X" + str(i) + ".anim")
        with open(TC_path + "\X\X" + str(i) + ".anim", 'r') as f:
            filedata = f.read()
        filedata = filedata.replace('(namename)', 'X'+str(i))
        filedata = filedata.replace('(ST.x)', str(x_size * 0.01))
        filedata = filedata.replace('(ST.y)', str(y_size * 0.01))
        filedata = filedata.replace('(ST.z)', str((i-1) * 0.1))
        with open(TC_path + "\X\X" + str(i) + ".anim", 'w') as f:
            f.write(filedata)
    os.remove("X.anim")
def TC_Y():
    print("TC_Y")
    os.chdir(TC_path + "\Y")
    for i in range(1,y_size+1):
        copyfile("Y.anim", TC_path + "\Y\Y" + str(i) + ".anim")
        with open(TC_path + "\Y\Y" + str(i) + ".anim", 'r') as f:
            filedata = f.read()
        filedata = filedata.replace('(namename)', 'Y'+str(i))
        filedata = filedata.replace('(ST.x)', str(x_size * 0.01))
        filedata = filedata.replace('(ST.y)', str(y_size * 0.01))
        filedata = filedata.replace('(ST.w)', str((i-1) * 0.1))
        with open(TC_path + "\Y\Y" + str(i) + ".anim", 'w') as f:
            f.write(filedata)
    os.remove("Y.anim")
set_TC()
TC_X()
TC_Y()
from tkinter import *
import sys
import os
import signal
import time
from subprocess import *
from tkinter import messagebox



def file_previous_close():
    try:
        with open('home_id.txt', 'r') as f:
            lines = f.read().splitlines()
            
    except:
        print('first instance no to close previous file')


def writing_id():
    file_home_id=open("home.txt","w+")
    home_id=os.getpid()
    file_home_id.writelines('home\n')
    file_home_id.writelines(str(home_id))
    file_home_id.close()
    print(home_id)

writing_id()

from tkinter import *
from tkinter import  messagebox
import sys
import os
import signal
import time
from subprocess import  *
import sqlite3

def file_previous_close():
    try:
        with open('home_id.txt', 'r') as f:
           
            if(page!='login'):
                os.kill(int(last_line),signal.SIGKILL)
    except:
        print('First instance no need to close previous file')
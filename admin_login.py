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
            lines = f.read().splitlines()
            last_line = lines[-1]
            page=lines[-2]
            if(page!='login'):
                os.kill(int(last_line),signal.SIGKILL)
    except:
        print('first instance no need to close previous file')

#file_previous_close()

def writing_id():
    file_home_id=open("home_id.txt","w+")
    home_id=os.getpid()
    file_home_id.writelines('login\n')
    file_home_id.writelines(str(home_id))
    file_home_id.close()
    print(home_id)

#writing_id()


class Home():



    def __init__(self,master):




        menu = Menu(master)
        master.config(menu=menu)

        home=Menu(menu)
        menu.add_cascade(label='Home',menu=home)
        home.add_command(label='How to use?',command=self.take_a_tour)
        home.add_command(label='Terms of use',command=self.terms_of_use)
        home.add_separator()

        login_option=Menu(menu)
        menu.add_cascade(label='Register and Login',menu=login_option)
        login_option.add_command(label='Login',command=self.login)
        login_option.add_command(label='Register',command=self.register)
        login_option.add_separator()

        submenu = Menu(menu)
        menu.add_cascade(label='Help', menu=submenu)
        submenu.add_command(label='Contact Us',command=self.contact_us)
        submenu.add_command(label='FAQs', command=self.faq)
       
        submenu.add_separator()

        about_us=Menu(menu)
        menu.add_cascade(label='About Us',menu=about_us)
        about_us.add_command(label='About us',command=self.about_us)
        about_us.add_separator()


        exit_button=Menu(menu)
        menu.add_cascade(label='Exit',menu=exit_button)
        exit_button.add_command(label='Exit',command=menu.quit)

        #can do a prompt to do yes or  no


        exit_button.add_command(label='Minimize',command=self.minimize)


        ##login frame starts here

        frame = Frame(master)
        self.var1 = StringVar()
        self.var2 = StringVar()

        Label1 = Label(master, text='Username:')
        Label1.pack(padx=15, pady=5)

        entry1 = Entry(master, bd=5,textvariable=self.var1)
        entry1.pack(padx=15, pady=5)

        Label2 = Label(master, text='Password: ')
        Label2.pack(padx=15, pady=6)

        entry2 = Entry(master,show="*" ,bd=5,textvariable=self.var2)
        entry2.pack(padx=15, pady=7)

        btn = Button(frame, text='Check Login', command=self.login_submit)
        btn.pack(side=RIGHT, padx=5)
        frame.pack(padx=100, pady=19)

    def login_submit(self):
       # file_previous_close()
        print("Attemted to login")
        try:
            conn = sqlite3.connect('omega.db')
            login_db_object = conn.cursor()
        except:
            messagebox.showinfo("Failed", "Can't connect to the server")
            print("cant connect")

        self.username=self.var1.get()
        self.password=self.var2.get()
        print(self.username,self.password)
        if(self.username=='admin' and self.password=='admin'):
            print("Welcome")
            writing_id()
            call('python admin_login_success.py', shell=True)
        else:
            print("Login failed")
            messagebox.showinfo("Login Failed", "Invalid Username or Password")


    def contact_us(self):
           ##declare a message box
        print("contact")

    def faq(self):
        ##message box indicating faqs
        print('he')

    def login(self):
        print('login ')
        call('python login.py', shell=True)



    def register(self):
        ##create a register Frame
        print('register')
        call('python registration.py', shell=True)

    def report_infringement(self):
        ##essage box
        print('re')



    def take_a_tour(self):
        ##take a tour of the app
        print('take a tour')
        tour_take=Toplevel()
        tour_take.geometry("220x180")
        tour_take.title("Take a Tour")
        message=Message(tour_take,text="Go to Register and Login section to register as an employee. You need to provide the required details. After registration is completed you can login using your login credentials to access your employee dashboard.\n\n")
        message.grid(row=0,column=1)
        button = Button(tour_take, text="Close", command=tour_take.destroy)
        button.grid(row=6, column=1)

    def terms_of_use(self):
        print('message box having   terms of use')
        string_terms='''Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: \n \n The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.'''
        dialog=Toplevel()
        dialog.geometry("310x260")
        dialog.title("Terms of Use")
        message=Message(dialog,text=string_terms)
        message.grid(row=0,column=0)
        button = Button(dialog, text="Close", command=dialog.destroy)
        button.grid(row=4, column=0)

    def about_us(self):
        print('Display your info')
        top = Toplevel()
        top.geometry("230x200")
        top.title("About Us")

        msg = Message(top, text='This is Omega Employee Management System. This was primarily made as a basic Employee Management System as a project for University Curriculum but later after constantly improving this project and adding features it was made public.\n\n')
        msg.grid(row=0, column=15)
        button = Button(top, text="Okay", command=top.destroy)
        button.grid(row=4, column=15)

    def minimize(self):
        print('minimize the window')



root=Tk()
login_home=Home(root)
root.wm_geometry("1360x1200")
root.title("Admin Login")
root.mainloop()

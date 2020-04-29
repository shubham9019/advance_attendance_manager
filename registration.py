from tkinter import *
from tkinter import  messagebox
import sys
import os
import signal
import time
from subprocess import  *
from tkinter.scrolledtext import ScrolledText
import sqlite3




def file_previous_close():
    try:
        with open('home_id.txt', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            page=lines[-2]
            if(page!='registration'):
                os.kill(int(last_line),signal.SIGKILL)
    except:
        print('first instance no need to close previous file')

#file_previous_close()

def writing_id():
    file_home_id=open("home_id.txt","w+")
    home_id=os.getpid()
    file_home_id.writelines('registration\n')
    file_home_id.writelines(str(home_id))
    file_home_id.close()
    print('writing id')
    print(home_id)
def write_message_no(number):
    file=open("message.txt","w+")
    file.writelines(number)
    file.close()

def login_details(username,password):
    file=open("login_details.txt","w+")
    file.writelines(username+'\n')
    file.writelines(password)
    file.close()

#writing_id()


class Home():



    def __init__(self,master):




        menu = Menu(master)
        master.config(menu=menu)

        home=Menu(menu)
        menu.add_cascade(label='Home',menu=home)
        home.add_command(label='How to use?',command=self.take_a_tour)
        home.add_command(label='Terms of Use',command=self.terms_of_use)
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
        self.username = StringVar(master)
        self.password = StringVar()
        self.name=StringVar()
        self.dob=StringVar()
        self.email=StringVar()
        self.mobile_number=StringVar()
        self.aadhar_number=StringVar()
        self.variable = StringVar(master)
        self.address_var=StringVar()
        self.variable.set("Select Post:")  # default value


        post_employee=Label(master,text="Post:")
        #for options menu of post of employee
        w = OptionMenu(master, self.variable, "Maintainance", "Developer", "Engineer","HR")
        w.pack(padx=15,pady=3)

        employee_name=Label(master,text="Name:")
        employee_name.pack(padx=15,pady=4)
        employee_name_entry=Entry(master,bd=5,textvariable=self.name)
        employee_name_entry.pack(padx=24,pady=4)


        Label1 = Label(master, text='Username:')
        Label1.pack(padx=15, pady=5)
        entry1 = Entry(master, bd=5,textvariable=self.username)
        entry1.pack(padx=15, pady=5)


        email_label=Label(master,text='Email:')
        email_label.pack(padx=15,pady=6)
        email_entry=Entry(master,bd=5,textvariable=self.email)
        email_entry.pack(padx=15,pady=6)


        mobile_label=Label(master,text="Mobile:")
        mobile_label.pack(padx=15,pady=7)
        mobile_entry=Entry(master,bd=5,textvariable=self.mobile_number)
        mobile_entry.pack(padx=15,pady=7)

        aadhar_label=Label(master,text="Aadhar:")
        aadhar_label.pack(padx=15,pady=8)
        aadhar_entry=Entry(master,bd=5,textvariable=self.aadhar_number)
        aadhar_entry.pack(padx=15,pady=8)


        Label2 = Label(master, text='Password: ')
        Label2.pack(padx=15, pady=9)
        entry2 = Entry(master,show="*" ,bd=5,textvariable=self.password)
        entry2.pack(padx=15, pady=9)

        address_label=Label(master,text='Address:')
        address_label.pack(padx=15,pady=10)

        large_font = ('Verdana', 30)
        address_entry=Entry(master,textvariable=self.address_var,bd=10,font=large_font)
        address_entry.pack(padx=15,pady=10)



        btn = Button(frame, text='Register', command=self.register_submit)
        btn.pack(side=RIGHT, padx=5)
        frame.pack(padx=100, pady=19)


    def register_submit(self):
        self.select_employee_type=self.variable.get()
        self.username_call=self.username.get()
        self.name_call=self.name.get()
        self.email_call=self.email.get()
        self.aadhar_number_call=self.aadhar_number.get()
        self.mobile_number_call=self.mobile_number.get()
        self.password_call=self.password.get()
        self.address_call=self.address_var.get()
        try:
            conn = sqlite3.connect('omega.db')
            register_db_object = conn.cursor()
            login_db_object=conn.cursor()
        except:
            messagebox.showinfo("Failed", "Can't connect to the server")
            print("cant connect")

        if(self.select_employee_type=='Maintainance'):
            print('Maintainance')
            self.salary='30000'
            try:
                register_db_object.execute("INSERT INTO register (username,password,salary,aadhar_number,email,name,post,phone,address) values (?,?,?,?,?,?,?,?,?)",(self.username_call,self.password_call,self.salary,self.aadhar_number_call,self.email_call,self.name_call,self.select_employee_type,self.mobile_number_call,self.address_call))
                conn.commit()
                login_db_object.execute("INSERT INTO main.login_details (username,password)  values (?,?)",(self.username_call,self.password_call))
                conn.commit()
                conn.close()
                counter=1

            except:
                counter=0
                messagebox.showinfo("Failed", "Can't Register :( Username Occupied ")


        elif(self.select_employee_type=='Developer'):
            print('Dev')
            self.salary = '130000'
            try:
                register_db_object.execute(
                    "INSERT INTO register (username,password,salary,aadhar_number,email,name,post,phone,address) values (?,?,?,?,?,?,?,?,?)",
                    (self.username_call, self.password_call, self.salary, self.aadhar_number_call, self.email_call,
                     self.name_call, self.select_employee_type, self.mobile_number_call, self.address_call))
                conn.commit()
                login_db_object.execute("INSERT INTO main.login_details (username,password)  values (?,?)",
                                           (self.username_call, self.password_call))
                conn.commit()
                conn.close()
                counter=1

            except:
                counter=0
                messagebox.showinfo("Failed", "Can't Register :( Username Occupied ")


        else:
            self.salary = '70000'
            try:
                register_db_object.execute(
                    "INSERT INTO register (username,password,salary,aadhar_number,email,name,post,phone,address) values (?,?,?,?,?,?,?,?,?)",
                    (self.username_call, self.password_call, self.salary, self.aadhar_number_call, self.email_call,
                     self.name_call, self.select_employee_type, self.mobile_number_call, self.address_call))
                conn.commit()
                login_db_object.execute("INSERT INTO main.login_details (username,password)  values (?,?)",
                                           (self.username_call, self.password_call))
                conn.commit()
                conn.close()
                counter=1

            except:
                print("Unable to register")
                messagebox.showinfo("Failed", "Can't Register :( Username Occupied ")
                counter=0


        try:
            print("Checking for mobile number")
            write_message_no(self.mobile_number_call)
        except:
            print("Can't Write Mobile Number")

        try:
            def send_email(user, pwd, recipient, subject, body):
                import smtplib

                FROM = user
                TO = recipient if isinstance(recipient, list) else [recipient]
                SUBJECT = subject
                TEXT = body

                # Prepare actual message
                message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(user, pwd)
                server.sendmail(FROM, TO, message)
                server.close()

            email = ''
            pwd = ''
            recipient = self.email_call
            subject = 'Registered with Omega'
            body = 'Hi '+self.name_call+',\nYou have successfully registered with Omega Employee Management'+'\nRegards,\nTeam Omega'
            send_email(email, pwd, recipient, subject, body)
            print("mailsent")


        except:
            messagebox.showinfo("Error while sending Mail","Mail can't be sent")

        if(counter!=0):
            messagebox.showinfo("Successfully Registered","Taking you to the Login Page")
            call('python login.py', shell=True)

    def contact_us(self):
           ##declare a message box
        messagebox.showerror("Contact Us","You can contact us at shubham9019@gmail.com in case software dosen't respond or for any suggestions for improvements.")

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
        #sys.exit()


  



    def take_a_tour(self):
        ##take a tour of the app
        tour_take=Toplevel()
        tour_take.geometry("220x180")
        tour_take.title("Take a Tour")
        message=Message(tour_take,text="Go to Register and Login section to register as an employee. You need to provide the required details. After registration is completed you can login using your login credentials to access your employee dashboard.\n\n")
        message.grid(row=0,column=1)
        button = Button(tour_take, text="Close", command=tour_take.destroy)
        button.grid(row=6, column=1)
        print('take a tour')

    def terms_of_use(self):
        string_terms='''Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: \n \n The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.'''
        dialog=Toplevel()
        dialog.geometry("310x260")
        dialog.title("Terms of Use")
        message=Message(dialog,text=string_terms)
        message.grid(row=0,column=0)
        button = Button(dialog, text="Close", command=dialog.destroy)
        button.grid(row=4, column=0)
        print('message box having   terms of use')

    def about_us(self):
        top = Toplevel()
        top.geometry("230x200")
        top.title("About Us")

        msg = Message(top, text='This is Omega Employee Management System. This was primarily made as a basic Employee Management System as a project for University Curriculum but later after constantly improving this project and adding features it was made public.\n\n')
        msg.grid(row=0, column=15)
        button = Button(top, text="Okay", command=top.destroy)
        button.grid(row=4, column=15)
        print('Display your info')

    def minimize(self):
        print('minimize the window')



root=Tk()
login_home=Home(root)
root.wm_geometry("1360x1200")
root.title("Register Here")
root.mainloop()

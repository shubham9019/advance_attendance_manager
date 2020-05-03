## Omega Employee Manager

This a fairly advanced GUI based application developed to create and manage employee database along with other benefits like having an inbuilt attendance system.

**Key Features**

 - Gmail SMTP
 - Adding employees to the database
 - Admin login functionality
 - Searching employees
 - Updating employee information
 - Deleting employees
 - Attendance System
 - Secure User Login
 - User registration

SQLite DB is used for storage and management of database easily. It can also be easily integrated with any existing system. Attendance can be updated form Spreadsheets containing relevant data. Also there is a one way messaging system thorough which admin can contact the employees regarding any event or broadcast some message to every employee.

### Prerequisites

 - Python 3
 - PIP - _pip_ is the package installer for Python

## Built With
-   [tkinter](https://docs.python.org/3/library/tkinter.html)  - The standard Python interface to the Tk GUI toolkit
-  [Subprocess]([https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html))  - This allows you to spawn new processes, connect to their input/output.
-  [smtplib]([https://docs.python.org/2/library/smtplib.html](https://docs.python.org/2/library/smtplib.html))  - This can be used to send mail to any Internet machine
-  [xlrd]([https://xlrd.readthedocs.io/en/latest/](https://xlrd.readthedocs.io/en/latest/))  - Used for reading data and formatting information from Excel files
-  [xlwt]([https://xlwt.readthedocs.io/en/latest/](https://xlwt.readthedocs.io/en/latest/))  - Used for writing data and formatting information to older Excel files
-  [xlutils.copy]([https://xlutils.readthedocs.io/en/latest/copy.html](https://xlutils.readthedocs.io/en/latest/copy.html))  - The function in this module copies `xlrd.Book` objects into `xlwt.Workbook` objects so they can be manipulated.


## License

This project is licensed under the MIT License - see the  [LICENSE.md](https://github.com/shubham9019/omega_attendance_manager/blob/master/LICENSE)  file for details

**Note - Please PIP install all the dependencies from Built with section before use**
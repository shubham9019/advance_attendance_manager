## Python Chat app

This a basic chat application implemented using Python 3 and the most basic libraries possible to make this app. This app has various functionality including adding username after connecting to a server. Server can be accessed by multiple computers on the same network. Chat experience is seamless even after multiple devices connected to the same server.

### Highlights of this app

**Socket Programming** - Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server.

**Multi-threading** - Running several threads is similar to running several different programs concurrently.

**Key Features**

 - Graphical User Interface(GUI)
 - Socket Programming
 - Multiple device connection
 - Minimalist UI

This feels great to be tested on multiple computers. You can, of course, run the server and the client on the same machine for testing (using `127.0.0.1` for `HOST` in your client), but seeing the communication happen in real-time among different computers feels awesome. The server script will log which IP addresses are accessing it, and the client script will generate a GUI (after asking for the host address)

### Prerequisites

 - Python 3
 - PIP - _pip_ is the package installer for Python

## Built With
-   [tkinter](https://docs.python.org/3/library/tkinter.html)  - The standard Python interface to the Tk GUI toolkit
-  [Subprocess](https://docs.python.org/3/library/subprocess.html)  - This allows you to spawn new processes, connect to their input/output.
-  [smtplib](https://docs.python.org/2/library/smtplib.html)  - This can be used to send mail to any Internet machine
-  [xlrd](https://xlrd.readthedocs.io/en/latest/)  - Used for reading data and formatting information from Excel files
-  [xlwt](https://xlwt.readthedocs.io/en/latest/)  - Used for writing data and formatting information to older Excel files
-  [xlutils.copy](https://xlutils.readthedocs.io/en/latest/copy.html)  - The function in this module copies `xlrd.Book` objects into `xlwt.Workbook` objects so they can be manipulated.


## License

This project is licensed under the MIT License - see the  [LICENSE.md](https://github.com/shubham9019/omega_attendance_manager/blob/master/LICENSE)  file for details

**Note - Please PIP install all the dependencies from Built with section before use**
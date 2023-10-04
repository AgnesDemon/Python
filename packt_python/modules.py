import time
'''while True:
    with open("vegetables.txt") as file:
        print(file.read())'''
#will print the file forever
#say you want the file to be read and printed every ten seconds
#since there are no built in functions for this, get into the python interactive shell
#you want to look for built-in modules instead of functions
#type "import sys" into the python interactive shell
#next, type in "sys.builtin_module_names"
#this will give you a list of built-in modules
#you want to use time
#type "import time"
#type in "dir(time)" to see the list of what you have for that module
#an example is the sleep method
#help(time.sleep): sleep(seconds); delays execution for given number of seconds

#now you can adjust how fast the file is read and printed
'''while True:
    with open("fruits.txt") as file:
        print(file.read())
        time.sleep(10)'''
#in this case, it reads and prints the file every ten seconds
#you can also change the text as it's waiting as long as you save it
#however, if the file is deleted, then an error will occur because the file no longer exists
#to keep executing the python script even when the file is no longer there:
#type "import os"
#os is not among the built-in python modules
#type "sys.prefix", which should take you to a directory path
#navigate to that directory; you can also copy the directory without the quotes
#in Windows, type "start (directory name)" to navigate to the directory
#this will open Windows explorer
#open the lib folder by double-clicking and find the folder python3.7 (or whatever version I have)
#you should see a lot of python files
#find the os.py file and double-click it; open it with whatever text editor
#in Python, you should see a new tab that is labeled os.py
#in this tab, you should see python code, but do not make any changes to it and close it

#in the interactive python shell, type dir(os) to see what you have available for that module
#os.path.exists("filename") tells you True or False, depending if the file exists

#to prevent an error from occuring when a while doesn't exist:
import os

while True:
    if os.path.exists("vegetables.txt"):
        with open("vegetables.txt") as file:
            print(file.read())
    else:
        print("File does not exist")
    time.sleep(10)

#you always have to import modules


#first, you need to install postgreSQL from their website
#make sure it is for the correct platform you are using (Windows, Linux, etc)
#be sure to remember your password and other things from the installation
#once everything is downloaded, use pip install to install psycopg2
#you may bump into an error with the Windows version
#there are different ways to solve this problem:
    #download Visual Studio Code
    #use precompiled libraries, and you can find those on the webpage by Christoph Gohlk
        #look for psycopg2 wheel (whl) file for the right system (Windows, Linux, etc)
        #wheel files can be downloaded with pip
        #once you find the right one, download it and move it to the desired python folder (in my case, packt_python\interacting_with_databases)
        #pip install the wheel file you just moved into the folder
        #you can check if the wheel file installed properly in the python interactive shell
        #to find out what version it is, type psycopg2.__version__ in the python interactive shell

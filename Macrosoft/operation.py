import os
import subprocess

def rewriteInstallApp(newAppName):
    file = open("Macrosoft/settings.py", "r")
    list = [x for x in file]
    file.close()
    anotherFile = open("Macrosoft/settings.py", "w")

    for line in list:
        anotherFile.write(line + "")
        if "INSTALLED_APPS" in line:
            anotherFile.write("'"+newAppName+"'" + ",\n")
    anotherFile.close()


print("\nThis is a script which can help you do some operation about his project")

loop = True

while(loop):
    print("only choice a number from below.")
    print("type number 1: start a an new app in this \n")
    print("type number 2: run the local server\n")
    print("type number 3: make some change to you model.py file in the app, need make migration?\n")
    print("type number 4: do the test in one button!\n")
    print("type other irrevalent thing: I need to quit\n")
    a = input("Please input you number of choice: ")

    if int(a) == 1:
        print("let's start a new app")
        appName = input("Please input the app name you want: ")
        args = ["django-admin", "startapp", appName]
        a = subprocess.run(args)
        if(a.returncode == 0):
            rewriteInstallApp(appName)
            print("add success\n")
        else:
            print("there might be some error\n")

    elif int(a) == 2:
        print("let's run the local server")
        args = ["python", "manage.py", "runserver"]
        a = subprocess.run(args)
        if(a.returncode == 0):
            print("successfully run the local server.\n")

    elif int(a) == 3:
        print("you make some change to the model.py? let's deal with that")
        # I will finish that later

    elif int(a) == 4:
        print("we will do the test")
        args = ["python", "manage.py", "test"]
        process = subprocess.run(args)
        if(process == 0):
            print("test is run successfully\n")
        input()
    else:
        print("have a good day!\n")
        loop = False

print("Enjoy coding!")
input()
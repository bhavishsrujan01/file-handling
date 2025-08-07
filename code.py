from pathlib import Path
import os
def displayfiles():
    path = Path('')
    items = list(path.rglob('*'))
    print("THESE ARE THE EXISTING FILES")
    for i, items in enumerate(items):
        print(f"{i+1} -> {items}")
def createchoice():
    try :
        displayfiles()
        name = input("enter your file name : ")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as x:
                print("file created successfully! ")
        else:
            print("this file is already exists! ")
    except Exception as err:
        print(f"an error occured as {err}")
def readfiles():
    try:
        displayfiles()
        a = input("ENTER THE FILE NAME WHICH U WNT TO READ : ")
        with open(a,"r") as j:
            print(j.read())
    except Exception as err:
        print(f"AN ERROR! OCCURED AS {err}")
def updatefile():
    try:
        displayfiles()
        a = input("ENTER THE FILE NAME WHICH U WNT TO UPDATE : ")
        with open(a,"a") as j:
           data = input("enter the data : ")
           j.write(data)
        print("FILE AFTER UPDATIG")
        with open(a,"r") as j:
            print(j.read())       
    except Exception as err:
        print(f"AN ERROR! OCCURED AS {err}")
def deletefiles():
    try :
        displayfiles()
        K=input("ENTER THE FILE NAME WHICH U WANT TO DLETE : ")
        p=Path(K)
        if p.exists() and p.is_file():
            os.remove(p)
        print(f"{p} deleted successfully ")
        print(f"{displayfiles()} these are the existing files now ")
    except Exception as err:
        print(f" an error occured during deletion {err}")
print(" ENTER 1 TO CREATE FILE ")
print(" ENTER 2 TO READ FILE ")
print(" ENTER 3 TO UPDATE FILE ")
print(" ENTER 4 TO DELETE FILE ")
choice = int(input("ENTER YOUR CHOICE :-> "))
if choice==1:
    createchoice()
if choice==2:
    readfiles()
if choice==3:
    updatefile()
if choice==4:
    deletefiles()
if choice>4 and choice <1:
    print("INVALID CHOICE ")
from tkinter import *
from tkinter import filedialog
from tkinter import StringVar
from tkinter import messagebox
import os
import shutil

#---GLOBALS

postTitle = "Default Post Title"
postEntry = "Default Post Text"
postPath = "Select a path"

#---USER INTERFACE
master = Tk()

def path_selection(): #sets the desired posting directory
    global postPath

    answer = filedialog.askdirectory(parent=master, initialdir=os.getcwd(), title="Please select a folder:")
    postPath = answer
    print(postPath)

    displayHolderPathText.set(postPath) #just for display

def set_attributes():
    global postTitle
    global postDate
    global postEntry

    postTitle = title.get() #get inputted title
    postDate = date.get() #get inputted date
    postEntry = entry.get("1.0",END) #get inputted entry
    look_for_newlines()

    print("Path " + postPath)
    print("Title " + postTitle)
    print("Date " + postDate)
    print("Entry " + postEntry)

    if(postPath == "Select a path" or postTitle == "" or postDate == "" or postEntry == ""): #only write file if all inputs are filled out
        messagebox.showerror("Error", "You are missing an input field!")
        print("error")
    else:
        master.quit()

def printEntry():
    print(postEntry)

def look_for_newlines():
    for line in postEntry:
        if(line == "\n"):
            line += "'<br>'"


my_filetypes = [('all files', '.*'), ('text files', '.txt')]

Label(master, text="Entry Title").grid(row=1, sticky=N)
Label(master, text="Entry Date").grid(row=2, sticky=N)
Label(master, text="Entry Post").grid(row=3, sticky=N)

title = Entry(master, width=20)
date = Entry(master, width=20)
entry = Text(master, height=20, width=40)

title.grid(row=1, column=1,sticky=W)
date.grid(row=2, column=1,sticky=W)
entry.grid(row=3, column=1)

Button(master, text='Post', command=set_attributes).grid(row=4, column=1, sticky=N+S+E+W, pady=4)
Button(master, text='Set Posting Path', command=path_selection).grid(row=0, column=0, sticky=N + S + E + W, pady=4)

displayHolderPathText = StringVar()
displayHolderPathText.set(postPath)

Label(master, textvariable=displayHolderPathText).grid(row=0, column=1, sticky=E+W)


mainloop()

#---FILE HANDLING FUNCTIONS
# 1. create new folder with foldername=date entry
# 2. create new markdown file with name=index.md
# 3. write to index.md

def create_folder():
    global postPath

    os.chdir(postPath) #change to desired directory

    _dirname = postPath + "/" + postDate #append date to path
    os.mkdir(_dirname) #create directory at path with dir name=date

    postPath = _dirname
    print(postPath)

def create_and_write_file():
    global postPath
    os.chdir(postPath)

    _f = open("index.md", "w+") #create and open a new index.md if it doesn't exist

    _md_content = "---\n" + 'date: "' + postDate + 'T17:12:33.962Z"\n' + 'title: "' + postTitle + '"\n' + "---\n\n" + postEntry
    _f.write(_md_content)


    _f.close()

#---RUNTIME
create_folder()
create_and_write_file()
from tkinter import *
from tkinter.messagebox import showinfo



def newfile():
    global file
    root.title("Notepad")
    file = None
    TextArea.delete(1.0,END)

def openfile():
    pass

def savefile():
    pass

def exitfile():
    pass

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))


def About():
    showinfo("Notepad","Notepad by code with deva")


if __name__ == '__main__':
    # basic tkinter setup
    root = Tk()
    root.geometry("645x780")
    root.title("Notepad")

    # Add TextArea
    TextArea = Text(root,font="lucida 15 bold")
    file = None
    TextArea.pack(expand=True,fill=BOTH)

    # lets create a menu bar
    MenuBar = Menu(root)
    # FILE MENU STARTS
    FileMenu = Menu(MenuBar,tearoff=0)
    FileMenu.add_command(label="New",command="newfile")
    FileMenu.add_command(label="Open",command="openfile")
    FileMenu.add_command(label="Save",command="savefile")
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command="exitfile")
    MenuBar.add_cascade(label="File",menu=FileMenu)

    # EDIT MENU STARTS
    EditMenu = Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label="Cut",command="cut")
    EditMenu.add_command(label="Copy", command="cut")
    EditMenu.add_command(label="Paste", command="cut")
    MenuBar.add_cascade(label="Edit",menu=EditMenu)

    # HELP MENU STARTS
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command="About")
    MenuBar.add_cascade(label="Help",menu=HelpMenu)

    # adding scroll bar form tut22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.config(menu=MenuBar)
    root.mainloop()

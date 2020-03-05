from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
from tkinter import messagebox
class notepad:
    
    def __init__(self):
        self.root=Tk()
        self.root.title("NOTEPAD+")
        self.root.minsize(1366,1027) #for fixing min height of window
        self.root.maxsize(1366,1027) #these two lines fix the window size.
        self.root.configure(background="#542681" )    # ")# for changing window background-color.

        self.label1=Label(self.root,text="-------------------Login-------------------",bg="#542681",fg="#ffffff")
        self.label1.configure(font=("Constantia",22,"bold"))
        self.label1.pack(pady=(30,10)) #padding-left(x) and top(y)
        self.label1=Label(self.root,text="Username:",bg="#542681",fg="#ffffff")
        self.label1.configure(font=("Constantia",13,"italic"))
        self.label1.pack(pady=(30,10)) #padding-left(x) and top(y)
        self.loginbox1=Entry(self.root) #for creating input field
        self.loginbox1.pack(ipadx=50,ipady=10) #for changing the size of input/entry box x:width, y:height

        self.label1=Label(self.root,text="Password:",bg="#542681",fg="#ffffff")
        self.label1.configure(font=("Constantia",13,"italic"))
        self.label1.pack(pady=(30,5)) #padding-left(x) and top(y)
        self.loginbox2=Entry(self.root) #for creating input field
        self.loginbox2.pack(ipadx=50,ipady=10)
        self.click=Button(self.root,text="Login",width=30,height=2,command=lambda:self.loginc())
        self.click.pack(pady=(15,15))
        self.label1=Label(self.root,text="--------------Registration-------------",bg="#542681",fg="#ffffff")
        self.label1.configure(font=("Constantia",22,"bold"))
        self.label1.pack(pady=(50,10)) #padding-left(x) and top(y)
        self.click2=Button(self.root,text="Register",width=30,height=2,command=lambda:self.register())
        self.click2.pack(pady=(15,15))

        self.result=Label(self.root,bg="#0089ae",fg="#ffffff")
        self.result.configure(font=("Constantia",12))
        self.result.pack(pady=(5,10)) #padding-left(x) and top(y)


        self.root.mainloop()
    def register(self):
    
        self.register=Tk()
        self.register.title("REGISTRARION")
        self.register.minsize(1366,1027) #for fixing min height of window
        self.register.maxsize(1366,1027) #these two lines fix the window size.
        self.register.configure(background="#542681")# for changing window background-color.
    
        
         # Set label for user's instruction
        self.register.label1=Label(self.register, text="Please enter details below", fg="#ffffff",bg="#542681",font=("Constantia",16,"italic")).pack()
        self.register.label1=Label(self.register, text="").pack()

        username = StringVar()
        password = StringVar()
 
    # Set username label
        self.label1=Label(self.register,text="Username:",bg="#542681",fg="#ffffff")
        self.label1.configure(font=("Constantia",13,"italic"))
        self.label1.pack(pady=(30,10)) #padding-left(x) and top(y)
     
    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
        
        self.register.username_entry = Entry(self.register, textvariable=username)
        self.register.username_entry.pack()
       
    # Set password label
        self.label2=Label(self.register,text="Password:",bg="#542681",fg="#ffffff")
        self.label2.configure(font=("Constantia",13,"italic"))
        self.label2.pack(pady=(30,10)) #padding-left(x) and top(y)
        
    # Set password entry
        self.register.password_entry = Entry(self.register, textvariable=password, show='*')
        self.register.password_entry.pack()
        
        Label(self.register, text="").pack()
        
    # Set register button
        self.register.butt=Button(self.register, text="Register", width=10, height=1)
        self.register.butt.pack(pady=(15,15))
    
        
    def loginc(self):
        
        if self.loginbox1.get()=="12345" and self.loginbox2.get()=="12345" :
           self.notepad()
        else:
             self.label22=Label(self.root,text="LOGIN ERROR",bg="#005545",fg="#ffffff")
             self.label22.configure(font=("Constantia",22,"bold"))
             self.label22.pack(pady=(30,10))
        
        
    
     
    
    def notepad(self):
        def newFile():
            global file
            root.title("Untitled-Notepad")
            file=None
            TextArea.delete(1.0,END)


        def openFile():
            global file
            file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            if file=="":
                file=None
            else:
                root.title(os.path.basename(file)+"-Notepad")
                TextArea.delete(1.0,END)
                f=open(file,"r")
                TextArea.insert(1.0,f.read())
                f.close()


        def saveFile():
            global file
            if file==None:
                file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
                if file=="":
                    file=None

                else:
                    #Save as a new file
                    f = open(file,"w")
                    f.write(TextArea.get(1.0,END))
                    f.close()

                    root.title(os.path.basename(file)+"-Notepad")
                    print("File Saved")
            else:
                # Save the file
                f=open(file,"w")
                f.write(TextArea.get(1.0,END))
                f.close()


        def quitApp():
            root.destroy()

        def cut():
            TextArea.event_generate(("<<cut>>"))

        def copy():
            TextArea.event_generate(("<<copy>>"))

        def paste():
            TextArea.event_generate(("<<paste>>"))

        def about():
            showinfo("Notepad","Notepad by Code With ANIL")

        if __name__ == '__main__':
            #Basic tkinter setup
            root=Tk()
            root.title("Untitled-Notepad")
            root.geometry("644x788")

            #Add TextArea
            TextArea=Text(root,font="lucida 13")
            file=None
            TextArea.pack(expand=True,fill=BOTH)

            # Lets create a menubar
            MenuBar=Menu(root)
            FileMenu=Menu(MenuBar,tearoff=0)

            #File Menu Starts
            FileMenu=Menu(MenuBar,tearoff=0)
            # To open new file
            FileMenu.add_command(label="New",command=newFile)

            #To Open already existing file
            FileMenu.add_command(label="Open",command=openFile)

            # To save the current file

            FileMenu.add_command(label="Save",command=saveFile)
            FileMenu.add_separator()
            FileMenu.add_command(label="Exit",command=quitApp)
            MenuBar.add_cascade(label="File",menu=FileMenu)
            # File Menu ends

            # Edit Menu Starts
            EditMenu=Menu(MenuBar,tearoff=0)
            #To give a feature of cut,copy and paste
            EditMenu.add_command(label="Cut",command=cut)
            EditMenu.add_command(label="Copy",command=copy)
            EditMenu.add_command(label="Paste",command=paste)

            MenuBar.add_cascade(label="Edit",menu=EditMenu)

            # Edit Menu Ends

            root.config(menu=MenuBar)

            #Adding Scrollbar using rules from Tkinter lecture no 22
            Scroll=Scrollbar(TextArea)
            Scroll.pack(side=RIGHT, fill=Y)
            Scroll.config(command=TextArea.yview)
            TextArea.config(yscrollcommand=Scroll.set)
            
            # Help Menu Starts
            HelpMenu=Menu(MenuBar,tearoff=0)
            HelpMenu.add_command(label="About Notepad",command=about)
            MenuBar.add_cascade(label="Help",menu=HelpMenu)

            root.mainloop()


obj=notepad()
    

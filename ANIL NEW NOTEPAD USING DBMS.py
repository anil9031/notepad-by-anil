import mysql.connector
import time
from tkinter import *
from tkinter import messagebox
mydb=mysql.connector.connect(host='localhost',user='root',password='*************',database="db9");
mycoursor=mydb.cursor()
mycoursor.execute("show database")
class notepad:
    
   
    def start(self):
        
        self.root=Tk()
       
        self.root.title("NOTEPAD+")
        self.root.minsize(1366,1027) #for fixing min height of window
        self.root.maxsize(1366,1027) #these two lines fix the window size.
        self.root.configure(background="#999888")# for changing window background-color.
        
        self.label1=Label(self.root,text="-------------------Login-------------------",bg="#005545",fg="#ffffff")
        self.label1.configure(font=("Constantia",22,"bold"))
        self.label1.pack(pady=(30,10)) #padding-left(x) and top(y)
        self.u=StringVar(self.root)
        self.p=StringVar(self.root)
        

        Entry(self.root,textvariable=self.u).pack(ipadx=50,ipady=10) #for creating input field
         #for changing the size of input/entry box x:width, y:height
        Entry(self.root,textvariable=self.p).pack(ipadx=50,ipady=10) #for creating input field
       
        self.click=Button(self.root,text="Login",width=30,height=2,command=lambda:self.logok())
        self.click.pack(pady=(15,15))
        self.label1=Label(self.root,text="--------------Registration-------------",bg="#0089ae",fg="#ffffff")
        self.label1.configure(font=("Constantia",22,"bold"))
        self.label1.pack(pady=(50,10)) #padding-left(x) and top(y)
        self.click2=Button(self.root,text="Register",width=30,height=2,command=lambda:self.reg())
        self.click2.pack(pady=(15,15))

        self.result=Label(self.root,bg="#0089ae",fg="#ffffff")
        self.result.configure(font=("Constantia",12))
        self.result.pack(pady=(5,10)) #padding-left(x) and top(y)
        


        self.root.mainloop()

    



    def reg(self):
     self.root.destroy();
     root1=Tk();
     root1.geometry("300x300+100+50");
    
     a=StringVar(root1);
     b=StringVar(root1);
     Label(root1,text="userid",fg='yellow',bg='red').pack();
     Entry(root1,textvariable=a).pack();
     Label(root1,text="password",fg='yellow',bg='red').pack();
     Entry(root1,textvariable=b).pack();
     Button(root1,text='ok',fg='red',bg='yellow',command= lambda: self.register(root1,a,b)).pack();
     root1.mainloop();


    def register(self,root1,a,b):
    
     cur=mydb.cursor();
    
     l="select text from inform where userid=%s and password=%s;";
     cur.execute(l,(a.get(),int(b.get())));
    
    
    
     result=cur.fetchall();
     print(result);
    
     if(len(result) is not 0):
         Label(root1,text="user already present",fg='yellow',bg='red').pack();
     else:
         cur=mydb.cursor();
         l="insert into inform(userid,password)values(%s,%s);"
         cur.execute(l,(a.get(),int(b.get())));
         mydb.commit();
         d=Label(root1,text="registration successful",fg='red',bg='yellow').pack();
         Button(root1,text='login',fg='red',bg='yellow',command= lambda: self.start()).pack();
    
    
    
    
    
    

    def logok(self):
     
     cur=mydb.cursor();
    
     l="select text from inform where userid=%s and password=%s;"
     cur.execute(l,(self.u.get(),int(self.p.get())));
     result=cur.fetchall();
     a=self.u.get();
     b=int(self.p.get());
    
     if(len(result)==0):
         Label(self.root,text="your password or userid is wrong",fg='yellow',bg='red').pack();
        
        
     else:
        
       
         self.work(self.root,result,a,b);
     
    
    
    def of(self,root2,resul,n,o):
     root2.destroy();
     mydb=mysql.connector.connect(host='localhost',user='root',password='Saikat676@',database='db9');
     cur=mydb.cursor();
     l="select text from inform where userid=%s and password=%s;"
     cur.execute(l,(n,o));
     result=cur.fetchall();
     print(n,o);
     print(result);
    
     result=result[0][0];
     root5=Tk();
     root5.geometry("300x300+100+50");
     mymenu=Menu(root5);
     listone=Menu(root5);
     listone.add_command(label='new file',command= lambda: self.nf(root5,result,n,o));
     mymenu.add_cascade(label="file",menu=listone);
     root5.config(menu=mymenu);
    
    
     if(result is not None):
      result=result.split(" #@-69474452083 ");
      for i in range(len(result)):
          if(i is not 0):
             Label(root5,text="new {}".format(i),fg='yellow',bg='red',font=4).pack();
      p=StringVar(root5);
      Label(root5,text="enter your choice",fg='yellow',bg='red').pack();
      Entry(root5,textvariable=p).pack();
    
    
    
      Button(root5,text='ok',fg='red',bg='yellow',command= lambda: self.fe(root5,p,result,n,o)).pack();
      root5.mainloop();
     else:
    
         Label(root5,text="no file has",fg='yellow',bg='red',font=4).pack();
         root5.mainloop();
        
        
        
    
    
       
    def fe(self,root5,p,result,n,o):
     root5.destroy()
     p=p.get().split(" ");
     p=p[1];
     text=result[int(p)];
    
     root3=Tk();
     root3.geometry("300x300+100+50");
    
     tex=Text(root3,width=15,height=15,wrap=WORD);
     tex.pack();
     tex.delete(1.0,END);
     tex.insert(INSERT,text);
     mymenu=Menu(root3);
     listone=Menu(root3);
     listone.add_command(label='save change',command= lambda: self.scf(root3,result,tex,n,o,p));
     listone.add_command(label='open files',command= lambda: self.of(root3,result,n,o));
     mymenu.add_cascade(label="file",menu=listone);
     root3.config(menu=mymenu);
     root3.mainloop()


    def scf(self,root,result,tex,o,q,p):
     mydb=mysql.connector.connect(host='localhost',user='root',password='Saikat676@',database='db9');
     cur=mydb.cursor();
     l="select text from inform where userid=%s and password=%s;"
     cur.execute(l,(o,q));
     result=cur.fetchall();
     result=result[0];
     result=result[0]
     cur=mydb.cursor()
     r=tex.get(1.0,END);
     result=result.split(" #@-69474452083 ");
     result[int(p)]=r;
     result=result[1:len(result)]
     s=""
     for i in result:
         s=s+" #@-69474452083 "+i;
     l="update inform set text=%s where userid=%s and password=%s;"
     cur.execute(l,(s,o,q));
     mydb.commit();
     Label(root,text="File saved successfully",fg='yellow',bg='red').pack();
    
    

    def sf(self,root6,result,tex,k,m):
    
    
    
   
     root7=Tk();
     root7.geometry("300x300+100+50");
     cur=mydb.cursor();
     tui="select text from inform where userid=%s and password=%s;"
     cur.execute(tui,(k,m));
     result=cur.fetchall();
     print(result);
     result=result[0];
     result=result[0]
     if(result is not None):
      resul=result.split(" #@-69474452083 ");
      messagebox.showinfo('alert name is automatically given','do you want to save the file in the name of new {}?'.format(len(resul)));
     else:
         messagebox.showinfo('alert name is automatically given','do you want to save the file in the name of new 1?');
     print(result);
    
    
     r=tex.get(1.0,END);
     cur=mydb.cursor();
     mymenu=Menu(root7);
     listone=Menu(root7);
     listone.add_command(label='new file',command= lambda: self.nf(root7,result,k,m));
     listone.add_command(label='open files',command= lambda: self.of(root7,result,k,m));
     mymenu.add_cascade(label="file",menu=listone);
     root7.config(menu=mymenu);
    
    
     if(result is None):
        
       s=" #@-69474452083 "+r;
       l="update inform set text=%s where userid=%s and password=%s;"
       cur.execute(l,(s,k,m));
       mydb.commit();
       Label(root7,text="File saved successfully",fg='yellow',bg='red').pack();
       root6.destroy();
     
       root7.mainloop()
      
     else:
       s=result+" #@-69474452083 "+r;
       l="update inform set text=%s where userid=%s and password=%s;"
       cur.execute(l,(s,k,m));
       mydb.commit();
       Label(root7,text="File saved successfully",fg='yellow',bg='red').pack();
       root6.destroy();
      
       root7.mainloop()
    

    def nf(self,root2,result,i,j):
     root2.destroy();
     cur=mydb.cursor();
     l="select text from inform where userid=%s and password=%s;"
     cur.execute(l,(i,j));
     result=cur.fetchall();
     root6=Tk();
     root6.geometry("300x300+100+50");
    
    
    
     tex=Text(root6,width=15,height=15,wrap=WORD);
     tex.pack();
     mymenu=Menu(root6);
     listone=Menu(root6);
     listone.add_command(label='save file',command= lambda: self.sf(root6,result,tex,i,j));
     listone.add_command(label='open files',command= lambda: self.of(root6,result,i,j));
     mymenu.add_cascade(label="option",menu=listone);
    
     root6.config(menu=mymenu);
     root6.mainloop();
    
    def work(self,root4,result,g,h):
     root4.destroy();
   
     root2=Tk();
     root2.geometry("300x300+100+50")
   
     Label(root2,text="successfully login welcome",fg='yellow',bg='red').pack();
     mymenu=Menu(root2);
     listone=Menu(root2);
     listone.add_command(label='new file',command= lambda: self.nf(root2,result,g,h));
     listone.add_command(label='open files',command= lambda: self.of(root2,result,g,h));
     mymenu.add_cascade(label="file",menu=listone);
     root2.config(menu=mymenu);
     root2.mainloop();


obj=notepad();
obj.start()
    
   

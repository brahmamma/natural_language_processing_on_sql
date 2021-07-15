import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb
import random
import tkinter.ttk
from tkinter import Menu
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from fileoutput import *
from ln2sql import ln2sql
from PIL import ImageTk,Image


import mysql.connector 
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="brahmi"
)
db_cursor= db_connection.cursor(buffered=True)

class LoginApp(tk.Tk):
   
       
   def __init__(self):
       super().__init__()
       self.title("ConvertEasy")
       self.geometry("600x450+485+162")
       image = Image.open("b.png")
       resize_image = image.resize((600, 450))
       img = ImageTk.PhotoImage(resize_image)
       label1 = tk.Label(image=img)
       label1.image = img
       label1.pack()
       w=Frame(self,height=250,width=300,bg="#f2eaea")
       w.place(relx=.55,rely=.53,anchor="center")

       
       self.iconbitmap(r'large.ico')
       
       self.lblHeading =tk.Label(w,text=" Login ", font=("Helvetica", 18),fg="black")
       self.lbluname = tk.Label(w,text="UserName:", font=("Helvetica", 11),fg="black")
       self.lblpsswd = tk.Label(w,text="Password:", font=("Helvetica", 11),fg="black")
       self.txtuname = tk.Entry(w,width=90)
       self.txtpasswd = tk.Entry(w,width=70, show="*")
       self.btn_login = tk.Button(w, text="Login",font=("Helvetica", 11),bg="green",fg="white",command=self.login)
       self.btn_register= tk.Button(w, text="Register",font=("Helvetica", 11),bg="black",fg="white",command=self.open_registration_window)
       self.btn_forget = tk.Button(self, text="Forget pwd", font=("Helvetica", 11),bg="blue",fg="white",command=self.open_forget_window)
       self.btn_exit = tk.Button(w, text="Exit",font=("Helvetica", 11),bg="red",fg="white",command=self.exit)
       self.lblHeading.place(relx=0.10, rely=0.05, height=50, width=250)
       self.lbluname.place(relx=0.14, rely=0.280, height=21, width=100)
       self.lblpsswd.place(relx=0.14, rely=0.400, height=21, width=100)
       self.txtuname.place(relx=0.46, rely=0.289,height=20, relwidth=0.4)
       self.txtpasswd.place(relx=0.46, rely=0.398,height=20, relwidth=0.4)
       self.btn_login.place(relx=0.55, rely=0.56, height=24, width=76)
       self.btn_register.place(relx=0.25, rely=0.56, height=24, width=72)
       self.btn_forget.place(relx=0.42, rely=0.64, height=24, width=76 )
       self.btn_exit.place(relx=0.56, rely=0.7, height=24, width=61)
       
   def open_forget_window(self):
       
       self.withdraw()
       window=Forgetwindow(self)
       window.grab_set()
       
   def open_registration_window(self):
       self.txtuname.delete(0, tk.END)
       self.txtpasswd.delete(0, tk.END)
       self.txtuname.focus_set()
       self.withdraw()
       window = RegisterWindow(self)
       window.grab_set()
   


   def open_login_success_window(self):
       self.withdraw()
       window = Login_Success_Window(self)
       window.grab_set()
   def open_login_success_window2(self):
       self.withdraw()
       window = Login_Success_Window(self)
       window.grab_set()


   def show(self):
       """"""
       self.update()
       self.deiconify()
   def login(self):
       if db_connection.is_connected() == False:
              db_connection.connect()
       db_cursor.execute("CREATE DATABASE IF NOT EXISTS projectgui")  
       db_cursor.execute("use projectgui")
       db_cursor.execute("create table if not exists user(uid VARCHAR(30) NOT NULL  PRIMARY KEY,password VARCHAR(30),fname VARCHAR(30))")
       db_connection.commit()


       try:
           global username
           username = str(self.txtuname.get())  
           passwd = str(self.txtpasswd.get())  
           if username == "" :
               mb.showinfo('Information', "Please Enter Username")
               self.txtuname.focus_set()
               return
           if passwd == "" :
               mb.showinfo('Information', "Please Enter Password")
               self.txtpasswd.focus_set()
               return

           
           query ="SELECT * FROM user WHERE uid = '" + username + "' AND password = '" + passwd + "'"
           db_cursor.execute(query)
           rowcount = db_cursor.rowcount
           if db_cursor.rowcount == 1:
              self.txtuname.delete(0, tk.END)
              self.txtpasswd.delete(0, tk.END)
              self.txtuname.focus_set()
              
              self.open_login_success_window()
           else:
               mb.showinfo('Information', "Login failed,Invalid Username or Password.Try again!!!")
       except:
          db_connection.disconnect()


   def clear_form(self):
    self.txtuname.delete(0, tk.END)
    self.txtpasswd.delete(0, tk.END)
    self.txtuname.focus_set()

   def exit(self):
    MsgBox = mb.askquestion('Exit', 'Are you sure you want to exit',icon='warning')
    if MsgBox == 'yes':
        self.destroy()
class Login_Success_Window(tk.Toplevel):
   def __init__(self, parent):
         super().__init__(parent)
         self.original_frame = parent
         self.geometry("600x450+485+162")
         self.title("ConvertEasy")
         image_label=tk.Label(self)
         
         image2 = Image.open("b.png")
         image2=image2.resize((600,450))
         self.test_image2 = ImageTk.PhotoImage(image2)
         image_label.place(x=0, y=0)
         image_label.config(image=self.test_image2)
         self.iconbitmap(r'large.ico')
         #self.configure(background="#000000")
         w=Frame(self,height=200,width=350,bg="#f2eaea")
         w.place(relx=.59,rely=.5,anchor="center")
         self.lbl_Login_success = tk.Label(w, text="Welcome "+str(username), font=("Helvetica", 20),fg="green")
         self.lbl_Login_success.place(relx=0.15 , rely=0.05, height=30, width=250)
         #self.blbl_Login_success = tk.Label(w, text="Below Are your Account options", font=("Helvetica", 14),fg="black")
         #self.blbl_Login_success.place(relx=0.04, rely=0.26, height=20, width=350)
         #self.ubtn_exit = tk.Button(w, text="Update",font=("Helvetica", 11),fg="white",bg="blue",command=self.update_open)
         #self.ubtn_exit.place(relx=0.5, rely=0.4, height=24, width=61)
         self.txt=tk.Label(w,text="click on this button",font=("Helvetica", 11),fg="black")
         self.txt.place(relx=0.03, rely=0.35)
         #self.dbtn_exit = tk.Button(w, text="Delete",font=("Helvetica", 11),bg="red",fg="white",command=self.delete)
         #self.dbtn_exit.place(relx=0.5, rely=0.4, height=24, width=61)
         self.qbtn_exit = tk.Button(w, text="Generate",font=("Helvetica", 11),bg="green",fg="white",command=self.query_open)
         self.qbtn_exit.place(relx=0.4, rely=0.35, height=30, width=70)
         self.txt1=tk.Label(w,text="to generate a query",font=("Helvetica", 11),fg="black")
         self.txt1.place(relx=0.62,rely=0.35)
         self.hbtn_exit = tk.Button(w, text="History",font=("Helvetica", 11),bg="black",fg="white",command=self.history_open)
         self.hbtn_exit.place(relx=0.1, rely=0.8, height=24, width=68)
         self.resizable(0,0)
         self.lbtn_exit = tk.Button(w, text="Logout",font=("Helvetica", 11),bg="black",fg="white",command=self.onClose)
         self.lbtn_exit.place(relx=0.7, rely=0.8, height=24, width=68)
         self.btn_exit = tk.Button(w, text="Exit",font=("Helvetica", 11),bg="red",fg="white",command=self.exit)
         self.btn_exit.place(relx=0.4, rely=0.8, height=24, width=68)

   def query_open(self):
       self.withdraw()
       window = Query(self)
       window.grab_set()
   def history_open(self):
       self.withdraw()
       window = History(self)
       window.grab_set()
   def update_open(self):
      MsgBox = mb.askquestion('Update', 'Your past data will be lost if you update!! still you want to continue',icon='warning')
      if MsgBox == 'yes':
       self.withdraw()
       window = Update(self)
       window.grab_set()
   
   

   def delete(self):
    MsgBox = mb.askquestion('Delete', 'Are you sure you want to DELETE your account',icon='warning')
    if MsgBox == 'yes':
      query ="DELETE FROM user WHERE uid = '" + username +"'"
      db_cursor.execute(query)
      qe="drop table if exists " + username 
      db_cursor.execute(qe)
      db_connection.commit()
      MsgBox = mb.showinfo('Information', 'Your Account is deleted')
    if MsgBox == 'ok':
      self.destroy()
      self.original_frame.show()


         
   def exit(self):
    MsgBox = mb.askquestion('Exit', 'Are you sure you want to exit',icon='warning')
    if MsgBox == 'yes':
        self.destroy()
   def onClose(self):
    MsgBox = mb.askquestion('Logout', 'Are you sure you want to logout',icon='warning')
    if MsgBox == 'yes':
       """"""
       self.destroy()
       self.original_frame.show()
   def show(self):
       """"""
       self.update()
       self.deiconify()

class History(tk.Toplevel):
   def __init__(self, parent):
         super().__init__(parent)
         self.original_frame = parent
         self.geometry("600x450+485+162")
         image_label=tk.Label(self)
         
         image2 = Image.open("b.png")
         image2=image2.resize((600,450))
         self.test_image2 = ImageTk.PhotoImage(image2)
         image_label.place(x=0, y=0)
         image_label.config(image=self.test_image2)
         self.title("ConvertEasy")
         #self.configure(background="#000000")
         self.iconbitmap(r'large.ico')
         #s="delete from " + username + " where history=''"
         #db_cursor.execute(s)
         db_cursor.execute("use projectgui")
         q="select * from " + username+";"
         print(username)
         db_cursor.execute(q)
         records=db_cursor.fetchall()
         #print(records)
         self.tbtn_exit = tk.Button(self, text="Back",font=("Helvetica", 12),bg="black",fg="white",command=self.back)
         self.tbtn_exit.place(relx=0.45, rely=0.92, height=24, width=90)
         self.resizable(0,0)
         his=''
         for record in records:
            
            
            his=his+' # '+record[0]+'\n'+' -> '+record[1]+'\n\n'
         
         hisoutput=tk.Text(self,height=18,width=61,font=("Helvetica", 12))
         hisoutput.insert(1.0,his)
            
         hisoutput.configure(state='disabled')
         hisoutput.place(relx=0.03,rely=0.1)
            
         mb.showinfo('Information', "This is your past Question History")

   def back(self):
      self.destroy()
      self.original_frame.show()
         

class Query(tk.Toplevel):
   def __init__(self, parent):
         super().__init__(parent)
         self.original_frame = parent
         self.geometry("600x450+485+162")
         self.title("ConvertEasy")
         image_label=tk.Label(self)
         
         image2 = Image.open("b.png")
         image2=image2.resize((600,450))
         self.test_image2 = ImageTk.PhotoImage(image2)
         image_label.place(x=0, y=0)
         image_label.config(image=self.test_image2)
         
         self.iconbitmap(r'large.ico')
         #self.configure(background="#000000")
         self.resizable(0,0)
         
         self.sentence_frame = tk.LabelFrame(self, text="Input Sentence",font=("Helvetica", 13),padx=5, pady=5,height=60)
         self.sentence_frame.pack(fill="x", expand="no", padx=5, pady=10)
         self.input_sentence_string = StringVar()
         self.input_sentence_string.set("Enter a sentence...")
         self.input_sentence_entry = tk.Entry(self.sentence_frame, textvariable=self.input_sentence_string,font=("Helvetica", 12), width=100)
         self.input_sentence_entry.pack(side="right")
         #self.input_sentence_entry.bind('<Button-1>',self.clearEntry)
         
         self.database_frame = tk.LabelFrame(self, text="Database Selection",font=("Helvetica", 13), padx=5, pady=5,height=60)
         self.database_frame.pack(fill="x", expand="no", padx=5, pady=3)
         self.database_path_label = tk.Label(self.database_frame, text="No SQL dump selected...",font=("Helvetica", 12))
         self.database_path_label.pack(side="left")
         self.load_database_button = tk.Button(self.database_frame, text="Choose a SQL dump",font=("Helvetica", 12), command=self.find_sql_file, width=20)
         self.load_database_button.pack(side="right")
         
         self.btn_exit = tk.Button(self, text="Exit",font=("Helvetica", 15),bg="red",fg="white",command=self.exit)
         self.btn_exit.place(relx=0.52, rely=0.9, height=26, width=90) 
         self.tbtn_exit = tk.Button(self, text="Submit",font=("Helvetica", 15),bg="green",fg="white",command=self.submit)
         self.tbtn_exit.place(relx=0.32, rely=0.75, height=26, width=90)
         self.tbtn1_exit = tk.Button(self, text="Back",font=("Helvetica", 15),bg="black",fg="white",command=self.back)
         self.tbtn1_exit.place(relx=0.32, rely=0.9, height=26, width=90)
         self.reset = tk.Button(self, text="Reset", fg="white",bg="red",font=("Helvetica", 15),command=self.reset)
         self.reset.place(relx=0.52, rely=0.75, height=26, width=90)
         
   def exit(self):
    MsgBox = mb.askquestion('Exit', 'Are you sure you want to exit',icon='warning')
    if MsgBox == 'yes':
        self.destroy()
   def back(self):
      self.destroy()
      self.original_frame.show()
   def show(self):
       """"""
       self.update()
       self.deiconify()
   def reset(self):
        self.input_sentence_entry.focus_set()
        self.database_path_label["text"] = "No SQL dump selected"
        self.database_path_label["text"] = "No SQL dump selected..."
        self.input_sentence_string.set("Enter a sentence...")
        
        
   def find_sql_file(self):
        filename = tk.filedialog.askopenfilename(title="Select a SQL file",filetypes=[('sql files', '.sql'), ('all files', '.*')])
        self.database_path_label["text"] = filename
   
   def clearEntry(self):
      self.input_sentence_string.set("")
		
   def submit(self):
      try:
            thesaurus_path="C:/Users/pavani/Pictures/ln2sql-master1/thesaurus/th_english.dat";
            language_path="C:/Users/pavani/Pictures/ln2sql-master1/lang/english.csv";
			
            if (str(self.database_path_label["text"]) != "No SQL dump selected...") and (str(self.input_sentence_string.get()) != "Enter a sentence..."):
               ln2sql(self.database_path_label["text"], self.input_sentence_string.get(), language_path, thesaurus_path, './output.json','./output.txt')
               result=readtxt(self.database_path_label["text"])
               input_sen=self.input_sentence_string.get()

               w=Frame(self,height=350,width=540,bg="#f2eaea",padx=5,pady=5)
               w.place(relx=0.5,rely=0.5,anchor="center")


               userlabel=tk.Label(w,text="Input query :",font=("Helvetica", 12))
               userlabel.place(relx=0.02,rely=0.1)
               userquery=tk.Text(w,font=("Helvetica", 13),height=4,width=40)
               userquery.insert('1.0',self.input_sentence_string.get())
               userquery.place(relx=0.2,rely=0.1)

               self.sentence_frame.destroy()
               self.database_frame.destroy()
               self.database_path_label.destroy()
               self.tbtn_exit.destroy()
               self.reset.destroy()
               
               
               
               
               querylabel=tk.Label(w,text="SQL query :",font=("Helvetica", 12))
               querylabel.place(relx=0.02,rely=0.23)
               querydisplay=tk.Text(w,font=("Helvetica", 12),height=4,width=40)
               querydisplay.insert('1.0',result[0])
               querydisplay.configure(state='disabled')
               querydisplay.place(relx=0.2,rely=0.23)
               outputlabel=tk.Label(w,text="output :",font=("Helvetica", 12))
               outputlabel.place(relx=0.02,rely=0.47)
               queryoutput=tk.Text(w,height=8,width=40,font=("Helvetica", 12))
               print(type(result[1]))
               queryoutput.insert('1.0',result[1])
               queryoutput.configure(state='disabled')
               queryoutput.place(relx=0.2,rely=0.47)
                  
               mb.showinfo('Result', 'Parsing done!')
               
               try:
                  db_cursor.execute("CREATE DATABASE IF NOT EXISTS projectgui")
                  db_cursor.execute("use projectgui")
                  qui="Create table if not exists " + username + "(userquery TEXT,sqlquery TEXT)"
                  db_cursor.execute(qui)
                  insert_stmt = ("INSERT INTO "+username+"(userquery,sqlquery) VALUES (%s, %s)")
                  data =(str(self.input_sentence_string.get()),(result[0]))
                  db_cursor.execute(insert_stmt, data)

                  
                  #quk="INSERT INTO " + username  + "(history) VALUES ('%s')" %(str(self.input_sentence_string.get()),result[0])
                  #quk="insert in to "+username+"(userquery,sqlquery) values('%s','%s')" %(str(self.input_sentence_string.get()),str(result[0]))
                  #db_cursor.execute(quk)
                  #self.input_sentence_entry.focus_set()
                  db_connection.commit()
               except Exception as e:
                  mb.showinfo('Information', e)
                  self.input_sentence_entry.focus_set()
                  db_connection.rollback()
                  db_connection.close()
               
            else:
                   mb.showinfo('Warning','You must fill in all fields, please.')
      except Exception as e:
         mb.showinfo('Error',e)
            
            
            
class Query_sub(tk.Toplevel):
   def __init__(self, parent):
         super().__init__(parent)
         self.original_frame = parent
         self.geometry("900x450+485+162")
         self.title("ConvertEasy")
         self.iconbitmap(r'large.ico')
         self.configure(background="#000000")
         self.resizable(0,0)
         self.llbluname = tk.Label(self,text="QUERY:", font=("Helvetica", 19),bg="black",fg="white")
         self.llbluname.place(relx=0.0, rely=0.14, height=22, width=180)
         self.ltxtuname = tk.Entry(self,width=390)
         self.ltxtuname.place(relx=0.18, rely=0.1,height=203, relwidth=0.800)
         self.lbluname = tk.Label(self,text="ANSWER:", font=("Helvetica", 19),bg="black",fg="white")
         self.lbluname.place(relx=0, rely=0.68, height=22, width=180)
         self.txtuname = tk.Entry(self,width=390)
         self.txtuname.place(relx=0.180, rely=0.66,height=90, relwidth=0.800)
         self.tbtn_exit = tk.Button(self, text="Back",font=("Helvetica", 20),bg="black",fg="white",command=self.back)
         self.tbtn_exit.place(relx=0.49, rely=0.92, height=24, width=90)


   def back(self):
      self.destroy()
      self.original_frame.show()



class RegisterWindow(tk.Toplevel):
   def __init__(self, parent):
         super().__init__(parent)
         self.original_frame = parent
         self.geometry("600x450+485+162")
         self.title("ConvertEasy")
         image_label=tk.Label(self)
         
         image2 = Image.open("b.png")
         image2=image2.resize((600,450))
         self.test_image2 = ImageTk.PhotoImage(image2)
         image_label.place(x=0, y=0)
         image_label.config(image=self.test_image2)
         self.iconbitmap(r'large.ico')
         w=Frame(self,height=250,width=280,bg="#f2eaea")
         w.place(relx=.55,rely=.53,anchor="center")
         self.lblRegister = tk.Label(w, text="Register", font=("Helvetica", 18),fg="black")
         self.lblFName = tk.Label(w, text="Name:", font=("Helvetica", 10),fg="black")
         self.lblUId = tk.Label(w, text="UserName:", font=("Helvetica", 10), fg="black")
         self.lblPwd = tk.Label(w, text="Password:", font=("Helvetica", 10), fg="black")
         
         self.txtFName = tk.Entry(w,width=70)
         self.txtUId = tk.Entry(w,width=70)
         self.txtPwd = tk.Entry(w,width=70,show="*")
         self.btn_register = tk.Button(w, text="Register", font=("Helvetica", 11), bg="green", fg="white",command=self.register)
         #self.btn_cancel = tk.Button(w, text="Login", font=("Helvetica", 11), bg="black", fg="yellow",command=self.onClose)
         self.btn_exit = tk.Button(w, text="Exit",font=("Helvetica", 11),bg="Red",fg="white",command=self.exit)
         self.btn_clear= tk.Button(w, text="Login",font=("Helvetica", 11),fg="white",bg="black",command=self.onClose)

         self.lblRegister.place(relx=0.34, rely=0.101, height=25, width=100)
         self.lblFName.place(relx=0.12, rely=0.24, height=21, width=100)
         self.lblUId.place(relx=0.12, rely=0.36, height=21, width=100)
         self.lblPwd.place(relx=0.12, rely=0.48, height=21, width=100)
         self.txtFName.place(relx=0.490, rely=0.24, height=20, relwidth=0.4)
         self.txtUId.place(relx=0.490, rely=0.36, height=20, relwidth=0.4)
         self.txtPwd.place(relx=0.490, rely=0.48, height=20, relwidth=0.4)
         self.btn_register.place(relx=0.17, rely=0.62, height=24, width=85)
         #self.btn_cancel.place(relx=0.370, rely=0.630, height=24, width=205)
         self.btn_exit.place(relx=0.44, rely=0.74, height=24, width=61)
         self.btn_clear.place(relx=0.58, rely=0.62, height=24, width=85)
         self.resizable(0,0)
         

   def register(self):

       if db_connection.is_connected()== False:
             db_connection.connect()
       db_cursor.execute("CREATE DATABASE IF NOT EXISTS projectgui")  
       db_cursor.execute("use projectgui")  
       db_cursor.execute("Create table if not exists user(uid VARCHAR(30) NOT NULL  PRIMARY KEY,password VARCHAR(30),fname VARCHAR(30))")

       db_connection.commit()

       fname = self.txtFName.get()  
       uid = self.txtUId.get()  
       pwd = self.txtPwd.get()  
       if fname == "":
           mb.showinfo('Information', "Please Enter Firstname")
           self.txtFName.focus_set()
           return
       
       if uid == "":
           mb.showinfo('Information', "Please Enter User Id")
           self.txtUId.focus_set()
           return
       if pwd == "":
           mb.showinfo('Information', "Please Enter Password")
           self.txtPwd.focus_set()
           return
       
       
       
       
       db_cursor.execute("use projectgui")  
       query ="INSERT INTO user(uid,password,fname) VALUES ('%s','%s','%s')" %(uid,pwd,fname)

       try:
            
            db_cursor.execute(query)
            mb.showinfo('Information', "Registered Successfully")
            self.txtFName.delete(0, tk.END)
            self.txtUId.delete(0, tk.END)
            self.txtPwd.delete(0, tk.END)
            self.txtFName.focus_set()
            db_connection.commit()
       except:
            mb.showinfo('Information', "Registration Failed !!!This Username is already existed")
            self.txtFName.delete(0, tk.END)
            self.txtUId.delete(0, tk.END)
            self.txtPwd.delete(0, tk.END)
            self.txtFName.focus_set()
            db_connection.rollback()
            db_connection.close()


   def onClose(self):
       """"""
       self.destroy()
       self.original_frame.show()
       
   def clear_form(self):
    self.txtFName.delete(0, tk.END)
    self.txtUId.delete(0, tk.END)
    self.txtPwd.delete(0, tk.END)
    self.txtFName.focus_set()
    
   def exit(self):
     
    MsgBox = mb.askquestion('Exit', 'Are you sure you want to exit ',icon='warning')
    if MsgBox == 'yes':
        self.destroy()




        
class Forgetwindow(tk.Toplevel):
   def __init__(self, parent):
         super().__init__(parent)
         self.original_frame = parent
         self.geometry("600x450+485+162")
         self.title("ConvertEasy")
         image_label=tk.Label(self)
         
         image2 = Image.open("b.png")
         image2=image2.resize((600,450))
         self.test_image2 = ImageTk.PhotoImage(image2)
         image_label.place(x=0, y=0)
         image_label.config(image=self.test_image2)
         self.iconbitmap(r'large.ico')
         w=Frame(self,height=250,width=280,bg="#f2eaea")
         w.place(relx=.55,rely=.53,anchor="center")
         self.lblforget = tk.Label(w, text="Forget Password", font=("Helvetica", 17),fg="black")
         #self.lblFName = tk.Label(w, text="Name:", font=("Helvetica", 10),fg="black")
         self.lblUId = tk.Label(w, text="UserName:", font=("Helvetica", 12), fg="black")
         #self.lblPwd = tk.Label(w, text="Password:", font=("Helvetica", 10), fg="black")
         
         #self.txtFName = tk.Entry(w,width=70)
         self.txtUId = tk.Entry(w,width=70)
         #self.txtPwd = tk.Entry(w,width=70,show="*")
         self.btn_forget = tk.Button(w, text="submit", font=("Helvetica", 11), bg="green", fg="white",command=self.forget)
         #self.btn_cancel = tk.Button(w, text="Login", font=("Helvetica", 11), bg="black", fg="yellow",command=self.onClose)
         self.btn_exit = tk.Button(w, text="Exit",font=("Helvetica", 11),bg="Red",fg="white",command=self.exit)
         self.btn_clear= tk.Button(w, text="Login",font=("Helvetica", 11),fg="white",bg="black",command=self.onClose)

         self.lblforget.place(relx=0.23, rely=0.1, height=25)
         #self.lblFName.place(relx=0.12, rely=0.24, height=21, width=100)
         self.lblUId.place(relx=0.12, rely=0.36, height=21, width=100)
         #self.lblPwd.place(relx=0.12, rely=0.48, height=21, width=100)
         #self.txtFName.place(relx=0.490, rely=0.24, height=20, relwidth=0.4)
         self.txtUId.place(relx=0.490, rely=0.36, height=25, relwidth=0.4)
         #self.txtPwd.place(relx=0.490, rely=0.48, height=20, relwidth=0.4)
         self.btn_forget.place(relx=0.58, rely=0.6, height=24, width=85)
         #self.btn_cancel.place(relx=0.370, rely=0.630, height=24, width=205)
         self.btn_exit.place(relx=0.44, rely=0.74, height=24, width=61)
         self.btn_clear.place(relx=0.17, rely=0.6, height=24, width=85)
         self.resizable(0,0)
         

   def forget(self):
       w=Frame(self,height=250,width=280,bg="#f2eaea")
       w.place(relx=.55,rely=.53,anchor="center")
       self.uid = self.txtUId.get()
       
       if self.uid == "":
           mb.showinfo('Information', "Please Enter User Id")
           self.txtUId.focus_set()
           
       
       
       

       if db_connection.is_connected()== False:
             db_connection.connect()
       #db_cursor.execute("CREATE DATABASE IF NOT EXISTS projectgui")  
       db_cursor.execute("use projectgui")  
       #db_cursor.execute("Create table if not exists user(uid VARCHAR(30) NOT NULL  PRIMARY KEY,password VARCHAR(30),fname VARCHAR(30))")
       query ="SELECT * FROM user WHERE uid = '" + self.uid + "';"
       db_cursor.execute(query)
       rowcount = db_cursor.rowcount
       if db_cursor.rowcount == 1:
          
          self.txtUId.destroy()
          self.lblUId.destroy()
          self.lblpwd=tk.Label(w,text="Forget Password",font=("Helvetica", 17),fg="black")
          self.lblpwd.place(relx=0.23,rely=0.1,height=25)
          self.lblpwd=tk.Label(w,text="New Password",font=("Helvetica", 12),fg="black")
          self.lblpwd.place(relx=0.1,rely=0.28)
          self.pwd=tk.Entry(w)
          self.pwd.place(relx=0.5,rely=0.28)
          self.btn_forget=tk.Button(w,text="Submit",font=("Helvetica", 12), bg="green", fg="white",command=self.submit)
          self.btn_forget.place(relx=0.58, rely=0.55, height=24, width=85)
          self.btn_exit=tk.Button(w,text="exit",font=("Helvetica", 12), bg="red", fg="white")
          self.btn_exit.place(relx=0.44, rely=0.65, height=24, width=61)
          self.btn_clear=tk.Button(w,text="Register",font=("Helvetica", 12), bg="blue", fg="white")
          self.btn_clear.place(relx=0.17, rely=0.55, height=24, width=85)
          self.resizable(0,0)

         
          
       else:
          mb.showinfo('Information', "Invalid Username.Try again!!!")
       

       db_connection.commit()


   def submit(self):
          try:
             if(self.pwd.get()==""):
                mb.showinfo('error',"password not be empty")
               
             else:
                query ="UPDATE user set password ='"+self.pwd.get()+"' WHERE uid = '" + self.uid + "';"
                db_cursor.execute(query)
                mb.showinfo('info','password changed successfully')
                self.destroy()
                self.original_frame.show()
                
          except Exception as e:
             mb.showinfo('Error',e)
             
          

       

   def onClose(self):
       """"""
       self.destroy()
       self.original_frame.show()
       
   def clear_form(self):
    self.txtFName.delete(0, tk.END)
    self.txtUId.delete(0, tk.END)
    self.txtPwd.delete(0, tk.END)
    self.txtFName.focus_set()
    
   def exit(self):
     
    MsgBox = mb.askquestion('Exit', 'Are you sure you want to exit ',icon='warning')
    if MsgBox == 'yes':
        self.destroy()
   




if __name__ == "__main__":
   app = LoginApp()
   app.resizable(0,0)
   app.mainloop()

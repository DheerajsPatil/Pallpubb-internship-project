from tkinter import *
from tkinter import ttk,messagebox
from tkinter import filedialog
import sqlite3
class BookClass:
       def __init__(self,root):
              self.root=root
       #self.root.iconbitmap('my office logo.ico')
              self.root.title("PALLPUBB")#.title is used to title a software
              self.root.geometry("1535x780+0+0")#.geometry is used to set the height,weidth, and x,y axis of gui.
              #self.root.resizable(False,False)#.resizable is used to restrict user from expanding gui window, it set default.
              self.root.config(bg="#324370")#.config is used to configure the gui by changing its color,text,etc.
              self.btn_back =Button(self.root, text="Back",font=("Helvetica bold",12,"bold"), bg="#769ADD", fg="white", width=8,height=1,activebackground="#769ADD",activeforeground="White",command=self.close_window)
              self.btn_back.place(x=30, y=120)
              self.root.focus_force()


              self.var_searchby=StringVar()
              self.var_searchtxt=StringVar()
              self.var_cname=StringVar()
              self.var_language=StringVar()
              self.var_bname=StringVar()
              self.var_language=StringVar()
              self.var_quantity=StringVar()
              self.var_pname=StringVar()
              self.var_packages=StringVar()

              lbl_title=Label(root,text="BOOK")
              lbl_title.config(font=('Helvetica bold', 60,"bold"),bg="#769ADD",fg="#FFFFFF")
              lbl_title.place(x=580,y=0)
              lbl_title.pack(fill=X)
    
              SearchFrame=LabelFrame(self.root,text="Search Name or Contact No", bg="#324370", fg="#FFFFFF", font=("Calibri",12,"bold"),bd=2,relief=RIDGE)
              SearchFrame.place(x=500,y=150,width=600,height=70)
       #-------------combobox----------------------------------------------------------------
              cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","cname","bname"),state='readonly',justify=CENTER,font=("goudy old style",15))
              cmb_search.place(x=10,y=10,width=180)
              cmb_search.current(0)

       #----------------Content ------------------------------------------------------------

              txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("",15),bg="white").place(x=200,y=10)
              btn_search=Button(SearchFrame, text="Search",font=("",15),bg="#769ADD",fg="white",activebackground="#769ADD",activeforeground="White",cursor="hand2",command=self.search).place(x=440,y=9,width=150,height=30)
      
      #============Row 1=================
              lbl_cname=Label(self.root,text="Client Name",font=("",15),bg="#324370",fg="white").place(x=120,y=250)
              lbl_pname=Label(self.root,text="Printing Press ",font=("",15),bg="#324370",fg="white").place(x=1020,y=250)
       
              txt_cname=Entry(self.root,textvariable=self.var_cname,font=("",12),bg="#FFFFFF",fg="black").place(x=250,y=250,width=230,height=25)
              txt_pname=Entry(self.root,textvariable=self.var_pname,font=("",12),bg="#FFFFFF",fg="black").place(x=1150,y=250,width=230,height=25)
       
       #============Row 2=====================
              lbl_bname=Label(self.root,text="Book Name",font=("",15),bg="#324370",fg="white").place(x=120,y=310)
              lbl_quantity=Label(self.root,text="Quantity",font=("",15),bg="#324370",fg="white").place(x=1020,y=305)
       
              txt_bname=Entry(self.root,textvariable=self.var_bname,font=("",12),bg="#FFFFFF",fg="black").place(x=250,y=310,width=230,height=25)
              txt_quantity=Entry(self.root,textvariable=self.var_quantity,font=("",12),fg="black").place(x=1150,y=305,width=230,height=25)

       #============Row 3=======================
              lbl_language=Label(self.root,text="Language",font=("",15),bg="#324370",fg="white").place(x=120,y=365)
              lbl_Package=Label(self.root,text="Packages",font=("",15),bg="#324370",fg="white").place(x=1020,y=360)
       
              txt_language=Entry(self.root,textvariable=self.var_language,font=("",12),bg="#FFFFFF",fg="black").place(x=250,y=370,width=230,height=25)
              cmb_package=ttk.Combobox(self.root,textvariable=self.var_packages,values=("","Silver","Gold","Platinum"),state='readonly',justify=CENTER,font=("goudy old style",15))
              cmb_package.place(x=1150,y=360,width=230,height=25)
              cmb_package.current(0)

       #============Row 4=========================
              lbl_online=Label(self.root,text="Online",font=("",15),bg="#324370",fg="white").place(x=560,y=235)
       
              self.txt_online=Text(self.root,font=("",11),bg="white")
              self.txt_online.place(x=640,y=240, width=300, height= 65)

              lbl_paper=Label(self.root,text="PaperBack",font=("",15),bg="#324370",fg="white").place(x=520,y=320)
       
              self.txt_paper=Text(self.root,font=("",11),bg="white")
              self.txt_paper.place(x=640,y=330, width=300, height= 65)

              btn_save=Button(root,text="Save")
              btn_save.config(font=('Helvetica bold', 14,"bold"),bg="#769ADD",fg="white",activebackground="#769ADD",activeforeground="White",width=10,command=self.add)
              btn_save.place(x=800,y=470)
        
              btn_clearall=Button(root,text="ClearAll")
              btn_clearall.config(font=('Helvetica bold', 12,"bold"),bg="WHITE",fg="#000000",width=10,command=self.clear)
              btn_clearall.place(x=1280,y=470)

              btn_delete=Button(root,text="Delete")
              btn_delete.config(font=('Helvetica bold', 12,"bold"),bg="WHITE",fg="#000000",width=10,command=self.delete)
              btn_delete.place(x=1400,y=470)

              btn_update=Button(root,text="Update")
              btn_update.config(font=('Helvetica bold', 12,"bold"),bg="WHITE",fg="#000000",width=10,command=self.update)
              btn_update.place(x=1160,y=470)


#==================Clients Details====================================================

              clients_frame=Frame(self.root,bd=3,relief=RIDGE)
              clients_frame.place(x=0,y=520,relwidth=1,height=260,width=-10)

              scrolly=Scrollbar(clients_frame,orient=VERTICAL)
              scrolly.config(width=20)
              scrollx=Scrollbar(clients_frame,orient=HORIZONTAL)

              self.BooksTable=ttk.Treeview(clients_frame,columns=("cname","bname","language","online","paperback","ppress","quantity","packages"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
              scrollx.pack(side=BOTTOM,fill=X)
              scrolly.pack(side=RIGHT,fill=Y)
              scrollx.config(command=self.BooksTable.xview)
              scrolly.config(command=self.BooksTable.yview)
              self.BooksTable.heading("cname",text="Client Name")
              self.BooksTable.heading("bname",text="Book Name")
              self.BooksTable.heading("language",text="Language")
              self.BooksTable.heading("online",text="Online")
              self.BooksTable.heading("paperback",text="PaperBack")
              self.BooksTable.heading("ppress",text="Printing Press")
              self.BooksTable.heading("quantity",text="Quantity")
              self.BooksTable.heading("packages",text="Packages")
       
              self.BooksTable["show"]="headings"

              self.BooksTable.column("cname",width=90)
              self.BooksTable.column("bname",width=100)
              self.BooksTable.column("language",width=100)
              self.BooksTable.column("online",width=100)
              self.BooksTable.column("paperback",width=100)
              self.BooksTable.column("ppress",width=100)
              self.BooksTable.column("quantity",width=100)
              self.BooksTable.column("packages",width=100)
              self.BooksTable.pack(fill=BOTH,expand=1)
              self.BooksTable.bind("<ButtonRelease-1>",self.get_data)

              self.show()

#===============================================================================================

       def add(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             if self.var_cname.get()=="":
                 messagebox.showerror("Error","Client Name Must required",parent=self.root)
             else:
                 cur.execute("Select * from books where cname=?",(self.var_cname.get(),))
                 row=cur.fetchone()
                 cur.execute("Insert into books (cname,bname,language,online,paperback,ppress,quantity,packages) values(?,?,?,?,?,?,?,?)",(
                                         self.var_cname.get(),
                                         self.var_bname.get(),
                                         self.var_language.get(),
                                         self.txt_online.get('1.0',END),
                                         self.txt_paper.get('1.0',END),
                                         self.var_pname.get(),
                                         self.var_quantity.get(),
                                         self.var_packages.get(),   
                 ))
                 con.commit()
                 messagebox.showinfo("Success","Customer Added Successfully",parent=self.root)
                 self.show()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


       def show(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             cur.execute("select * from books")
             rows=cur.fetchall()
             self.BooksTable.delete(*self.BooksTable.get_children())
             for row in rows:
                 self.BooksTable.insert('',END,values=row)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

       def get_data(self,ev):
         f=self.BooksTable.focus()
         content=(self.BooksTable.item(f))
         row=content['values']
         self.var_cname.set(row[0])
         self.var_bname.set(row[1])
         self.var_language.set(row[2])
         self.txt_online.delete('1.0',END)
         self.txt_online.insert(END,row[3])
         self.txt_paper.delete('1.0',END)
         self.txt_paper.insert(END,row[4])
         self.var_pname.set(row[5])
         self.var_quantity.set(row[6])
         self.var_packages.set(row[7])


       def update(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             if self.var_cname.get()=="":
                 messagebox.showerror("Error","Client Name Must required",parent=self.root)
             else:
                 cur.execute("Select * from books where cname=?",(self.var_cname.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error","Invalid Client Name",parent=self.root)
                 else:
                     cur.execute("Update books set bname=?,language=?,online=?,paperback=?,ppress=?,quantity=?,packages=? where cname=?",(
                                         self.var_bname.get(),
                                         self.var_language.get(),
                                         self.txt_online.get('1.0',END),
                                         self.txt_paper.get('1.0',END),
                                         self.var_pname.get(),
                                         self.var_quantity.get(),
                                         self.var_packages.get(),
                                         self.var_cname.get(),   
                     ))
                     con.commit()
                     messagebox.showinfo("Success","Book Details Updated Successfully",parent=self.root)
                     self.show()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


       def delete(self):
          con=sqlite3.connect(database=r'pallpubb.db')
          cur=con.cursor()
          try:
               if self.var_cname.get()=="":
                 messagebox.showerror("Error","Client Name Must required",parent=self.root)
               else:
                 cur.execute("Select * from books where cname=?",(self.var_cname.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error","Invalid Client Name",parent=self.root)
                 else:
                     op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                     if op==True:
                         cur.execute("delete from books where cname=?",(self.var_cname.get(),))
                         con.commit()
                         messagebox.showinfo("Delete","Customer Deleted Successfully",parent=self.root)
                         self.clear()
             
          except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

       def clear(self):
          self.var_cname.set("")
          self.var_bname.set("")
          self.var_language.set("")
          self.txt_online.delete('1.0',END)
          self.txt_paper.delete('1.0',END)
          self.var_pname.set("")
          self.var_quantity.set("")
          self.var_packages.set("")
          self.var_searchtxt.set("")
          self.var_searchby.set("Select")
          self.show()

       def search(self):
          con=sqlite3.connect(database=r'pallpubb.db')
          cur=con.cursor()
          try:
               if self.var_searchby.get()=="Select":
                    messagebox.showerror("Error","Select Search By option",parent=self.root)
               elif self.var_searchtxt.get()=="":
                    messagebox.showerror("Error","Select input should be required",parent=self.root)
               else:
                    cur.execute("select * from books where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                    rows=cur.fetchall()
                    if len(rows)!=0:
                         self.BooksTable.delete(*self.BooksTable.get_children())
                         for row in rows:
                              self.BooksTable.insert('',END,values=row)
                    else:
                         messagebox.showerror("Error","No Record Found",parent=self.root)

          except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
       

       def close_window(self):
           self.root.destroy()

     

if __name__=="__main__":
    root=Tk()
    obj=BookClass(root)
    root.mainloop()#.mainloop is used to keep the software gui stable on window.
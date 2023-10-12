from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
class DataClass:
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
              self.var_name=StringVar()
              self.var_age=StringVar()
              self.var_contact=StringVar()
              self.var_address=StringVar()
              self.var_occupation=StringVar()
              self.var_insta=StringVar()
              self.var_facebook=StringVar()
              self.var_other=StringVar()


              lbl_title=Label(root,text="DATA")
              lbl_title.config(font=('Helvetica bold', 60,"bold"),bg="#769ADD",fg="#FFFFFF")
              lbl_title.place(x=580,y=0)
              lbl_title.pack(fill=X)
    
              SearchFrame=LabelFrame(self.root,text="Search Name or Contact No", bg="#324370", fg="#FFFFFF", font=("Calibri",12,"bold"),bd=2,relief=RIDGE)
              SearchFrame.place(x=500,y=150,width=600,height=70)
       #-------------combobox----------------------------------------------------------------
              cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","name","contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
              cmb_search.place(x=10,y=10,width=180)
              cmb_search.current(0)

       #----------------Content ------------------------------------------------------------

              txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("",15),bg="white").place(x=200,y=10)
              btn_search=Button(SearchFrame, text="Search",font=("",15),bg="#769ADD",fg="white",activebackground="#769ADD",activeforeground="White",cursor="hand2",command=self.search).place(x=440,y=9,width=150,height=30)
      
      #============Row 1=================
              lbl_name=Label(self.root,text="Name",font=("",16),bg="#324370",fg="white").place(x=340,y=245)
              lbl_occupation=Label(self.root,text="Occupation",font=("",15),bg="#324370",fg="white").place(x=870,y=250)
       
              txt_name=Entry(self.root,textvariable=self.var_name,font=("",12),bg="#FFFFFF",fg="black").place(x=410,y=250,width=230,height=25)
              txt_occupation=Entry(self.root,textvariable=self.var_occupation,font=("",12),bg="#FFFFFF",fg="black").place(x=1000,y=250,width=230,height=25)
       
       #============Row 2=====================
              lbl_age=Label(self.root,text="Age",font=("",16),bg="#324370",fg="white").place(x=340,y=295)
              lbl_insta=Label(self.root,text="Instagram ID",font=("",15),bg="#324370",fg="white").place(x=860,y=295)
       
              txt_age=Entry(self.root,textvariable=self.var_age,font=("",12),bg="#FFFFFF",fg="black").place(x=410,y=300,width=230,height=25)
              txt_insta=Entry(self.root,textvariable=self.var_insta,font=("",12),fg="black").place(x=1000,y=300,width=230,height=25)

       #============Row 3=======================
              lbl_contact=Label(self.root,text="Contact",font=("",15),bg="#324370",fg="white").place(x=320,y=345)
              lbl_facebook=Label(self.root,text="Facebook ID",font=("",15),bg="#324370",fg="white").place(x=860,y=345)
       
              txt_contact=Entry(self.root,textvariable=self.var_contact,font=("",12),bg="#FFFFFF",fg="black").place(x=410,y=350,width=230,height=25)
              txt_facebook=Entry(self.root,textvariable=self.var_facebook,font=("",12),bg="#FFFFFF",fg="black").place(x=1000,y=350,width=230,height=25)
              

       #============Row 4=========================
              lbl_address=Label(self.root,text="Address",font=("",15),bg="#324370",fg="white").place(x=320,y=395)
              lbl_other=Label(self.root,text="Other link",font=("",15),bg="#324370",fg="white").place(x=870,y=395)
       
              self.txt_address=Text(self.root,font=("",11),bg="white")
              self.txt_address.place(x=410,y=400, width=300, height= 65)
              txt_other=Entry(self.root,textvariable=self.var_other,font=("",12),bg="#FFFFFF",fg="black").place(x=1000,y=395,width=230,height=25)


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

              data_frame=Frame(self.root,bd=3,relief=RIDGE)
              data_frame.place(x=0,y=520,relwidth=1,height=260,width=-10)

              scrolly=Scrollbar(data_frame,orient=VERTICAL)
              scrolly.config(width=20)
              scrollx=Scrollbar(data_frame,orient=HORIZONTAL)

              self.DataTable=ttk.Treeview(data_frame,columns=("name","age","contact","address","occupation","insta","facebook","other"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
              scrollx.pack(side=BOTTOM,fill=X)
              scrolly.pack(side=RIGHT,fill=Y)
              scrollx.config(command=self.DataTable.xview)
              scrolly.config(command=self.DataTable.yview)
              self.DataTable.heading("name",text="Name")
              self.DataTable.heading("age",text="Age")
              self.DataTable.heading("contact",text="Contact")
              self.DataTable.heading("address",text="Address")
              self.DataTable.heading("occupation",text="Occupation")
              self.DataTable.heading("insta",text="Instagram")
              self.DataTable.heading("facebook",text="Facebook")
              self.DataTable.heading("other",text="Other")
       
              self.DataTable["show"]="headings"

              self.DataTable.column("name",width=90)
              self.DataTable.column("age",width=100)
              self.DataTable.column("contact",width=100)
              self.DataTable.column("address",width=100)
              self.DataTable.column("occupation",width=100)
              self.DataTable.column("insta",width=100)
              self.DataTable.column("facebook",width=100)
              self.DataTable.column("other",width=100)
              self.DataTable.pack(fill=BOTH,expand=1)
              self.DataTable.bind("<ButtonRelease-1>",self.get_data)

              self.show()

#===============================================================================================

       def add(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             if self.var_name.get()=="":
                 messagebox.showerror("Error","Name Must required",parent=self.root)
             else:
                 cur.execute("Select * from data where name=?",(self.var_name.get(),))
                 row=cur.fetchone()

                 cur.execute("Insert into data (name,age,contact,address,occupation,insta,facebook,other) values(?,?,?,?,?,?,?,?)",(
                                         self.var_name.get(),
                                         self.var_age.get(),
                                         self.var_contact.get(),
                                         self.txt_address.get('1.0',END),
                                         self.var_occupation.get(),
                                         self.var_insta.get(),
                                         self.var_facebook.get(),
                                         self.var_other.get(),   
                 ))
                 con.commit()
                 messagebox.showinfo("Success","Data Added Successfully",parent=self.root)
                 self.show()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


       def show(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             cur.execute("select * from data")
             rows=cur.fetchall()
             self.DataTable.delete(*self.DataTable.get_children())
             for row in rows:
                 self.DataTable.insert('',END,values=row)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

       def get_data(self,ev):
         f=self.DataTable.focus()
         content=(self.DataTable.item(f))
         row=content['values']
         self.var_name.set(row[0])
         self.var_age.set(row[1])
         self.var_contact.set(row[2])
         self.txt_address.delete('1.0',END)
         self.txt_address.insert(END,row[3])
         self.var_occupation.set(row[4])
         self.var_insta.set(row[5])
         self.var_facebook.set(row[6])
         self.var_other.set(row[7])


       def update(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             if self.var_name.get()=="":
                 messagebox.showerror("Error","Name Must required",parent=self.root)
             else:
                 cur.execute("Select * from data where name=?",(self.var_name.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error","Invalid Name",parent=self.root)
                 else:
                     cur.execute("Update data set age=?,contact=?,address=?,occupation=?,insta=?,facebook=?,other=? where name=?",(
                                         self.var_age.get(),
                                         self.var_contact.get(),
                                         self.txt_address.get('1.0',END),
                                         self.var_occupation.get(),
                                         self.var_insta.get(),
                                         self.var_facebook.get(),
                                         self.var_other.get(),
                                         self.var_name.get(),   
                     ))
                     con.commit()
                     messagebox.showinfo("Success","Updated Successfully",parent=self.root)
                     self.show()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


       def delete(self):
          con=sqlite3.connect(database=r'pallpubb.db')
          cur=con.cursor()
          try:
               if self.var_name.get()=="":
                 messagebox.showerror("Error","Name Must required",parent=self.root)
               else:
                 cur.execute("Select * from data where name=?",(self.var_name.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error","Invalid Name",parent=self.root)
                 else:
                     op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                     if op==True:
                         cur.execute("delete from data where name=?",(self.var_name.get(),))
                         con.commit()
                         messagebox.showinfo("Delete","Deleted Successfully",parent=self.root)
                         self.clear()
             
          except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

       def clear(self):
          self.var_name.set("")
          self.var_age.set("")
          self.var_contact.set("")
          self.txt_address.delete('1.0',END)
          self.var_occupation.set("")
          self.var_insta.set("")
          self.var_facebook.set("")
          self.var_other.set("")
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
                    cur.execute("select * from data where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                    rows=cur.fetchall()
                    if len(rows)!=0:
                         self.DataTable.delete(*self.DataTable.get_children())
                         for row in rows:
                              self.DataTable.insert('',END,values=row)
                    else:
                         messagebox.showerror("Error","No Record Found",parent=self.root)

          except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
       

       def close_window(self):
           self.root.destroy()

     

if __name__=="__main__":
    root=Tk()
    obj=DataClass(root)
    root.mainloop()#.mainloop is used to keep the software gui stable on window.
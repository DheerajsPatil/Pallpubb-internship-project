from tkinter import *
from tkinter import ttk,messagebox
from tkinter import filedialog
import sqlite3
class studentClass:
    def __init__(self,root):
        self.root=root
        self.root.iconbitmap('my office logo.ico')
        self.root.title("PALLPUBB")#.title is used to title a software
        self.root.geometry("1535x780+0+0")#.geometry is used to set the height,weidth, and x,y axis of gui.
        #self.root.resizable(False,False)#.resizable is used to restrict user from expanding gui window, it set default.
        self.root.config(bg="#324370")#.config is used to configure the gui by changing its color,text,etc.
        self.back_button =Button(self.root, text="Back",font=("Helvetica bold",12,"bold"), bg="#769ADD", fg="white",activebackground="#769ADD",activeforeground="White", width=8,height=1,command=self.close_window)
        self.back_button.place(x=30, y=120)

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_student=StringVar()
        self.var_school=StringVar()
        self.var_contact=StringVar()

        lbl_title=Label(root,text="STUDENT")
        lbl_title.config(font=('Helvetica bold', 60,"bold"),bg="#769ADD",fg="#FFFFFF")
        lbl_title.place(x=580,y=0)
        lbl_title.pack(fill=X)
        #=============Back Button=======================#
       #----------------------Search Frame------------------------------------------------------------#
        SearchFrame=LabelFrame(self.root,text="Search Student Name or  School Name", bg="#324370", fg="#FFFFFF", font=("Calibri",12,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=500,y=150,width=600,height=70)
       #-------------combobox----------------------------------------------------------------
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Stuname","Schname"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("",15),bg="white").place(x=200,y=10)
        btn_search=Button(SearchFrame, text="Search",font=("",15),bg="#769ADD",fg="white",activebackground="#769ADD",activeforeground="White",cursor="hand2",command=self.search).place(x=440,y=9,width=150,height=30)

        studentn_lbl=Label(self.root,text="Student Name",font=("",16,"bold"),bg="#324370",fg="#FFFFFF").place(x=350,y=250)
        studentn_Entry=Entry(self.root,textvariable=self.var_student,font=("",12),fg="black",bd=5,relief=GROOVE).place(x=510,y=250)
        
        schooln_lbl=Label(self.root,text="School Name",font=("",16,"bold"),bg="#324370",fg="#FFFFFF").place(x=350,y=320)
        schooln_Entry=Entry(self.root,textvariable=self.var_school,font=("",12),fg="black",bd=5,relief=GROOVE).place(x=510,y=320)
        
        contact_lbl=Label(self.root,text="Contact",font=("",16,"bold"),bg="#324370",fg="#FFFFFF").place(x=780,y=250)
        contact_Entry=Entry(self.root,textvariable=self.var_contact,font=("",12),fg="black",bd=5,relief=GROOVE).place(x=880,y=250)

        lbl_address=Label(self.root,text="Address",font=("",15,"bold"),bg="#324370",fg="white").place(x=780,y=320)
        self.txt_address=Text(self.root,font=("",11),bg="white")
        self.txt_address.place(x=880,y=320, width=300, height= 60)
        
        btn_save=Button(root,text="Save")
        btn_save.config(font=('Helvetica bold', 14,"bold"),bg="#769ADD",fg="white",activebackground="#769ADD",activeforeground="White",width=10,command=self.add)
        btn_save.place(x=730,y=420)
        
        btn_clearall=Button(root,text="ClearAll")
        btn_clearall.config(font=('Helvetica bold', 12,"bold"),bg="WHITE",fg="BLACK",width=10,command=self.clear)
        btn_clearall.place(x=1280,y=420)

        btn_delete=Button(root,text="Delete")
        btn_delete.config(font=('Helvetica bold', 12,"bold"),bg="WHITE",fg="BLACK",width=10,command=self.delete)
        btn_delete.place(x=1400,y=420)

        btn_edit=Button(root,text="Update")
        btn_edit.config(font=('Helvetica bold', 12,"bold"),bg="WHITE",fg="BLACK",width=10,command=self.update)
        btn_edit.place(x=1160,y=420)


        student_frame=Frame(self.root,bd=3,relief=RIDGE)
        student_frame.place(x=280,y=520,relwidth=1,height=260,width=-500)

        scrolly=Scrollbar(student_frame,orient=VERTICAL)
        scrollx=Scrollbar(student_frame,orient=HORIZONTAL)

        self.StudentTable=ttk.Treeview(student_frame,columns=("stuname","schname","contact","address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.StudentTable.xview)
        scrolly.config(command=self.StudentTable.yview)
        self.StudentTable.heading("stuname",text="Student Name")
        self.StudentTable.heading("schname",text="School Name")
        self.StudentTable.heading("contact",text="Contact")
        self.StudentTable.heading("address",text="Address")

        self.StudentTable["show"]="headings"

        self.StudentTable.column("stuname",width=90)
        self.StudentTable.column("schname",width=100)
        self.StudentTable.column("contact",width=100)
        self.StudentTable.column("address",width=100)
        self.StudentTable.pack(fill=BOTH,expand=1)
        self.StudentTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#===================================================================================

    def add(self):
        con=sqlite3.connect(database=r'pallpubb.db')
        cur=con.cursor()
        try:
            if self.var_student.get()=="":
                messagebox.showerror("Error","All Fields Must be Required",parent=self.root)
            else:
                cur.execute("Select * from students where stuname=?",(self.var_student.get(),))
                row=cur.fetchone()
                cur.execute("Insert into students (stuname,schname,contact,address) values(?,?,?,?)",(
                                        self.var_student.get(),
                                        self.var_school.get(),
                                        self.var_contact.get(),
                                        self.txt_address.get('1.0',END),                 
                ))
                con.commit()
                messagebox.showinfo("Success","Inserted Successfully",parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             cur.execute("Select * from students")
             rows=cur.fetchall()
             self.StudentTable.delete(*self.StudentTable.get_children())
             for row in rows:
                 self.StudentTable.insert('',END,values=row)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.StudentTable.focus()
        content=(self.StudentTable.item(f))
        row=content['values']
        #print(row)
        self.var_student.set(row[0])
        self.var_school.set(row[1])
        self.var_contact.set(row[2])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[3])

    def update(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             if self.var_student.get()=="":
                 messagebox.showerror("Error","Student Name Must required",parent=self.root)
             else:
                 cur.execute("Select * from students where stuname=?",(self.var_student.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error","Invalid student ID",parent=self.root)
                 else:
                     cur.execute("Update students set schname=?,contact=?,address=? where stuname=?",(
                                        self.var_school.get(),
                                        self.var_contact.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_student.get(),   
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
               if self.var_student.get()=="":
                 messagebox.showerror("Error","Student Name Must required",parent=self.root)
               else:
                 cur.execute("Select * from students where stuname=?",(self.var_student.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error","Invalid Student Name",parent=self.root)
                 else:
                     op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                     if op==True:
                         cur.execute("delete from students where stuname=?",(self.var_student.get(),))
                         con.commit()
                         messagebox.showinfo("Delete","Deleted Successfully",parent=self.root)
                         self.clear()
             
          except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
          self.var_student.set("")
          self.var_school.set("")
          self.var_contact.set("")
          self.txt_address.delete('1.0',END)
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
                    cur.execute("Select * from students where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                    rows=cur.fetchall()
                    if len(rows)!=0:
                         self.StudentTable.delete(*self.StudentTable.get_children())
                         for row in rows:
                              self.StudentTable.insert('',END,values=row)
                    else:
                         messagebox.showerror("Error","No Record Found",parent=self.root)

          except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    
    
        
    def close_window(self):
        self.root.destroy()





if __name__=="__main__":
    root=Tk()
    obj=studentClass(root)
    root.mainloop()#.mainloop is used to keep the software gui stable on window.
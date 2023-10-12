from tkinter import *
from tkinter import ttk,messagebox
from tkinter import filedialog
import sqlite3
class SchoolClass:
     def __init__(self,root):
       self.root=root
       self.root.iconbitmap('my office logo.ico')
       self.root.title("PALLPUBB")#.title is used to title a software
       self.root.geometry("1535x780+0+0")#.geometry is used to set the height,weidth, and x,y axis of gui.
       #self.root.resizable(False,False)#.resizable is used to restrict user from expanding gui window, it set default.
       self.root.config(bg="#324370")#.config is used to configure the gui by changing its color,text,etc.
       self.btn_back =Button(self.root, text="Back",font=("Helvetica bold",12,"bold"), bg="#769ADD", fg="white", width=8,height=1,activebackground="#769ADD",activeforeground="White",command=self.close_window)
       self.btn_back.place(x=30, y=120)
       self.root.focus_force()



       self.var_searchby=StringVar()
       self.var_searchtxt=StringVar()
       self.var_sname=StringVar()
       self.var_pname=StringVar()
       self.var_date=StringVar()
       self.var_seid=StringVar()
       self.var_cpname=StringVar()
       self.var_cpid=StringVar()
       self.var_instaid=StringVar()
       self.var_facebookid=StringVar()

       lbl_title=Label(root,text="SCHOOL")
       lbl_title.config(font=('Helvetica bold', 60,"bold"),bg="#769ADD",fg="#FFFFFF")
       lbl_title.place(x=580,y=0)
       lbl_title.pack(fill=X)
    
       SearchFrame=LabelFrame(self.root,text="Search School Name or Contact Person Name", bg="#324370", fg="#FFFFFF", font=("Calibri",12,"bold"),bd=2,relief=RIDGE)
       SearchFrame.place(x=500,y=120,width=600,height=70)
       #-------------combobox----------------------------------------------------------------
       cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","sname","cpname"),state='readonly',justify=CENTER,font=("goudy old style",15))
       cmb_search.place(x=10,y=10,width=180)
       cmb_search.current(0)

       #----------------Content ------------------------------------------------------------

       txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("",15),bg="white").place(x=200,y=10)
       btn_search=Button(SearchFrame, text="Search",font=("",15),bg="#769ADD",fg="white",activebackground="#769ADD",activeforeground="White",cursor="hand2",command=self.search).place(x=440,y=9,width=150,height=30)
      
      #============Row 1=================
       lbl_sname=Label(self.root,text="School Name",font=("",15),bg="#324370",fg="white").place(x=130,y=220)
       lbl_doj=Label(self.root,text="DOJ [d/m/y]",font=("",15),bg="#324370",fg="white").place(x=550,y=220)
       lbl_cpname=Label(self.root,text="Contact Person Name",font=("",15),bg="#324370",fg="white").place(x=950,y=220)

       txt_sname=Entry(self.root,textvariable=self.var_sname,font=("",12),bg="#FFFFFF",fg="black").place(x=280,y=220,width=230,height=27)
       txt_doj=Entry(self.root,textvariable=self.var_date,font=("",12),bg="#FFFFFF",fg="black").place(x=700,y=220,width=230,height=27)
       txt_cpname=Entry(self.root,textvariable=self.var_cpname,font=("",12),bg="#FFFFFF",fg="black").place(x=1170,y=220,width=230,height=27)
       
       #============Row 2=====================
       lbl_pname=Label(self.root,text="Principal Name",font=("",15),bg="#324370",fg="white").place(x=130,y=280)
       lbl_seid=Label(self.root,text="School Mail ID",font=("",15),bg="#324370",fg="white").place(x=550,y=280)
       lbl_instaid=Label(self.root,text="Instagram ID",font=("",15),bg="#324370",fg="white").place(x=980,y=280)

       txt_pname=Entry(self.root,textvariable=self.var_pname,font=("",12),bg="#FFFFFF",fg="black").place(x=280,y=280,width=230,height=27)
       txt_seid=Entry(self.root,textvariable=self.var_seid,font=("",12),bg="#FFFFFF",fg="black").place(x=700,y=280,width=230,height=27)
       txt_instaid=Entry(self.root,textvariable=self.var_instaid,font=("",12),bg="#FFFFFF",fg="black").place(x=1170,y=280,width=230,height=27)
       #============Row 3=======================
       lbl_address=Label(self.root,text="Address",font=("",15),bg="#324370",fg="white").place(x=130,y=340)
       lbl_cpid=Label(self.root,text="Contact Person \n Mail ID",font=("",15),bg="#324370",fg="white").place(x=550,y=340)
       lbl_facebookid=Label(self.root,text="Facebook ID",font=("",15),bg="#324370",fg="white").place(x=980,y=340)

       self.txt_address=Text(self.root,font=("",11),bg="white")
       self.txt_address.place(x=230,y=340, width=280, height= 60)
       txt_cpid=Entry(self.root,textvariable=self.var_cpid,font=("",12),bg="#FFFFFF",fg="black").place(x=700,y=340,width=230,height=27)
       txt_facebookid=Entry(self.root,textvariable=self.var_facebookid,font=("",12),bg="#FFFFFF",fg="black").place(x=1170,y=340,width=230,height=25)
       #============Row 4========================

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


#==================school Details====================================================

       school_frame=Frame(self.root,bd=3,relief=RIDGE)
       school_frame.place(x=0,y=520,relwidth=1,height=260,width=-10)

       scrolly=Scrollbar(school_frame,orient=VERTICAL)
       scrolly.config(width=20)
       scrollx=Scrollbar(school_frame,orient=HORIZONTAL)

       self.SchoolTable=ttk.Treeview(school_frame,columns=("sname","pname","address","doj","seid","cpid","cpname","instaid","facebookid"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)
       scrollx.config(command=self.SchoolTable.xview)
       scrolly.config(command=self.SchoolTable.yview)
       self.SchoolTable.heading("sname",text="School Name")
       self.SchoolTable.heading("pname",text="Principal Name")
       self.SchoolTable.heading("address",text="Address")
       self.SchoolTable.heading("doj",text="Date of joining")
       self.SchoolTable.heading("seid",text="School Mail ID")
       self.SchoolTable.heading("cpid",text="Contact Person Mail ID")
       self.SchoolTable.heading("cpname",text="Contact Person Name")
       self.SchoolTable.heading("instaid",text="Instagram ID")
       self.SchoolTable.heading("facebookid",text="Facebook ID")

       
       self.SchoolTable["show"]="headings"

       self.SchoolTable.column("sname",width=90)
       self.SchoolTable.column("pname",width=100)
       self.SchoolTable.column("address",width=100)
       self.SchoolTable.column("doj",width=100)
       self.SchoolTable.column("seid",width=100)
       self.SchoolTable.column("cpid",width=100)
       self.SchoolTable.column("cpname",width=100)
       self.SchoolTable.column("instaid",width=100)
       self.SchoolTable.column("facebookid",width=100)
       self.SchoolTable.pack(fill=BOTH,expand=1)
       self.SchoolTable.bind("<ButtonRelease-1>",self.get_data)

       self.show()

#===============================================================================================
     def add(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             if self.var_sname.get()=="":
                 messagebox.showerror("Error","School Name Must required",parent=self.root)
             else:
                 cur.execute("Select * from schools where sname=?",(self.var_sname.get(),))
                 row=cur.fetchone()
                 cur.execute("Insert into schools (sname,pname,address,doj,seid,cpid,cpname,instaid,facebookid) values(?,?,?,?,?,?,?,?,?)",(
                                   self.var_sname.get(),
                                   self.var_pname.get(),
                                   self.txt_address.get('1.0',END),
                                   self.var_date.get(),
                                   self.var_seid.get(),
                                   self.var_cpid.get(),
                                   self.var_cpname.get(),
                                   self.var_instaid.get(),
                                   self.var_facebookid.get(),   
                 ))
                 con.commit()
                 messagebox.showinfo("Success","schools Added Successfully",parent=self.root)
                 self.show()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

     def show(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             cur.execute("select * from schools")
             rows=cur.fetchall()
             self.SchoolTable.delete(*self.SchoolTable.get_children())
             for row in rows:
                 self.SchoolTable.insert('',END,values=row)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
         

     def get_data(self,ev):
         f=self.SchoolTable.focus()
         content=(self.SchoolTable.item(f))
         row=content['values']
         #print(row)
         self.var_sname.set(row[0])
         self.var_pname.set(row[1])
         self.txt_address.delete('1.0',END)
         self.txt_address.insert(END,row[2])
         self.var_date.set(row[3])
         self.var_seid.set(row[4])
         self.var_cpid.set(row[5])
         self.var_cpname.set(row[6])
         self.var_instaid.set(row[7])
         self.var_facebookid.set(row[8])

     def update(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             if self.var_sname.get()=="":
                 messagebox.showerror("Error","School Name Must required",parent=self.root)
             else:
                 cur.execute("Select * from schools where sname=?",(self.var_sname.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error","Invalid School Name",parent=self.root)
                 else:
                     cur.execute("Update schools set pname=?, address=?, doj=?, seid=?, cpid=?, cpname=?, instaid=?, facebookid=? where sname=?",(
                                         self.var_pname.get(),
                                         self.txt_address.get('1.0',END),
                                         self.var_date.get(),
                                         self.var_seid.get(),
                                         self.var_cpid.get(),
                                         self.var_cpname.get(),
                                         self.var_instaid.get(),
                                         self.var_facebookid.get(), 
                                         self.var_sname.get(),  
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
               if self.var_sname.get()=="":
                 messagebox.showerror("Error","School Name Must required",parent=self.root)
               else:
                 cur.execute("Select * from schools where sname=?",(self.var_sname.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error","Invalid School Name",parent=self.root)
                 else:
                     op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                     if op==True:
                         cur.execute("delete from schools where sname=?",(self.var_sname.get(),))
                         con.commit()
                         messagebox.showinfo("Delete","School Deleted Successfully",parent=self.root)
                         self.clear()
             
          except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


     def clear(self):
          self.var_sname.set("")
          self.var_pname.set("")
          self.txt_address.delete('1.0',END)
          self.var_date.set("")
          self.var_seid.set("")
          self.var_cpid.set("")
          self.var_cpname.set("")
          self.var_instaid.set("")
          self.var_facebookid.set("")
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
                    cur.execute("select * from schools where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                    rows=cur.fetchall()
                    if len(rows)!=0:
                         self.SchoolTable.delete(*self.SchoolTable.get_children())
                         for row in rows:
                              self.SchoolTable.insert('',END,values=row)
                    else:
                         messagebox.showerror("Error","No Record Found",parent=self.root)

          except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 
         

     def close_window(self):
           self.root.destroy()
     

if __name__=="__main__":
    root=Tk()
    obj=SchoolClass(root)
    root.mainloop()#.mainloop is used to keep the software gui stable on window.
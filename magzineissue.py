from tkinter import *
from tkinter import ttk,messagebox
from tkinter import filedialog
import sqlite3
class IssueClass:
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
        self.var_sr_no=StringVar()
        self.var_month=StringVar()
        self.var_year=StringVar()

        def openFile():
            filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Asus\\OneDrive\\Desktop\\Data",
                                          title="Open File",filetypes= (("Text files","*.txt"),("All Files","*.*")))
            file = open(filepath,'rt')
            print(file.read())
            file.close

        lbl_title=Label(root,text="ISSUE")
        lbl_title.config(font=('Helvetica bold', 60,"bold"),bg="#769ADD",fg="#FFFFFF")
        lbl_title.place(x=580,y=0)
        lbl_title.pack(fill=X)
        #=============Back Button=======================#
       #----------------------Search Frame------------------------------------------------------------#
        SearchFrame=LabelFrame(self.root,text="Search Month or Year", bg="#324370", fg="#FFFFFF", font=("Calibri",12,"bold"),bd=2,relief=RIDGE)
        SearchFrame.place(x=500,y=150,width=600,height=70)
       #-------------combobox----------------------------------------------------------------
        cmb_search=ttk.Combobox(SearchFrame,values=("Select","Month","Year"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,font=("",15),bg="white").place(x=200,y=10)
        btn_search=Button(SearchFrame, text="Search",font=("",15),bg="#769ADD",fg="white",activebackground="#769ADD",activeforeground="White",cursor="hand2").place(x=440,y=9,width=150,height=30)

        sr_no_lbl=Label(self.root,text="ISSUE ID",font=("",16,"bold"),bg="#324370",fg="#FFFFFF").place(x=610,y=250)
        sr_no_Entry=Entry(self.root,textvariable=self.var_sr_no,font=("",12),fg="black",bd=5,relief=GROOVE).place(x=720,y=250)
        
        month_lbl=Label(self.root,text="MONTH",font=("",16,"bold"),bg="#324370",fg="#FFFFFF").place(x=610,y=300)
        month_Entry=Entry(self.root,textvariable=self.var_month,font=("",12),fg="black",bd=5,relief=GROOVE).place(x=720,y=300)
        
        year_lbl=Label(self.root,text="YEAR",font=("",16,"bold"),bg="#324370",fg="#FFFFFF").place(x=610,y=350)
        year_Entry=Entry(self.root,textvariable=self.var_year,font=("",12),fg="black",bd=5,relief=GROOVE).place(x=720,y=350)
        
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


        issue_frame=Frame(self.root,bd=3,relief=RIDGE)
        issue_frame.place(x=440,y=520,relwidth=1,height=260,width=-800)

        scrolly=Scrollbar(issue_frame,orient=VERTICAL)
        scrollx=Scrollbar(issue_frame,orient=HORIZONTAL)

        self.IssueTable=ttk.Treeview(issue_frame,columns=("cid","month","year"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.IssueTable.xview)
        scrolly.config(command=self.IssueTable.yview)
        self.IssueTable.heading("cid",text="ISSUE ID")
        self.IssueTable.heading("month",text="MONTH")
        self.IssueTable.heading("year",text="YEAR")

        self.IssueTable["show"]="headings"

        self.IssueTable.column("cid",width=90)
        self.IssueTable.column("month",width=100)
        self.IssueTable.column("year",width=100)
        self.IssueTable.pack(fill=BOTH,expand=1)
        self.IssueTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#===================================================================================

    def add(self):
        con=sqlite3.connect(database=r'pallpubb.db')
        cur=con.cursor()
        try:
            if self.var_sr_no.get()=="":
                messagebox.showerror("Error","All Fields Must be Required",parent=self.root)
            else:
                cur.execute("Select * from issue where cid=?",(self.var_sr_no.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This ID is already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into issue (cid,month,year) values(?,?,?)",(
                                        self.var_sr_no.get(),
                                        self.var_month.get(),
                                        self.var_year.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Issued Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             cur.execute("Select * from issue")
             rows=cur.fetchall()
             self.IssueTable.delete(*self.IssueTable.get_children())
             for row in rows:
                 self.IssueTable.insert('',END,values=row)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.IssueTable.focus()
        content=(self.IssueTable.item(f))
        row=content['values']
        #print(row)
        self.var_sr_no.set(row[0])
        self.var_month.set(row[1])
        self.var_year.set(row[2])

    def update(self):
         con=sqlite3.connect(database=r'pallpubb.db')
         cur=con.cursor()
         try:
             if self.var_sr_no.get()=="":
                 messagebox.showerror("Error","All Fields Must required",parent=self.root)
             else:
                 cur.execute("Select * from issue where cid=?",(self.var_sr_no.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error","Invalid Issue ID",parent=self.root)
                 else:
                     cur.execute("Update issue set month=?,year=? where cid=?",(
                                        self.var_month.get(),
                                        self.var_year.get(),
                                        self.var_sr_no.get(),   
                     ))
                     con.commit()
                     messagebox.showinfo("Success","Issue Updated Successfully",parent=self.root)
                     self.show()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
          con=sqlite3.connect(database=r'pallpubb.db')
          cur=con.cursor()
          try:
               if self.var_sr_no.get()=="":
                 messagebox.showerror("Error","Issue ID Must required",parent=self.root)
               else:
                 cur.execute("Select * from issue where cid=?",(self.var_sr_no.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error","Invalid Issue ID",parent=self.root)
                 else:
                     op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                     if op==True:
                         cur.execute("delete from issue where cid=?",(self.var_sr_no.get(),))
                         con.commit()
                         messagebox.showinfo("Delete","Issue Deleted Successfully",parent=self.root)
                         self.clear()
             
          except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
          self.var_sr_no.set("")
          self.var_month.set("")
          self.var_year.set("")
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
                    cur.execute("Select * from issue where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                    rows=cur.fetchall()
                    if len(rows)!=0:
                         self.IssueTable.delete(*self.IssueTable.get_children())
                         for row in rows:
                              self.IssueTable.insert('',END,values=row)
                    else:
                         messagebox.showerror("Error","No Record Found",parent=self.root)

          except Exception as ex:
             messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    
    
        
    def close_window(self):
        self.root.destroy()





if __name__=="__main__":
    root=Tk()
    obj=IssueClass(root)
    root.mainloop()#.mainloop is used to keep the software gui stable on window.
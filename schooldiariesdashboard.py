from tkinter import *
from studentdiaries import studentClass
from schooldiaries import SchoolClass
class diaries:
    def __init__(self,root):
        self.root=root
        self.root.iconbitmap('my office logo.ico')
        self.root.title("PALLPUBB")#.title is used to title a software
        self.root.geometry("1920x780+0+0")#.geometry is used to set the height,weidth, and x,y axis of gui.
        self.root.config(bg="#324370")#.config is used to configure the gui by changing its color,text,etc.
        self.root.focus_force()

        lbl_title=Label(self.root,text="PALLPUBB")
        lbl_title.config(font=('Helvetica bold', 60,"bold"),bg="#769ADD",fg="#FFFFFF")
        lbl_title.place(x=580,y=0)
        lbl_title.pack(fill=X)

        # Create back button
        btn_back =Button(self.root, text="Back",font=("Helvetica bold",12,"bold"), bg="#769ADD", fg="white", width=8,height=1,activebackground="#769ADD",activeforeground="White",command=self.close_window)
        btn_back.place(x=30, y=120)
        # Create the rectangular box for The School Diaries
        pall_magzine_rectangle =Frame(self.root, bg="#2F4D99", width=3000, height=900,padx=5, pady=25) #padx=25, pady=25 # Increase width and height here
        pall_magzine_rectangle.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        # Create the label for The School Diaries
        lbl_my_scribble =Label(pall_magzine_rectangle, text="School Diaries", fg="#FFFFFF", bg="#2F4D99", font=("Helvetica", 35, "bold"))
        lbl_my_scribble.pack(pady=20)
        # Create the frame for buttons
        btn_frame =Frame(pall_magzine_rectangle, bg="#2F4D99")
        btn_frame.pack(padx=50,pady=30)
        # Create the Clients button
        btn_student =Button(btn_frame, text="STUDENT",font=("",16,"bold"),bg="#769ADD",fg="#FFFFFF",width=10,activebackground="#769ADD",activeforeground="White",command=self.Student)
        btn_student.pack(side=LEFT, padx=50)
        # Create the Issue button
        btn_school =Button(btn_frame, text="SCHOOL",font=("",16,"bold"),bg="#769ADD",fg="#FFFFFF",width=10,activebackground="#769ADD",activeforeground="White",command=self.School)
        btn_school.pack(side=RIGHT, padx=50)

    

    def Student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def School(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SchoolClass(self.new_win)

    def close_window(self):
        self.root.destroy()


if __name__=="__main__":
    root=Tk()
    obj=diaries(root)
    root.mainloop()#.mainloop is used to keep the software
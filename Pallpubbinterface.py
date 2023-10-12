from tkinter import*
from data import DataClass
from pallmagzine import Pallmagzine
from packagesinterface import Packages
from myfirstdashboard import scribble
from schooldiariesdashboard import diaries
class IMS:
    def __init__(self,root):
        self.root=root
        self.root=root
        self.root.iconbitmap('my office logo.ico')
        self.root.title("PALLPUBB")#.title is used to title a software
        self.root.config(bg="white")
        self.root.geometry("1920x780+0+0")#.geometry is used to set the height,weidth, and x,y axis of gui.
        self.root.focus_force()


        #self.icon_title=PhotoImage(file="images/image 1.png")
        title=Label(self.root,text="PALLPUBB",font=("times new roman",45,"bold"),bg="#38B6FF",fg="black",padx=20).place(x=0,y=0,relwidth=1,height=100)
#================Clock============================
        self.lbl_clock=Label(self.root,text="Welcome to PALLPUBB database software\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_clock.place(x=0,y=90,relwidth=1,height=20)

#================Left Menu=========================
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="#009688")
        LeftMenu.place(x=0,y=150,width=250,height=520)

        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20,"bold"),bg="#009688").pack(side=TOP,fill=X,pady=10)
        btn_data=Button(LeftMenu,text="Data",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",command=self.Data).pack(side=TOP,fill=X,pady=10)
        btn_pallmagzine=Button(LeftMenu,text="Pall Magzine",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",command=self.PallMagzine).pack(side=TOP,fill=X,pady=10)
        btn_myfscribble=Button(LeftMenu,text="My First Scribble",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",command=self.myfirstscribble).pack(side=TOP,fill=X,pady=10)
        btn_schooldiagries=Button(LeftMenu,text="School Diaries",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",command=self.schooldiaries).pack(side=TOP,fill=X,pady=10)
        btn_packages=Button(LeftMenu,text="Packages",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",command=self.Packages).pack(side=TOP,fill=X,pady=10)
        btn_exit=Button(LeftMenu,text="Exit",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",command=self.close_window).pack(side=TOP,fill=X,pady=10)

        lbl_footer=Label(self.root,text="PALLPUBB Founder : Sejal Patil | Contact : 9922168681/9096095885 \n Website : www.pallpubb.com",font=("times new roman",12),bg="#607d8b",fg="white").pack(side=BOTTOM,fill=X)

        self.lbl_data=Label(self.root,text="Data\n[0]",bd=5,relief=RIDGE,bg="#518AB8",fg="white",font=("times new roman",20,"bold"))
        self.lbl_data.place(x=370,y=170,height=150,width=300)

        self.lbl_pallmagzine=Label(self.root,text="PallMagzine\n[0]",bd=5,relief=RIDGE,bg="#e48585",fg="white",font=("times new roman",20,"bold"))
        self.lbl_pallmagzine.place(x=720,y=170,height=150,width=300)

        self.lbl_myfirstscribble=Label(self.root,text="My First Scribble\n[0]",bd=5,relief=RIDGE,bg="#244266",fg="white",font=("times new roman",20,"bold"))
        self.lbl_myfirstscribble.place(x=1100,y=170,height=150,width=300)

        self.lbl_schooldiaries=Label(self.root,text="School Diaries\n[0]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("times new roman",20,"bold"))
        self.lbl_schooldiaries.place(x=480,y=400,height=150,width=300)

        self.lbl_packages=Label(self.root,text="Packages\n[0]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("times new roman",20,"bold"))
        self.lbl_packages.place(x=850,y=400,height=150,width=300)

    def Data(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=DataClass(self.new_win)

    def PallMagzine(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Pallmagzine(self.new_win)

    def Packages(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Packages(self.new_win)

    def myfirstscribble(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=scribble(self.new_win)

    def schooldiaries(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=diaries(self.new_win)

    
    def close_window(self):
        self.root.destroy()



            

if __name__=="__main__":
     root=Tk()
     obj=IMS(root)
     root.mainloop()
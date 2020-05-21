from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
class login_page:
	def __init__(self,root):
		self.root=root
		self.root.title("Attendance System")
		self.root.geometry("1350x700+0+0")
		#self.root.configure(bg='white')

		self.bg_icon=ImageTk.PhotoImage(file="images/bg.jpg")
		self.user_icon=PhotoImage(file="images/user.png")
		self.pass_icon=PhotoImage(file="images/pass.png")
		self.logo_icon=PhotoImage(file="images/logo.png")
		

		self.uname=StringVar()
		self.pass_=StringVar()



		bg_lb1=Label(self.root,image=self.bg_icon).pack()
		
		title = Label(self.root,text="Login",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
		title.place(x=0,y=0,relwidth=1)

		Login_Frame=Frame(self.root,bg="white")
		Login_Frame.place(x=400,y=150)


		logolb1 = Label(Login_Frame,image=self.logo_icon,bg="white",bd=0).grid(row=0,columnspan=2,pady=20)
		
		lbl1user=Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
		txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("times new roman",15)).grid(row=1,column=1,padx=20)



		lbl1pass=Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
		txtpass=Entry(Login_Frame,bd=5,textvariable=self.pass_,relief=GROOVE,font=("times new roman",15)).grid(row=2,column=1,padx=20)	

		btn_log=Button(Login_Frame,text="Login",command=self.login,width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)		 

	def login(self):
		if self.uname.get()=="" or self.pass_.get()=="":
			messagebox.showerror("Error","All fields are required")


root=Tk()
obj=login_page(root)
root.mainloop()

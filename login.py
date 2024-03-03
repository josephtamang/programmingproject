from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
root =Tk()

root.maxsize(width=1520, height=900)
root.minsize(width=1520, height=900)
root.title("hospital Management System")
root.iconbitmap("signup.png")
root.config(bg='#CAA8F5')



 #photo
image_background=ImageTk.PhotoImage(Image.open('hospitals.png'))
label=Label(root,image=image_background)
label.place(x=0,y=0,width=800,height=600)


#frame
frame = LabelFrame(root,relief='raised',bg='#CAA8F5')
frame.place(x=800,y=80,width=450, height=580) 


#heading
login=Label(frame,text='Login',bg='#CAA8F5', font=("times new roman",24,"bold"))
login.place(x=190,y=20)



#label, place for the details
user_name=Label(frame,text='Username:',bg='#CAA8F5', font=("times new roman",16,"bold"))
user_name.place(x=70,y=170)
Password=Label(frame,text='Password:',bg='#CAA8F5', font=("times new roman",16,"bold"))
Password.place(x=70, y=260)



#entry of other details
entry_name=Entry(frame,width=50)
entry_name.place(x=70,y=210)         #for name
entry_password=Entry(frame, width=50,show='')       #show='' is used first when user type anything it shows  asterick(*) after clicking on the button only it shows password
entry_password.place(x=70, y=300)       #for password



#to show and not to show password
def add():
    if CheckVar1.get()==1:
        entry_password.config(show="")
    else:
        entry_password.config(show="*")
    
CheckVar1=IntVar()
c1 = Checkbutton(frame, text="Show password", bg='#CAA8F5',variable=CheckVar1, onvalue=1, offvalue=0, command=add)
c1.place(x=70, y=330)




#button for login
#to destroy the login and go to forget password
def home():
    if entry_name.get()=='' or entry_password.get()=='' :
        messagebox.showerror('Error!', 'Please fill up all the required details.')
    else:

        #to delete 
        entry_name.delete(0,END)
        entry_password.delete(0,END)

        messagebox.showinfo('success',"Successfully login!")

        #to destroy
        root.destroy()
        import homepage

login=Button(frame,text="LOGIN",fg='white', bg='white')#CAA8F5',relief='raised', font=("times new roman",15,"bold"),command=home)
login.place(x=180, y=450)


# forget password?
for_pass=Button(frame,text="Forget Passoword?",relief='raised')
for_pass.place(x=280, y=360)

#sign up
label_sign=Label(frame,text="Don't have an account?",bg='white')
label_sign.place(x=120,y=520)

sign_up=Button(frame,text="Sign up",relief='raised')
sign_up.place(x=275, y=520)


root.mainloop()


from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
win=Tk()
win.state('zoomed')
win.config(bg='white')
#function for button:
def pd():
    if e1.get()==""or e2.get()=="":
        messagebox.showerror('Error','All credentials required')
    else:
        con=mysql.connector.connect(host='localhost',username='root',password='@HMSproject1234',database='mydatabase')
        my_cursor=con.cursor()
        my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            nameoftablets.get(),
            ref.get(),
            dose.get(),
            nooftablets.get(),
            issuedate.get(),
            expdate.get(),
            dailydose.get(),
            sideeffect.get(),
            nameofpateint.get(),
            dob.get(),
            addressofpatient.get()
        ))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo('success','Succesfully recorded')
def fetch_data():
    con=mysql.connector.connect(host='localhost',username='root',password='@HMSproject1234',database='mydatabase')
    my_cursor=con.cursor()
    my_cursor.execute('select * from hospital')
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        table.delete(* table.get_children())
        for items in rows:
            table.insert('',END,values=items)
            con.commit()
        con.close()
def get_data(event=''):
    cursor_row=table.focus()
    data=table.item(cursor_row)
    row=data['values']
    nameoftablets.set(row[0])
    ref.set(row[1])
    dose.set(row[2])
    nooftablets.set(row[3])
    issuedate.set(row[4])
    expdate.set(row[5])
    dailydose.set(row[6])
    sideeffect.set(row[7])
    addressofpatient.set(row[8])
    dob.set(row[9])
    nameofpateint.set(row[10])
   
   

#function for prescribtion :
def pre():
    txt_frame.insert(END,'name of tablets:\t\t\t'+nameoftablets.get()+'\n')
    txt_frame.insert(END,'reference no:\t\t\t'+ref.get()+'\n')
    txt_frame.insert(END,'dose\t\t\t'+dose.get()+'\n')
    txt_frame.insert(END,'no.of tablets:\t\t\t'+nooftablets.get()+'\n')
    txt_frame.insert(END,'Issue date:\t\t\t'+issuedate.get()+'\n')
    txt_frame.insert(END,'Exp.date:\t\t\t'+expdate.get()+'\n')
    txt_frame.insert(END,'daily dose:\t\t\t'+dailydose.get()+'\n')
    txt_frame.insert(END,'side effect:\t\t\t'+sideeffect.get()+'\n')
    txt_frame.insert(END,'Blood pressure:\t\t\t'+bloodpressure.get()+'\n')
    txt_frame.insert(END,'Doctor name:\t\t\t'+doc.get()+'\n')
    txt_frame.insert(END,'medication:\t\t\t'+medication.get()+'\n')
    txt_frame.insert(END,'patient id:\t\t\t'+pateintid.get()+'\n')
    txt_frame.insert(END,'name of patient:\t\t\t'+nameofpateint.get()+'\n')
    txt_frame.insert(END,'DOB:\t\t\t'+dob.get()+'\n')
    txt_frame.insert(END,'patient address:\t\t\t'+addressofpatient.get()+'\n')

#function for delete btn:
def delete():
    con=mysql.connector.connect(host='localhost',username='root',password='@HMSproject1234',database='mydatabase')
    my_cursor=con.cursor()
    qry=('delete from hospital where refrence=%s')
    value=(ref.get(),)
    my_cursor.execute(qry,value)
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo('deleted','Successfully deleted')

#function for clear btn:
def clr():
    nameoftablets.set('')
    ref.set('')
    dose.set('')
    nooftablets.set('')
    issuedate.set('')
    expdate.set('')
    dailydose.set('')
    doc.set('')
    bloodpressure.set('')
    sideeffect.set('')
    medication.set('')
    pateintid.set('')
    dob.set('')
    nameofpateint.set('')
    addressofpatient.set('')
    txt_frame.delete(1.0,END)
    messagebox.showinfo('clear','Successfully cleared')

#function for exit btn:
def exit():
    confirm=messagebox.askyesno('confirmation','Are sure you want to exit')
    if confirm>0:
        win.destroy()
        return

#heading
Label(win,text='Hospital Managemet System',font='impack 31 bold',bg='red',fg='white').pack(fill=X)
#frame1
f1=Frame(win,bd=15,relief=RIDGE)
f1.place(x=0,y=50,width=1300,height=410)
#label frame for patient info
lf1=LabelFrame(f1,text="Patient Information",font='ariel 10 bold',bd=10,bg='skyblue')
lf1.place(x=10,y=0,width=700,height=400)
#label frame for prescription
lf2=LabelFrame(f1,text="Prescription",font='ariel 12 bold',bd=10)
lf2.place(x=730,y=0,width=500,height=390)
#Textbox for prescription
txt_frame=Text(lf2,font='impack 10 bold',width=90,height=40,bg='yellow')
txt_frame.pack(fill=BOTH)
               


#label for patient info
Label(lf1,text='Name of Tablets',bg='skyblue').place(x=4,y=10)
Label(lf1,text='Reference No.',bg='skyblue').place(x=5,y=50)
Label(lf1,text='Dose',bg='skyblue').place(x=5,y=90)
Label(lf1,text='Issue Date',bg='skyblue').place(x=5,y=140)
Label(lf1,text='Exp. Date',bg='skyblue').place(x=5,y=180)
Label(lf1,text='Daily Dose',bg='skyblue').place(x=5,y=220)
Label(lf1,text='Side Effect',bg='skyblue').place(x=5,y=260)
Label(lf1,text='Blood Pressure',bg='skyblue').place(x=5,y=300)
Label(lf1,text='Doctor Name',bg='skyblue').place(x=350,y=10)
Label(lf1,text='No of tablets',bg='skyblue').place(x=350,y=60)
Label(lf1,text='Medication',bg='skyblue').place(x=350,y=110)
Label(lf1,text='Patient id.',bg='skyblue').place(x=350,y=160)
Label(lf1,text='Name of Patient',bg='skyblue').place(x=350,y=210)
Label(lf1,text='DOB',bg='skyblue').place(x=350,y=260)
Label(lf1,text='Patient Addresss',bg='skyblue').place(x=350,y=300)

#textvariable for all widget:
nameoftablets=StringVar()
ref=StringVar()
dose=StringVar()
nooftablets=StringVar()
issuedate=StringVar()
expdate=StringVar()
dailydose=StringVar()
sideeffect=StringVar()
bloodpressure=StringVar()
doc=StringVar()
medication=StringVar()
pateintid=StringVar()
nameofpateint=StringVar()
dob=StringVar()
addressofpatient=StringVar()


#entry field for all label
e1=Entry(lf1,bd=4,textvariable=nameoftablets)
e1.place(x=130,y=10,width=200)
e2=Entry(lf1,bd=4,textvariable=ref)
e2.place(x=130,y=50,width=200)
e3=Entry(lf1,bd=4,textvariable=dose)
e3.place(x=130,y=90,width=200)
e4=Entry(lf1,bd=4,textvariable=nooftablets)
e4.place(x=130,y=140,width=200)
e5=Entry(lf1,bd=4,textvariable=issuedate)
e5.place(x=130,y=180,width=200)
e6=Entry(lf1,bd=4,textvariable=expdate)
e6.place(x=130,y=220,width=200)
e7=Entry(lf1,bd=4,textvariable=dailydose)
e7.place(x=130,y=260,width=200)
e8=Entry(lf1,bd=4,textvariable=sideeffect)
e8.place(x=130,y=300,width=200)
e9=Entry(lf1,bd=4,textvariable=bloodpressure)
e9.place(x=460,y=10,width=200)
e10=Entry(lf1,bd=4,textvariable=doc)
e10.place(x=460,y=60,width=200)
e11=Entry(lf1,bd=4,textvariable=medication)
e11.place(x=460,y=110,width=200)
e12=Entry(lf1,bd=4,textvariable=pateintid)
e12.place(x=460,y=160,width=200)
e13=Entry(lf1,bd=4,textvariable=nameofpateint)
e13.place(x=460,y=210,width=200)
e14=Entry(lf1,bd=4,textvariable=dob)
e14.place(x=460,y=260,width=200)
e15=Entry(lf1,bd=4,textvariable=addressofpatient)
e15.place(x=460,y=300,width=200)


#frame2
f2=Frame(win,bd=15,relief=RIDGE)
f2.place(x=0,y=420,width=1290,height=210)
#buttons

#del button
d_btn=Button(win,text='Delete',font='ariel 15 bold',bg='brown',fg='white',bd=5,cursor='hand2',command=delete)
d_btn.place(x=90,y=620,width=190)
#prescription button
p_btn=Button(win,text='Prescription',font='ariel 15 bold',bg='green',fg='white',bd=5,cursor='hand2',command=pre)
p_btn.place(x=300,y=620,width=190)
#save prescription data
pd_btn=Button(win,text='Save Prescription Data',font='ariel 15 bold',bg='blue',fg='white',bd=5,cursor='hand2',command=pd)
pd_btn.place(x=900,y=620,width=290)
#clear button
c_btn=Button(win,text='Clear',font='ariel 15 bold',bg='purple',fg='white',bd=5,cursor='hand2',command=clr)
c_btn.place(x=700,y=620,width=190)
#exit button
e_btn=Button(win,text='Exit',font='ariel 15 bold',bg='orange',fg='white',bd=5,cursor='hand2',command=exit)
e_btn.place(x=500,y=620,width=190)
#Scroll bar for prescription
scroll_x=ttk.Scrollbar(f2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill='x')
scroll_y=ttk.Scrollbar(f2,orient=VERTICAL)
scroll_y.pack(side='right',fill='y')

table=ttk.Treeview(f2,columns=('not','ref','dose','nots','issd','expd','dd','sd','pi','pn','dob','pa'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x=ttk.Scrollbar(command=table.xview)
scroll_y=ttk.Scrollbar(command=table.yview)

#heading for prescription data
table.heading('not',text='Name of Tablets')
table.heading('ref',text='Reference No.')
table.heading('dose',text='Dose')
table.heading('nots',text='No. of Tablets')
table.heading('issd',text='Issue Date')
table.heading('expd',text='Exp.Date')
table.heading('dd',text='Daily Dose')
table.heading('pi',text='Patient id.')
table.heading('sd',text='Side Effect')
table.heading('pn',text='Patient Name')
table.heading('dob',text='DOB')
table.heading('pa',text='Patient Address')


table['show']='headings'
table.pack(fill=BOTH,expand=1)
table.column('not',width=40)
table.column('ref',width=100)
table.column('dose',width=100)
table.column('nots',width=100)
table.column('issd',width=100)
table.column('expd',width=100)
table.column('dd',width=100)
table.column('sd',width=100)
table.column('pi',width=100)
table.column('pn',width=100)
table.column('dob',width=100)
table.column('pa',width=100)
table.bind('<ButtonRelease-1>',get_data)
fetch_data()
win.mainloop()


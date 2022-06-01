def addstudent():
    print('Student added')
def searchstudent():
    print('Student Search')
def deletestudent():
    print('Student delete')
def updatestudent():
    print('Student update')
def showstudent():
    print('Student show')
def exportstudent():
    print('Student export')
def exitstudent():
    print('Student exit')




#############################################Connecttion of Database
def Connectdb():
    dbroot = Toplevel()
    dbroot.grab_set()                                    #
    dbroot.geometry('470x250+800+230')                   #---soto window er map
    dbroot.iconbitmap('r.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
    #------------------------------------Connectdb Labels
    hostlabel = Label(dbroot,text="Enter host : ",bg='gold2', font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot,text="Enter user : ",bg='gold2', font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot,text="Enter password : ",bg='gold2', font=('times', 20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    passwordlabel.place(x=10, y=130)


    #-----------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()


    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
    passwordentry.place(x=250, y=130)

    #-----------------------------Connectdb button
    submitbutton = Button(dbroot,text='submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',activeforeground='white')
    submitbutton.place(x=150,y=190)





    dbroot.mainloop()








def tick():                                                #---------Clock er jonno time ebong date
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%M/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)





##################### Intro Slider
import random
colors = ['red','green','blue','yellow','pink','red2','gold2']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2,IntroLabelColorTick)







def IntroLabelTick():                                       #----------Rmstu student management system lehka ta lafabe tar jonno ei code
    global count,text
    if(count>=len(ss)):
        count = 0
        text =''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count +=1
    SliderLabel.after(200,IntroLabelTick)








########################################



from tkinter import*
from tkinter import Toplevel                     #ekta soto window database login er jonno
import time
root = Tk()                                      #The root window is created. The root window is a main application window in our programs. It has a title bar and borders. These are provided by the window manager
root.title('RMSTU Student Management System')
root.config(bg='gold2')
root.geometry('1174x700+200+50')                 #screen hidth width diyesi ebong x=200 mane 20-0 ghor pase cepa jabe ebong y mane niche
root.iconbitmap('r.ico')                         #image lagalam title er pase ico image e lagbe eta copy kore pycharam er code er upor paste dilei hbe
root.resizable(False,False)                      #window bar lock kore diar moto mane soto boro kisui kora jabenaa







########################## Frames
DataEntryFrame =Frame(root,bg='white',relief=GROOVE,borderwidth=5)                 #-----Frame 1
DataEntryFrame.place(x=10,y=80,width=500,height=600)


##----------------------------------------------------Dataentry Frame Intro
frontlabel= Label(DataEntryFrame,text='-----------Welcome----------',width=30,font=('arial',22,'italic bold'),bg='gold2')
frontlabel.pack(side=TOP,expand=True)


addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)


searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)


deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)


updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)


showallbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)


exportbtn = Button(DataEntryFrame,text='6. Export Data',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exitstudent)
exportbtn.pack(side=TOP,expand=True)


exitbtn = Button(DataEntryFrame,text='7. Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)








ShowdataFrame =Frame(root,bg='white',relief=GROOVE,borderwidth=5)
ShowdataFrame.place(x=540,y=80,width=620,height=600)








######################### Slider                          A slider is a Tkinter object with which a user can set a value by moving an indicator. Sliders can be vertically or horizontally arranged. A slider is created with the Scale method()
ss= 'Welcome to RMSTU Student Management System'
count = 0
text = ''
#########################
SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=40,bg='cyan')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()







######################### Clock
clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=0,y=0)
tick()





#################################Connect database Button
connectbutton = Button(root,text='connect to Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bd=6,bg='green2',activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=930,y=0)






root.mainloop()                                  #amr window display show er knno




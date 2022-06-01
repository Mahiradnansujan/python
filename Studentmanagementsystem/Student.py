from tkinter import *
from tkinter import ttk            #combo box gender e use er jnno
import pymysql
from tkinter import messagebox

class Student:                         #-------akta class banate hbe
    def __init__(self,root):         #----------akane root holo window
       self.root=root
       self.root.title("RMSTU CSE Student Management System")
       self.root.geometry("1350x700+0+0")





       #----------Frame-------------
       title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="Blue",fg="yellow")    #title er name dilam
       title.pack(side=TOP,fill=X)



       #--------------All variable--------------------

       self.Roll_No_var=StringVar()
       self.Name_var=StringVar()
       self.Reg_No_var=StringVar()
       self.Email_var=StringVar()
       self.Gender_var=StringVar()
       self.Contact_No_var=StringVar()
       self.Session_var=StringVar()



       self.search_by = StringVar()
       self.search_txt = StringVar()






                    #---------------Manage Frame
       Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="red")        #------Frame 1                 #-----------frame banalam 2 ta banabo frame er name diyesi .place diye frame er jaiga diyesi koi bosbe x mane left theka rigt e capa r y mane kotota niche hbe seta
       Manage_Frame.place(x=20,y=100,width=550,height=680)

       m_title=Label(Manage_Frame,text="Manage Students",bg="red",fg="white",font=("times new roman",30,"bold",))
       m_title.grid(row=0,columnspan=2,pady=20)              #----place na dia grid use koresi karon grid dia frame er vitor kaj kore



       lbl_roll=Label(Manage_Frame,text="Roll No.",bg="red",fg="white",font=("times new roman",20,"bold",))
       lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

       txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
       txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")



       lbl_name = Label(Manage_Frame, text="Name.", bg="red", fg="white", font=("times new roman", 20, "bold",))
       lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

       txt_name = Entry(Manage_Frame,textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
       txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")




       lbl_regno = Label(Manage_Frame, text="Reg.No.", bg="red", fg="white", font=("times new roman", 20, "bold",))
       lbl_regno.grid(row=3, column=0, pady=10, padx=20, sticky="w")

       txt_regno = Entry(Manage_Frame,textvariable=self.Reg_No_var ,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
       txt_regno.grid(row=3, column=1, pady=10, padx=20, sticky="w")





       lbl_email = Label(Manage_Frame, text="Email.", bg="red", fg="white", font=("times new roman", 20, "bold",))
       lbl_email.grid(row=4, column=0, pady=10, padx=20, sticky="w")

       txt_email = Entry(Manage_Frame,textvariable=self.Email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
       txt_email.grid(row=4, column=1, pady=10, padx=20, sticky="w")




       lbl_gender = Label(Manage_Frame, text="Gender.", bg="red", fg="white", font=("times new roman", 20, "bold",))
       lbl_gender.grid(row=5, column=0, pady=10, padx=20, sticky="w")

       combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman", 14, "bold"),state='readonly')
       combo_gender['values']=("male","female","Other")
       combo_gender.grid(row=5,column=1,padx=20,pady=10)




       lbl_contact = Label(Manage_Frame, text="Contact No.", bg="red", fg="white", font=("times new roman", 20, "bold",))
       lbl_contact.grid(row=6, column=0, pady=10, padx=20, sticky="w")

       txt_contact = Entry(Manage_Frame,textvariable=self.Contact_No_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
       txt_contact.grid(row=6, column=1, pady=10, padx=20, sticky="w")




       lbl_session=Label(Manage_Frame,text="Session.",bg="red",fg="white",font=("times new roman",20,"bold"))
       lbl_session.grid(row=7,column=0,pady=10,padx=20,sticky="w")

       combo_session=ttk.Combobox(Manage_Frame,textvariable=self.Session_var, font=("times new roman",14,"bold"),state='readonly')
       combo_session['values']=("2014-2015","2015-2016","2017-2018","2019-2020","2021-2022")
       combo_session.grid(row=7,column=1,padx=20,pady=10)







       # ==========Button Frame-----------------------

       btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="yellow")
       btn_Frame.place(x=10,y=550,width=490,height=80)

       Addbtn = Button(btn_Frame,text="ADD",width=10,command=self.add_students).grid(row=0,column=0, padx=10, pady=10)
       updatebtn = Button(btn_Frame,text="Update",command=self.update_data,font=("times new roman",10,"bold"),width=13,height=3).grid(row=0,column=1, padx=10, pady=10)
       deletebtn = Button(btn_Frame,text="Delete",command=self.delete_data,font=("times new roman",10,"bold"),width=13,height=3).grid(row=0, column=2, padx=10, pady=10)
       Clearbtn = Button(btn_Frame,text="Clear",font=("times new roman",10,"bold"),width=13,height=3,command=self.clear).grid(row=0, column=3, padx=10, pady=10)







#==========-----------------Details Frame
       Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lime")     # ------Frame 2
       Detail_Frame.place(x=630,y=100,width=890,height=680)




       lbl_search=Label(Detail_Frame,text="Search By",bg="green",fg="white",font=("times new roman",20,"bold"))
       lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

       combo_search= ttk.Combobox(Detail_Frame,textvariable=self.search_by,font=("times new roman",14,"bold"),state='readonly')
       combo_search['values']=("Reg_no","Roll_no","Name","Contact ")
       combo_search.grid(row=0,column=1,padx=20,pady=10)

       txt_seacrh=Entry(Detail_Frame,textvariable=self.search_txt,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
       txt_seacrh.grid(row=0,column=2,pady=10,padx=20,sticky="w")

       searchbtn=Button(Detail_Frame,text="Search",width=10,pady=9,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
       showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=9,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)



#Table Frame----------====================------------------- Frame 3

       Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="Green")
       Table_Frame.place(x=10,y=70,width=855,height=595)

       scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
       scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
       self.Student_table=ttk.Treeview(Table_Frame,columns=("Roll No.","Name","Reg No.","Email","Gender","Contact No.","Session"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)

       scroll_x.config(command=self.Student_table.xview)
       scroll_y.config(command=self.Student_table.yview)
       self.Student_table.heading("Roll No.",text="Roll No.")
       self.Student_table.heading("Name",text="Name")
       self.Student_table.heading("Reg No.",text="Reg No.")
       self.Student_table.heading("Email",text="Email")
       self.Student_table.heading("Gender",text="Gender")
       self.Student_table.heading("Contact No.",text="Contact No.")
       self.Student_table.heading("Session",text="Session")
       self.Student_table['show']='headings'

       self.Student_table.column("Roll No.",width=100)                    #sob gular width thik kore dilam
       self.Student_table.column("Name", width=120)
       self.Student_table.column("Reg No.", width=120)
       self.Student_table.column("Email", width=120)
       self.Student_table.column("Gender", width=120)
       self.Student_table.column("Contact No.", width=120)
       self.Student_table.column("Session", width=150)


       self.Student_table.pack(fill=BOTH,expand=1)                #sada frame ta boro korlam fill expand diye
       self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
       self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.Name_var.get()=="" or self.Reg_No_var.get()=="" or self.Email_var.get()=="" or self.Gender_var.get()=="" or self.Contact_No_var.get()=="" or self.Session_var.get()=="" :
            messagebox.showerror("Error","All fields are required to fill")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                             self.Name_var.get(),
                                                                             self.Reg_No_var.get(),
                                                                             self.Email_var.get(),
                                                                             self.Gender_var.get(),
                                                                             self.Contact_No_var.get(),
                                                                             self.Session_var.get()
                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("sucess","Recored has been inserted")


    def fetch_data(self):                                                      #---------data display te show er jonno
        con = pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()

        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                    self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Reg_No_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_No_var.set("")
        self.Session_var.set("")

    def get_cursor(self,ev):
        curosor_row=self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)           #basai esa suru
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Reg_No_var.set(row[2])
        self.Email_var.set(row[3])
        self.Gender_var.set(row[4])
        self.Contact_No_var.set(row[5])
        self.Session_var.set(row[6])

    def update_data(self):
         con=pymysql.connect(host="localhost",user="root",password="",database="stm")
         cur=con.cursor()
         cur.execute("update students set Name=%s,reg_no=%s,Email=%s,Gender=%s,Contact_No=%s,Session=%s where roll_no=%s",(
                                                                         self.Name_var.get(),
                                                                         self.Reg_No_var.get(),
                                                                         self.Email_var.get(),
                                                                         self.Gender_var.get(),
                                                                         self.Contact_No_var.get(),
                                                                         self.Session_var.get(),
                                                                         self.Roll_No_var.get()
                                                                        ))
         con.commit()
         self.fetch_data()
         self.clear()
         con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()




    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()

        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                    self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()







root=Tk()             #---------object banalam
ob=Student(root)      #-------object e root pass korai dilam
root.mainloop()
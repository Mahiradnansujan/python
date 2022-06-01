from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_app:
    def __init__(self,root):   #====pura frame mane window banalam
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing software")
        bg_color="#088A08"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="black",font=("times new roman",30,"bold"),pady=2).pack(fill=X) #title box er sob kaj akane declare koresi


        #======#===#=variables===#==#==#=
        #========Cosmetics==========
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_oil=IntVar()
        self.body_lotion =IntVar()
        self.gell=IntVar()

        #=======grocery========
        self.Chips=IntVar()
        self.sugar=IntVar()
        self.food_oil=IntVar()
        self.wheat=IntVar()
        self.daal=IntVar()
        self.tea=IntVar()
        #=======Cold drinks=====
        self.seven_up=IntVar()
        self.fanta=IntVar()
        self.fruto=IntVar()
        self.coke=IntVar()
        self.sprite=IntVar()
        self.maza=IntVar()

        #=====Total product Price & Tax Variable====
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #======customer=======
        self.c_name=StringVar()
        self.c_phon=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()











        

















        #====customer details frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer details",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        cname_label=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_label=Label(F1,text="Customer phone no.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_label=Label(F1,text="Bill Number.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.bill_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10)




        #======cosmetics frame
        F2 =LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath soap",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        cream_lbl=Label(F2,text="cream",font=("times new roman",16,"bold"), bg=bg_color,fg="black").grid(row=1,column=0,padx=10, pady=10, sticky="w")
        cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w_lbl=Label(F2,text="Facewash",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_oil_lbl=Label(F2,text="Hair Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_oil__tx=Entry(F2,width=10,textvariable=self.hair_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        body_lotion__lbl=Label(F2,text="Body lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10, pady=10, sticky="w")
        body_lotion_tx=Entry(F2, width=10,textvariable=self.body_lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady =10)




        # ======Grocery frame
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        Chips_lbl=Label(F3,text="Chips",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Chips_txt=Entry(F3,width=10,textvariable=self.Chips,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        sugar_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cream_txt = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Tea_lbl=Label(F3,text="Food oil",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10, pady=10,sticky="w")
        Tea_txt=Entry(F3, width=10,textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Wheat_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"), bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Wheat_tx=Entry(F3,width=10,textvariable=self.wheat, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Daal_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4, column=0,padx=10,pady=10,sticky="w")
        Daal_tx = Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)





        # ======Cold Drink Frame
        F4=LabelFrame(self.root, bd=10,relief=GROOVE,text="Cold drink",font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        c1_lbl=Label(F4,text="7up",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4, width=10,textvariable=self.seven_up, font=("times new roman",16,"bold"),bd=5, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="Fanta",font=("times new roman", 16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.fanta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(F4,text="Fruto",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt = Entry(F4,width=10,textvariable=self.fruto,font=("times new roman",16,"bold"),bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl=Label(F4,text="cock",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_tx=Entry(F4,width=10,textvariable=self.coke, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl = Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_tx = Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)




        #============Bill Area========
        F5 =Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=528,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)





        #====ButtonFrame===================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=274)

        m1_lbl=Label(F6,text="total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=20,pady=10)

        m2_lbl=Label(F6,text="total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt = Entry(F6, width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=20,pady=10)

        m3_lbl=Label(F6,text="total COld drinks Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=20,pady=10)

        c1_lbl=Label(F6, text="total Cosmetic Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18,textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=20, pady=10)

        c2_lbl = Label(F6, text="total Grocery Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18,textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=20, pady=10)

        c3_lbl = Label(F6, text="total COld drinks Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18,textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=20, pady=10)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=840,width=670,height=145)

        total_btn=(Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="White",pady=15,bd=5,width=11,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5))
        GBILL_btn=(Button(btn_F,text="Genrate Bill",command=self.bill_area,bg="cadetblue",fg="White",pady=15,bd=5,width=11,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5))
        Clear_btn=(Button(btn_F,text="Clear",command=self.clear_data,bg="purple",fg="White",pady=15,bd=5,width=11,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5))
        Exit_btn=(Button(btn_F,text="Exit",command=self.Exit_app,bg="red",fg="White",pady=15,bd=5,width=11,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5))
        self.welcome_bill()




    def total(self):                #price gula diyesi abong total price o funtion e dukai disi total funtion e lak kore command diye call kore diyesi total re
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*180
        self.c_ho_p=self.hair_oil.get()*210
        self.c_bl_p=self.body_lotion.get()*320

        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_ho_p+
                                    self.c_bl_p
                                    )


        self.cosmetic_price.set("Tk "+ str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Tk. "+str(self.c_tax))



        self.g_c_p=self.Chips.get()*10
        self.g_sugar_p=self.sugar.get()*40
        self.g_foodoil_p=self.food_oil.get()*70
        self.g_wheat_p=self.wheat.get()*50
        self.g_daal_p=self.daal.get()*80

        self.total_grocery_price=float(
                                    self.g_c_p+
                                    self.g_sugar_p+
                                    self.g_foodoil_p+
                                    self.g_wheat_p+
                                    self.g_daal_p
                                    )

        self.grocery_price.set("Tk "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Tk "+str(self.g_tax))


        self.d_seven_up_p=self.seven_up.get()*35
        self.d_fanta_p=self.fanta.get()*30
        self.d_fruto_p=self.fruto.get()*40
        self.d_coke_p=self.coke.get()*15
        self.d_sprite_p=self.sprite.get()*25

        self.total_drinks_price=float(
                                    self.d_seven_up_p+
                                    self.d_fanta_p+
                                    self.d_fruto_p+
                                    self.d_coke_p+
                                    self.d_sprite_p
                                    )

        self.cold_drink_price.set("Tk "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.5),2)
        self.cold_drink_tax.set("Tk. "+str(self.d_tax))



        self.Total_bill=(   self.total_cosmetic_price+
                            self.total_grocery_price+
                            self.total_drinks_price+
                            self.c_tax+
                            self.g_tax+
                            self.d_tax
                       )






    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome MAhirs door ReAtil\n")
        self.txtarea.insert(END,f"\n Bill Number :{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number :{self.c_phon.get()}")
        self.txtarea.insert(END,f"\n============================================================")
        self.txtarea.insert(END,f"\n Products\t\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n============================================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Tk 0.0" and self.grocery_price.get()=="Tk 0.0" and self.cold_drink_price.get()=="Tk 0.0":
            messagebox.showerror("Error", "No product Purchased")

        else:
            self.welcome_bill()


            #Cosmetics====================
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.hair_oil.get()!=0:
                self.txtarea.insert(END,f"\n Hair oil\t\t\t{self.hair_oil.get()}\t\t{self.c_ho_p}")
            if self.body_lotion.get() != 0:
                self.txtarea.insert(END, f"\n Body lotion\t\t\t{self.body_lotion.get()}\t\t{self.c_bl_p}")

            #Grocery=======================
            if self.Chips.get()!=0:
               self.txtarea.insert(END,f"\n Chips\t\t\t{self.Chips.get()}\t\t{self.g_c_p}")
            if self.sugar.get()!=0:
               self.txtarea.insert(END,f"\n Sugar\t\t\t{self.sugar.get()}\t\t{self.g_sugar_p}")
            if self.food_oil.get()!=0:
               self.txtarea.insert(END,f"\n Food oil\t\t\t{self.food_oil.get()}\t\t{self.g_foodoil_p}")
            if self.wheat.get()!=0:
               self.txtarea.insert(END,f"\n Wheat\t\t\t{self.wheat.get()}\t\t{self.g_wheat_p}")
            if self.daal.get()!=0:
               self.txtarea.insert(END,f"\n Daal\t\t\t{self.daal.get()}\t\t{self.g_daal_p}")

            #Cold drinks===================
            if self.seven_up.get()!=0:
                self.txtarea.insert(END,f"\n Seven up\t\t\t{self.seven_up.get()}\t\t{self.d_seven_up_p}")
            if self.fanta.get() != 0:
                self.txtarea.insert(END, f"\n Fanta\t\t\t{self.fanta.get()}\t\t{self.d_fanta_p}")
            if self.fruto.get() != 0:
                self.txtarea.insert(END, f"\n Fruto\t\t\t{self.fruto.get()}\t\t{self.d_fruto_p}")
            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\n Coke\t\t\t{self.coke.get()}\t\t{self.d_coke_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t\t{self.sprite.get()}\t\t{self.d_sprite_p}")

            self.txtarea.insert(END,f"\n------------------------------------------------------------")
            if self.cosmetic_tax.get()!="Tk 0.0":
                self.txtarea.insert(END,f"\n Cosmetic    Tax\t\t\t\t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get()!="TK 0.0":
                self.txtarea.insert(END,f"\n Grocery     Tax\t\t\t\t\t {self.grocery_tax.get()}")

            if self.cold_drink_tax.get()!="Tk 0.0":
                self.txtarea.insert(END,f"\n Cold drinks Tax\t\t\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill :\t\t\t\t\tTk. {self.Total_bill}")
            self.txtarea.insert(END,f"\n-----------------------------------------------------------")
            self.save_bill()

    def save_bill(self):          #Bill save kora folder er vitor kaj koresi akane
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"Bill no. :{self.bill_no.get()} saved Successfully")
        else:
            return



    def find_bill(self): #====akane search button e ager akta bill number dia search er kaj kora holo r command e call kora hoyesa ei funtion ta
        present="no"
        # sss=str(self.bill_no.get())
        # print(sss)
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.bill_no.get():
                # print(i)
                f1=open(f"bills/{i }","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d )
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bil No.")





    def clear_data(self):                     #clear Button er kaj hoyese
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:



            # ========Cosmetics==========
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_oil.set(0)
            self.body_lotion.set(0)
            self.gell.set(0)

            # =======grocery========
            self.Chips.set(0)
            self.sugar.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.daal.set(0)
            self.tea.set(0)
            # =======Cold drinks=====
            self.seven_up.set(0)
            self.fanta.set(0)
            self.fruto.set(0)
            self.coke.set(0)
            self.sprite.set(0)
            self.maza.set(0)




            # =====Total product Price & Tax Variable====
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            # ======customer=======
            self.c_name.set("")
            self.c_phon.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()



    def Exit_app(self):                  #exit er kaj hoyesa
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()


root=Tk()
obj=Bill_app(root)
root.mainloop()
from tkinter import *
from PIL import Image,ImageTk   #pip install PILLOW
from tkinter import ttk,messagebox
import os
import sqlite3


class EmpClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("RETAILER BILLING SOFTWARE")
        self.root.config(bg="ivory3")
        self.root.focus_force() 

        #all variables==============
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_DOB=StringVar()
        self.var_DOJ=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        

#=============search frame=============================================================================
        searchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="ivory3")
        searchFrame.place(x=250,y=20,width=600,height=70)

#=================options================================
        cmb_Search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_Search.place(x=10,y=10,width=180)
        cmb_Search.current(0)


        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="seashell2").place(x=200,y=10)
        btn_search=Button(searchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="cornflower blue",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

#======title======
        title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="tan4",fg="white").place(x=50,y=100,width=1000)

#====content============

       #===row1=======
        lbl_empid=Label(self.root,text="EMP ID",font=("goudy old style",15),bg="ivory3").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="ivory3").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="ivory3").place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="seashell2").place(x=150,y=150,width=180)
        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="seashell2").place(x=850,y=150,width=180)

        # ===row2=======
        lbl_name=Label(self.root,text="NAME",font=("goudy old style",15),bg="ivory3").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="ivory3").place(x=350,y=190)
        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="ivory3").place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="seashell2").place(x=150, y=190, width=180)
        txt_dob=Entry(self.root,textvariable=self.var_DOB,font=("goudy old style", 15),bg="seashell2").place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_DOJ,font=("goudy old style",15),bg="seashell2").place(x=850,y=190,width=180)

        # ===row3=======
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="ivory3").place(x=50,y=230)
        lbl_password=Label(self.root,text="Password",font=("goudy old style",15),bg="ivory3").place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="ivory3").place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="seashell2").place(x=150, y=230, width=180)
        txt_pass=Entry(self.root,textvariable=self.var_password,font=("goudy old style", 15),bg="seashell2").place(x=500,y=230,width=180)
        # txt_utype=Entry(self.root,textvariable=self.var_utype,font=("goudy old style",15),bg="light yellow").place(x=850,y=230,width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin","Employee"),state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)

        # ===row4=======
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="ivory3").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="ivory3").place(x=500,y=270)

        self.txt_address=Text(self.root,font=("goudy old style",15),bg="seashell2")
        self.txt_address.place(x=150, y=270, width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style", 15),bg="seashell2").place(x=600,y=270,width=180)

#============buttons=====================
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="chartreuse4",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="gold3",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete= Button(self.root,command=self.delete,text="Delete",font=("goudy old style", 15), bg="red3",fg="white",cursor="hand2").place (x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="dodger blue",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

#===tree view====
#displays all the information in tabular manner

#===employee details=====

        emp_frame = Frame(self.root, bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.Emp_table=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","password","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)  #tupple banaye hai
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Emp_table.xview)
        scrolly.config(command=self.Emp_table.yview)
        self.Emp_table.heading("eid",text="EMP ID")
        self.Emp_table.heading("name",text="NAME")
        self.Emp_table.heading("email",text="E-mail")
        self.Emp_table.heading("gender",text="Gender")
        self.Emp_table.heading("contact",text="Contact")
        self.Emp_table.heading("dob",text="D.O.B")
        self.Emp_table.heading("doj",text="D.O.J")
        self.Emp_table.heading("password",text="Password")
        self.Emp_table.heading("utype",text="User Type")
        self.Emp_table.heading("address",text="Address")
        self.Emp_table.heading("salary",text="Salary")

        self.Emp_table["show"]="headings"

        self.Emp_table.column("eid",width=90)
        self.Emp_table.column("name",width=100)
        self.Emp_table.column("email",width=100)
        self.Emp_table.column("gender",width=100)
        self.Emp_table.column("contact",width=100)
        self.Emp_table.column("dob",width=100)
        self.Emp_table.column("doj",width=100)
        self.Emp_table.column("password",width=100)
        self.Emp_table.column("utype",width=100)
        self.Emp_table.column("address",width=100)
        self.Emp_table.column("salary",width=100)

        self.Emp_table.pack(fill=BOTH,expand=1)
        self.Emp_table.bind("<ButtonRelease-1>",self.get_data)



        self.Emp_table.pack(fill=BOTH,expand=1)

        self.show()
#===================================================================================================================================

    def add(self):                                              
        con=sqlite3.connect(database=r'BSW.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee Id is required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID already assigned,try diffrent",parent=self.root)
                else:
                    cur.execute("Insert into employee(eid,name,email,gender,contact,dob,doj,password,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                self.var_emp_id.get(),
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),

                                                self.var_DOB.get(),
                                                self.var_DOJ.get(),

                                                self.var_password.get(),
                                                self.var_utype.get(),
                                                self.txt_address.get('1.0',END),
                                                self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'BSW.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.Emp_table.delete(*self.Emp_table.get_children())
            for row in rows:
                self.Emp_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def get_data(self,ev):
        f=self.Emp_table.focus()
        content=self.Emp_table.item((f))
        row=content['values']
        #print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])

        self.var_DOB.set(row[5])
        self.var_DOJ.set(row[6])

        self.var_password.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])


    def update(self):                                               
        con=sqlite3.connect(database=r'BSW.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee Id is required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Invalid Employee ID   ",parent=self.root)
                else:
                    cur.execute("update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,password=?,utype=?,address=?,salary=? where eid=? ",(

                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),

                                                self.var_DOB.get(),
                                                self.var_DOJ.get(),

                                                self.var_password.get(),
                                                self.var_utype.get(),
                                                self.txt_address.get('1.0',END),
                                                self.var_salary.get(),
                                                self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
         con = sqlite3.connect(database=r'BSW.db')
         cur = con.cursor()
         try:
             if self.var_emp_id.get() == "":
                 messagebox.showerror("Error", "Employee Id is required", parent=self.root)
             else:
                 cur.execute("select * from employee where eid=?", (self.var_emp_id.get(),))
                 row = cur.fetchone()
                 if row == None:
                     messagebox.showerror("Invalid Employee ID",parent=self.root)
                 else:
                     op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                     if op==True:
                         cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                         con.commit()
                         messagebox.showinfo("Delete", "Employee Deleted  Successfully", parent=self.root)
                         self.clear()


         except Exception as ex:
             messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")

        self.var_DOB.set("")
        self.var_DOJ.set("")

        self.var_password.set("")
        self.var_utype.set("select")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("select")
        self.show()


    def search(self):
        con=sqlite3.connect(database=r'BSW.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Search":
                messagebox.showerror("Error","Select search by options",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)

            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Emp_table.delete(*self.Emp_table.get_children())
                    for row in rows:
                        self.Emp_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","NO Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = EmpClass(root)
    root.mainloop()

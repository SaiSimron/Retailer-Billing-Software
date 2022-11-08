from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class SupClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("RETAILER BILLING SOFTWARE")
        self.root.config(bg="ivory3")
        self.root.focus_force() 

        #all variables==============
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_sup_billNo=StringVar()
        self.var_name = StringVar()
        self.var_contact=StringVar()

#=================options================================
        lbl_Search=Label(self.root, text="Bill No", font=("goudy old style", 15), bg="ivory3")
        lbl_Search.place(x=700,y=80)

        txt_search=Entry(self.root, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="seashell2").place(x=800, y=80,width=160)
        btn_search=Button(self.root, text="Search", command=self.search, font=("goudy old style", 15), bg="cornflower blue", fg="white", cursor="hand2").place(x=980, y=79, width=100, height=28)

#======title======
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="tan4",fg="white").place(x=50,y=10,width=1000,height=40)

#====content============

       #===row1=======
        lbl_supplier_billNo=Label(self.root,text="Bill No",font=("goudy old style",15),bg="ivory3").place(x=50,y=80)
        txt_supplier_billNo = Entry(self.root, textvariable=self.var_sup_billNo, font=("goudy old style", 15),bg="seashell2").place(x=180, y=80, width=180)


        # ===row2=======
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="ivory3").place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="seashell2").place(x=180, y=120, width=180)

        # ===row3=======
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="ivory3").place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="seashell2").place(x=180, y=160, width=180)

        # ===row4=======
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="ivory3").place(x=50,y=200)
        self.txt_desc=Text(self.root, font=("goudy old style", 15), bg="seashell2")
        self.txt_desc.place(x=180, y=200, width=470, height=125)


#============buttons=====================
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="chartreuse4",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="gold3",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete= Button(self.root,text="Delete",command=self.delete,font=("goudy old style", 15), bg="red3",fg="white",cursor="hand2").place (x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)

#===tree view====
        
#===employee details=====

        emp_frame = Frame(self.root, bd=3,relief=RIDGE)  
        emp_frame.place(x=680, y=120, width=380, height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame, columns=("Bill", "name", "contact", "description"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("Bill", text="Bill No")
        self.supplierTable.heading("name", text="NAME")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("description", text="Description")

        self.supplierTable["show"]= "headings"

        self.supplierTable.column("Bill", width=90)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("description", width=100)

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.show()

        #===================================================================================================================================

    def add(self):                                              
        con=sqlite3.connect(database=r'BSW.db')
        cur=con.cursor()
        try:
            if self.var_sup_billNo.get()== "":
                messagebox.showerror("Error","Bill No is required",parent=self.root)
            else:
                cur.execute("select * from supplier where Bill=?", (self.var_sup_billNo.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Bill No already assigned,try diffrent",parent=self.root)
                else:
                    cur.execute("Insert into supplier(Bill,name,contact,desc) values(?,?,?,?)",(
                                                self.var_sup_billNo.get(),
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.txt_desc.get('1.0', END),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'BSW.db')
        cur=con.cursor()
        try:
            cur.execute("select * from Supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=self.supplierTable.item((f))
        row=content['values']
        #print(row)
        self.var_sup_billNo.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END, row[3])


    def update(self):                                              
        con=sqlite3.connect(database=r'BSW.db')
        cur=con.cursor()
        try:
            if self.var_sup_billNo.get()== "":
                messagebox.showerror("Error","Bill Number is required",parent=self.root)
            else:
                cur.execute("select * from supplier where Bill=?", (self.var_sup_billNo.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Invalid Bill Number ",parent=self.root)
                else:
                    cur.execute("update supplier set name=?,contact=?,desc=? where Bill=? ",(
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.txt_desc.get('1.0', END),
                                                self.var_sup_billNo.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
         con = sqlite3.connect(database=r'BSW.db')
         cur = con.cursor()
         try:
             if self.var_sup_billNo.get() == "":
                 messagebox.showerror("Error", "Bill Number is required", parent=self.root)
             else:
                 cur.execute("select * from supplier where Bill=?", (self.var_sup_billNo.get(),))
                 row = cur.fetchone()
                 if row == None:
                     messagebox.showerror("Invalid bill number",parent=self.root)
                 else:
                     op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                     if op==True:
                         cur.execute("delete from supplier where Bill=?", (self.var_sup_billNo.get(),))
                         con.commit()
                         messagebox.showinfo("Delete", "Supplier Deleted  Successfully", parent=self.root)
                         self.clear()


         except Exception as ex:
             messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup_billNo.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.var_searchtxt.set("")
        self.show()


    def search(self):
        con=sqlite3.connect(database=r'BSW.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Bill Number should be required",parent=self.root)
            else:
                cur.execute("select * from supplier where Bill=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error","NO Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



if __name__=="__main__":
    root = Tk()
    obj = SupClass(root)
    root.mainloop()

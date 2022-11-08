import os
import sqlite3
import time
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


from Employee import EmpClass
from Supplier import SupClass
from Category import CatClass
from Product import PrdClass
from Sales import SalClass

class BillSw:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("RETAILER BILLING SOFTWARE")
        self.root.config(bg="ivory3")

        # ===title=====

        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root, text="RETAIL BILLING",image=self.icon_title,compound=LEFT,font=("times new roman", 35, "bold"),bg="chocolate",fg="white",anchor="w",padx=15).place(x=0,y=0,relwidth=1,height=70)
        
        # ===btn_logout===
        btn_logout = Button(self.root, command = self.logout, text="Logout", font=("times new roman", 15, "bold"),bg="gold3",cursor="hand2").place(x=1150,
                                                                                                               y=10,height=50,width=150)
        #===clock===
        self.lbl_clock=Label(self.root, text="welcome to Store Billing System\t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS ",font=("times new roman", 16), bg="dark orchid", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        self.update_date_time()

        #===left Menue==== 
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((130,130),Image.Resampling.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="ivory4")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        

        self.icon_side=PhotoImage(file="images\logo1.png")
       
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",15),bg="ivory4").pack(side=TOP,fill=X)

        btn_employee=Button(LeftMenu, text="Employee", command = self.employee, image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman", 15,"bold"), bg="ivory3",bd=1,cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier=Button(LeftMenu, text="Supplier", command = self.supplier, image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman", 15,"bold"), bg="ivory3",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu, text="Category", command = self.category, image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman", 15,"bold"), bg="ivory3",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu, text="Product", command = self.product, image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman", 15,"bold"), bg="ivory3",bd=1,cursor="hand2").pack(side=TOP, fill=X)
        btn_sales=Button(LeftMenu, text="Sales", command = self.sales,  image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman", 15,"bold"), bg="ivory3",bd=1,cursor="hand2").pack(side=TOP, fill=X)
        btn_exit=Button(LeftMenu, text="Exit", command = self.exit, image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman", 15,"bold"), bg="ivory3",bd=1,cursor="hand2").pack(side=TOP, fill=X)

        #===content===
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="sienna3",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="chartreuse2",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total category\n[ 0 ]",bd=5,relief=RIDGE,bg="medium blue",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total product\n[ 0 ]",bd=5,relief=RIDGE,bg="plum4",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total sales\n[ 0 ]",bd=5,relief=RIDGE,bg="cyan4",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)


        #====footer====
        lbl_footer=Label(self.root,text="Retail Billing Software \n copyright @2022",font=("times new roman", 10), bg="dark orchid", fg="white").pack(side=BOTTOM,fill=X)

        self.update_content()

        #========================================================================================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=EmpClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SupClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CatClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=PrdClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SalClass(self.new_win)


    def exit(self):
        self.root.destroy()


    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d:%m-%Y")

        self.lbl_clock.config(text=f"welcome to Retailer Billing Software\t\t Date: {str(date_)} \t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)


    def update_content(self):
        con = sqlite3.connect(database=r'BSW.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[{str(len(product))}]')

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[{str(len(supplier))}]')

            cur.execute("select * from category")
            category= cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[{str(len(category))}]')

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[{str(len(employee))}]')

            bill=len(os.listdir('Bill Reports'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def logout(self):
        self.root.destroy()
        os.system("python Login.py")


if __name__=="__main__":
    root = Tk()
    obj = BillSw(root)
    root.mainloop()

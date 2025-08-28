from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime

class Renttal_Inventory:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Rental Inventory Management System") 
        self.root.geometry("1350x800+0+0")  
        self.root.configure(background='gainsboro')

        #=======================Frame============================================#
        MainFrame = Frame(self.root, bd=20,width=1350,height=700, relief=RIDGE, bg='black')
        MainFrame.grid()

        LeftFrame = Frame(MainFrame, bd=10,width=750,height=600, relief=RIDGE, bg='black')
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(MainFrame, bd=10,width=560,height=600, relief=RIDGE, bg='black')
        RightFrame.pack(side=RIGHT)

        # ====================Div_Frame=================================================#
        LeftFrame0 = Frame(LeftFrame, bd=5, width=712, height=143, padx=5, bg="gainsboro", relief=RIDGE)
        LeftFrame0.grid(row=0, column=0)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=712, height=170, padx=5, bg="gainsboro", relief=RIDGE)
        LeftFrame1.grid(row=1, column=0)
        LeftFrame2 = Frame(LeftFrame, bd=5, width=712, height=168, padx=5, bg="gainsboro", relief=RIDGE)
        LeftFrame2.grid(row=2, column=0)
        LeftFrame3 = Frame(LeftFrame, bd=5, width=712, height=95, padx=5, bg="gainsboro", relief=RIDGE)
        LeftFrame3.grid(row=3, column=0)

        RightFrame0 = Frame(RightFrame, bd=5, width=522, height=200, padx=5, bg="gainsboro", relief=RIDGE)
        RightFrame0.grid(row=0, column=0)
        RightFrame1 = Frame(RightFrame, bd=5, width=522, height=280, padx=5, bg="gainsboro", relief=RIDGE)
        RightFrame1.grid(row=1, column=0)
        RightFrame2 = Frame(RightFrame, bd=5, width=522, height=95, padx=0, bg="gainsboro", relief=RIDGE)
        RightFrame2.grid(row=2, column=0)

       
        # ================================================RightFrame0=================================================

        AcctOpen = StringVar()
        AppDate = StringVar()
        NextCreditReview = StringVar()
        LastCreditReview = StringVar()
        DateRev = StringVar()
        ProdCode = StringVar()
        ProdType = StringVar()
        NoDays = StringVar()
        CostPDay = StringVar()
        CreLimit = StringVar()
        CreCheck = StringVar()
        SettDueDay = StringVar()
        PaymentD = StringVar()
        Discount = StringVar()
        Deposit = StringVar()
        PayDueDay = StringVar()
        PaymentM = StringVar()

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        Tax = StringVar()
        SubTotal = StringVar()
        Total = StringVar()
        Receipt_Ref = StringVar()


        # ================================================RightFrame1=================================================

        # ================================================RightFrame2=================================================

        # ================================================LeftFrame0==================================================

        # ================================================LeftFrame1==================================================

        # ================================================LeftFrame2==================================================

        # ================================================LeftFrame3==================================================






if __name__=='__main__':
    root=Tk()
    application =Renttal_Inventory(root)
    root.mainloop()


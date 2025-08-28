import tkinter as tk
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime

class Rental_Inventory:
    

    def __init__(self, root):
        self.root = root
        self.root.title("Rental Inventory Management System") 
        self.root.geometry("1350x800+0+0")  
        self.root.configure(background='gainsboro')

        #=======================Frame============================================#
        MainFrame = tk.Frame(self.root, bd=20,width=1350,height=700, relief=tk.RIDGE, bg='black')
        MainFrame.grid()

        LeftFrame = tk.Frame(MainFrame, bd=10,width=750,height=600, relief=tk.RIDGE, bg='black')
        LeftFrame.pack(side=tk.LEFT)

        RightFrame = tk.Frame(MainFrame, bd=10,width=560,height=600, relief=tk.RIDGE, bg='black')
        RightFrame.pack(side=tk.RIGHT)

        # ====================Div_Frame=================================================#
        LeftFrame0 = tk.Frame(LeftFrame, bd=5, width=712, height=143, padx=5, bg="gainsboro", relief=tk.RIDGE)
        LeftFrame0.grid(row=0, column=0)
        LeftFrame1 = tk.Frame(LeftFrame, bd=5, width=712, height=170, padx=5, bg="gainsboro", relief=tk.RIDGE)
        LeftFrame1.grid(row=1, column=0)
        LeftFrame2 = tk.Frame(LeftFrame, bd=5, width=712, height=168, padx=5, bg="gainsboro", relief=tk.RIDGE)
        LeftFrame2.grid(row=2, column=0)
        LeftFrame3 = tk.Frame(LeftFrame, bd=5, width=712, height=95, padx=5, bg="gainsboro", relief=tk.RIDGE)
        LeftFrame3.grid(row=3, column=0)

        RightFrame0 = tk.Frame(RightFrame, bd=5, width=522, height=200, padx=5, bg="gainsboro", relief=tk.RIDGE)
        RightFrame0.grid(row=0, column=0)
        RightFrame1 = tk.Frame(RightFrame, bd=5, width=522, height=280, padx=5, bg="gainsboro", relief=tk.RIDGE)
        RightFrame1.grid(row=1, column=0)
        RightFrame2 = tk.Frame(RightFrame, bd=5, width=522, height=95, padx=0, bg="gainsboro", relief=tk.RIDGE)
        RightFrame2.grid(row=2, column=0)

        # ================================================Variables=================================================

        AcctOpen = tk.StringVar()
        AppDate = tk.StringVar()
        NextCreditReview = tk.StringVar()
        LastCreditReview = tk.StringVar()
        DateRev = tk.StringVar()
        ProdCode = tk.StringVar()
        ProdType = tk.StringVar()
        NoDays = tk.StringVar()
        CostPDay = tk.StringVar()
        CreLimit = tk.StringVar()
        CreCheck = tk.StringVar()
        SettDueDay = tk.StringVar()
        PaymentD = tk.StringVar()
        Discount = tk.StringVar()
        Deposit = tk.StringVar()
        PayDueDay = tk.StringVar()
        PaymentM = tk.StringVar()

        var1 = tk.IntVar()
        var2 = tk.IntVar()
        var3 = tk.IntVar()
        var4 = tk.IntVar()
        Tax = tk.StringVar()
        SubTotal = tk.StringVar()
        Total = tk.StringVar()
        Receipt_Ref = tk.StringVar()

        # ================================================RightFrame0=================================================

        self.lblAcctOpen = tk.Label(RightFrame0, font=('arial', 18, 'bold'), text="Account Opened:", padx=2, pady=2, bg="gainsboro")
        self.lblAcctOpen.grid(row=0, column=0, sticky=tk.W)

        self.cboAcctOpen = ttk.Combobox(RightFrame0, textvariable=AcctOpen, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboAcctOpen['value'] = ('', 'Select an option', 'Yes', 'No')
        self.cboAcctOpen.current(0)
        self.cboAcctOpen.grid(row=0, column=1, pady=2)

        self.lblNCreR = Label(RightFrame0, font=('arial', 18, 'bold'), text="Next Credit Review:", padx=2, pady=2, bg="gainsboro")
        self.lblNCreR.grid(row=2, column=0, sticky=W)

        self.cboNCreR = ttk.Combobox(RightFrame0, textvariable=NextCreditReview, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboNCreR['value'] = ('', 'Select an option', 'Yes', 'No')
        self.cboNCreR.current(0)
        self.cboNCreR.grid(row=2, column=1, pady=2)

        self.lblLCreR = Label(RightFrame0, font=('arial', 18, 'bold'), text="Last Credit Review:", padx=2, pady=2, bg="gainsboro")
        self.lblLCreR.grid(row=3, column=0, sticky=W)

        self.cboLCreR = ttk.Combobox(RightFrame0, textvariable=LastCreditReview, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboLCreR['value'] = ('', 'Select an option', 'Yes', 'No')
        self.cboLCreR.current(0)
        self.cboLCreR.grid(row=3, column=1, pady=2)

        self.lblDateRev = Label(RightFrame0, font=('arial', 18, 'bold'), text="Date Review:", padx=2, pady=2, bg="gainsboro")
        self.lblDateRev.grid(row=4, column=0, sticky=W)

        self.cboLCreR = ttk.Combobox(RightFrame0, textvariable=LastCreditReview, state='readonly',
                                font=('arial', 18, 'bold'), width=19)
        self.cboLCreR['value'] = ('', 'Select an option', 'Yes', 'No')
        self.cboLCreR.current(0)
        self.cboLCreR.grid(row=3, column=1, pady=2)

        self.lblDateRev = Label(RightFrame0, font=('arial', 18, 'bold'), text="Date Review:", padx=2, pady=2, bg="gainsboro")
        self.lblDateRev.grid(row=4, column=0, sticky=W)

        self.cboDateRev = ttk.Combobox(RightFrame0, textvariable=DateRev, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboDateRev['value'] = ('', 'Select an option', 'Yes', 'No')
        self.cboDateRev.current(0)
        self.cboDateRev.grid(row=4, column=1, pady=2)

        # ================================================RightFrame1=================================================

        # ================================================RightFrame2=================================================

        # ================================================LeftFrame0==================================================

        # ================================================LeftFrame1==================================================

        # ================================================LeftFrame2==================================================

        # ================================================LeftFrame3==================================================






if __name__=='__main__':
    root = tk.Tk()
    application = Rental_Inventory(root)
    root.mainloop()


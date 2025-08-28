from tkinter import *
from tkinter import ttk
import random
# import tkinter.messagebox # This import is redundant if 'from tkinter import messagebox' is also used
from tkinter import messagebox
import datetime

class Rental_Inventory:
    def __init__(self, root):
        self.root = root
        self.root.title("Rental Inventory Management System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='gainsboro')

        #=======================Frame============================================#
        # Changed tk.RIDGE to RIDGE because 'from tkinter import *' is used
        MainFrame = Frame(self.root, bd=20, width=1350, height=700, relief=RIDGE, bg='black')
        MainFrame.grid()

        # Changed tk.RIDGE to RIDGE and tk.LEFT to LEFT
        LeftFrame = Frame(MainFrame, bd=10, width=750, height=600, relief=RIDGE, bg='black')
        LeftFrame.pack(side=LEFT)

        # Changed tk.RIDGE to RIDGE and tk.RIGHT to RIGHT
        RightFrame = Frame(MainFrame, bd=10, width=560, height=600, relief=RIDGE, bg='black')
        RightFrame.pack(side=RIGHT)

        # ====================Div_Frame=================================================#
        # Changed tk.RIDGE to RIDGE
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

        # ================================================Variables=================================================
        # Variables must be instance variables (self.var_name) to persist and be accessible by widgets
        # Changed tk.StringVar() and tk.IntVar() to StringVar() and IntVar() due to 'from tkinter import *'
        self.AcctOpen = StringVar()
        self.AppDate = StringVar()
        self.NextCreditReview = StringVar()
        self.LastCreditReview = StringVar()
        self.DateRev = StringVar()
        self.ProdCode = StringVar()
        self.ProdType = StringVar()
        self.NoDays = StringVar()
        self.CostPDay = StringVar()
        self.CreLimit = StringVar()
        self.CreCheck = StringVar()
        self.SettDueDay = StringVar()
        self.PaymentD = StringVar()
        self.Discount = StringVar()
        self.Deposit = StringVar()
        self.PayDueDay = StringVar()
        self.PaymentM = StringVar()

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.Tax = StringVar()
        self.SubTotal = StringVar()
        self.Total = StringVar()
        self.Receipt_Ref = StringVar()

        # ================================================RightFrame0=================================================
        # Changed tk.Label to Label and tk.W to W
        self.lblAcctOpen = Label(RightFrame0, font=('arial', 18, 'bold'), text="Account Opened:", padx=2, pady=2, bg="gainsboro")
        self.lblAcctOpen.grid(row=0, column=0, sticky=W)

        # Changed textvariable=AcctOpen to textvariable=self.AcctOpen
        self.cboAcctOpen = ttk.Combobox(RightFrame0, textvariable=self.AcctOpen, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboAcctOpen['values'] = ('', 'Select an option', 'Yes', 'No')
        self.cboAcctOpen.current(0)
        self.cboAcctOpen.grid(row=0, column=1, pady=2)

        self.lblNCreR = Label(RightFrame0, font=('arial', 18, 'bold'), text="Next Credit Review:", padx=2, pady=2, bg="gainsboro")
        self.lblNCreR.grid(row=2, column=0, sticky=W)

        # Changed textvariable=NextCreditReview to textvariable=self.NextCreditReview
        self.cboNCreR = ttk.Combobox(RightFrame0, textvariable=self.NextCreditReview, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboNCreR['values'] = ('', 'Select an option', 'Yes', 'No')
        self.cboNCreR.current(0)
        self.cboNCreR.grid(row=2, column=1, pady=2)

        self.lblLCreR = Label(RightFrame0, font=('arial', 18, 'bold'), text="Last Credit Review:", padx=2, pady=2, bg="gainsboro")
        self.lblLCreR.grid(row=3, column=0, sticky=W)

        # Changed textvariable=LastCreditReview to textvariable=self.LastCreditReview
        self.cboLCreR = ttk.Combobox(RightFrame0, textvariable=self.LastCreditReview, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboLCreR['values'] = ('', 'Select an option', 'Yes', 'No')
        self.cboLCreR.current(0)
        self.cboLCreR.grid(row=3, column=1, pady=2)

        self.lblDateRev = Label(RightFrame0, font=('arial', 18, 'bold'), text="Date Review:", padx=2, pady=2, bg="gainsboro")
        self.lblDateRev.grid(row=4, column=0, sticky=W)

        # Changed textvariable=DateRev to textvariable=self.DateRev
        self.cboDateRev = ttk.Combobox(RightFrame0, textvariable=self.DateRev, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboDateRev['values'] = ('', 'Select an option', 'Yes', 'No')
        self.cboDateRev.current(0)
        self.cboDateRev.grid(row=4, column=1, pady=2)

        # ================================================RightFrame1=================================================

        # ================================================RightFrame2=================================================

        # ================================================LeftFrame0==================================================

        # ================================================LeftFrame1==================================================

        # ================================================LeftFrame2==================================================

        # ================================================LeftFrame3==================================================


if __name__=='__main__':
    root = Tk()
    application = Rental_Inventory(root)
    root.mainloop()
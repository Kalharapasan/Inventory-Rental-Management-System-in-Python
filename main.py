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
        self.Tax = StringVar() # Made self.Tax
        self.SubTotal = StringVar() # Made self.SubTotal
        self.Total = StringVar() # Made self.Total
        self.Receipt_Ref = StringVar()

        # ================================================RightFrame0=================================================
        
        self.lblAcctOpen = Label(RightFrame0, font=('arial', 18, 'bold'), text="Account Opened:", padx=2, pady=2, bg="gainsboro")
        self.lblAcctOpen.grid(row=0, column=0, sticky=W)

        
        self.cboAcctOpen = ttk.Combobox(RightFrame0, textvariable=self.AcctOpen, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboAcctOpen['values'] = ('', 'Select an option', 'Yes', 'No')
        self.cboAcctOpen.current(0)
        self.cboAcctOpen.grid(row=0, column=1, pady=2)

        self.lblNCreR = Label(RightFrame0, font=('arial', 18, 'bold'), text="Next Credit Review:", padx=2, pady=2, bg="gainsboro")
        self.lblNCreR.grid(row=2, column=0, sticky=W)

       
        self.cboNCreR = ttk.Combobox(RightFrame0, textvariable=self.NextCreditReview, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboNCreR['values'] = ('', 'Select an option', 'Yes', 'No')
        self.cboNCreR.current(0)
        self.cboNCreR.grid(row=2, column=1, pady=2)

        self.lblLCreR = Label(RightFrame0, font=('arial', 18, 'bold'), text="Last Credit Review:", padx=2, pady=2, bg="gainsboro")
        self.lblLCreR.grid(row=3, column=0, sticky=W)

        
        self.cboLCreR = ttk.Combobox(RightFrame0, textvariable=self.LastCreditReview, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboLCreR['values'] = ('', 'Select an option', 'Yes', 'No')
        self.cboLCreR.current(0)
        self.cboLCreR.grid(row=3, column=1, pady=2)

        self.lblDateRev = Label(RightFrame0, font=('arial', 18, 'bold'), text="Date Review:", padx=2, pady=2, bg="gainsboro")
        self.lblDateRev.grid(row=4, column=0, sticky=W)

        
        self.cboDateRev = ttk.Combobox(RightFrame0, textvariable=self.DateRev, state='readonly',
                                        font=('arial', 18, 'bold'), width=19)
        self.cboDateRev['values'] = ('', 'Select an option', 'Yes', 'No')
        self.cboDateRev.current(0)
        self.cboDateRev.grid(row=4, column=1, pady=2)

        # ================================================RightFrame1=================================================
        self.txtReceipt = Text(RightFrame1, pady=2, height=14, width=71, font=('arial', 9, 'bold'))
        self.txtReceipt.grid(row=0, column=0, pady=2)

        # ================================================RightFrame2=================================================
        self.lblTax = Label(RightFrame2, font=('arial', 18, 'bold'), text="Tax", padx=4, pady=1, fg="black", bg="gainsboro")
        self.lblTax.grid(row=0, column=0, sticky=W)
        
        self.txtTax = Entry(RightFrame2, textvariable=self.Tax, font=('arial', 16, 'bold'), bd=8,
                            fg="black", width=30, justify=LEFT)
        self.txtTax.grid(row=0, column=1, pady=1, padx=4)

        self.lblSubTotal = Label(RightFrame2, font=('arial', 18, 'bold'), text="Sub Total", padx=4, pady=1, fg="black", bg="gainsboro")
        self.lblSubTotal.grid(row=1, column=0, sticky=W)
        
        self.txtSubTotal = Entry(RightFrame2, textvariable=self.SubTotal, font=('arial', 16, 'bold'), bd=8,
                                fg="black", width=30, justify=LEFT)
        self.txtSubTotal.grid(row=1, column=1, pady=1, padx=4)

        self.lblTotal = Label(RightFrame2, font=('arial', 18, 'bold'), text="Total", padx=4, pady=1, fg="black", bg="gainsboro")
        self.lblTotal.grid(row=2, column=0, sticky=W)
        
        self.txtTotal = Entry(RightFrame2, textvariable=self.Total, font=('arial', 16, 'bold'), bd=8,
                            fg="black", width=30, justify=LEFT)
        self.txtTotal.grid(row=2, column=1, pady=1, padx=4)

        #==================================LeftFrame 0========================================
        self.lblProdType = Label(LeftFrame0, font=('arial', 18, 'bold'), text="Product Type:", padx=2, pady=16, bg="gainsboro")
        self.lblProdType.grid(row=0, column=0, sticky=W)

        self.cboProdType=ttk.Combobox(LeftFrame0, textvariable=self.ProdType, state='readonly', 
                                    font=('arial', 18, 'bold'), width=12)
        self.cboProdType['value'] = ('', 'Car', 'Van', 'Minibus', 'Truck')
        self.cboProdType.current(0)
        self.cboProdType.grid(row=0, column=1)

        self.lblNoDays = Label(LeftFrame0, font=('arial', 18, 'bold'), text="No of Days:", padx=2, pady=2, bg="gainsboro")
        self.lblNoDays.grid(row=0, column=2, sticky=W)

        self.cboNoDays=ttk.Combobox(LeftFrame0, textvariable=self.NoDays, state='readonly',
                                    font=('arial', 18, 'bold'), width=12)
        self.cboNoDays['value'] = ('0', '1-30', '31-90', '91-270', '271-365')
        self.cboNoDays.current(0)
        self.cboNoDays.grid(row=0, column=3)

        self.lblProdCode = Label(LeftFrame0, font=('arial', 16, 'bold'), text="Product Code:", padx=1, pady=16, bg="gainsboro")
        self.lblProdCode.grid(row=1, column=0, sticky=W)

        self.txtProdCode=Entry(LeftFrame0, textvariable=self.ProdCode, font=('arial', 16, 'bold'), bd=8,
                            fg="black", width=14, justify=LEFT).grid(row=1, column=1)

        self.lblProdCode = Label(LeftFrame0, font=('arial', 16, 'bold'), text="Product Code:", padx=1, pady=2, bg="gainsboro")
        self.lblProdCode.grid(row=1, column=2, sticky=W)

        self.txtCostPDay=Entry(LeftFrame0, textvariable=self.CostPDay, font=('arial', 16, 'bold'), bd=8,
                            fg="black", width=14, justify=LEFT).grid(row=1, column=3)

        # ================================================LeftFrame1==================================================
        
        self.lblCreLimit=Label(LeftFrame1, font=('arial', 18, 'bold'), text="Credit Limit:",padx=2,pady=2, bg="gainsboro")
        self.lblCreLimit.grid(row=0, column=0, sticky=W)

        self.cboCreLimit=ttk.Combobox(LeftFrame1, textvariable=self.CreLimit, state='readonly', 
                                    font=('arial', 18, 'bold'), width=12)
        self.cboCreLimit['value']=('', 'Select an option', '£150', '£200', '£250', '£300')
        self.cboCreLimit.current(0)
        self.cboCreLimit.grid(row=0, column=1, pady=2)

        self.lblCreCheck=Label(LeftFrame1, font=('arial', 18, 'bold'), text="Credit Check:",padx=2,pady=2, bg="gainsboro")
        self.lblCreCheck.grid(row=0, column=2, sticky=W)

        self.cboCreCheck=ttk.Combobox(LeftFrame1, textvariable=self.CreCheck, state='readonly',
                                    font=('arial', 18, 'bold'), width=10)
        self.cboCreCheck['value']=('', 'Select an option', 'Yes', 'No')
        self.cboCreCheck.current(0)
        self.cboCreCheck.grid(row=0, column=3, pady=2)

        self.lblSettDueDate=Label(LeftFrame1, font=('arial', 18, 'bold'), text="Sett. Due:",padx=2,pady=2, bg="gainsboro")
        self.lblSettDueDate.grid(row=1, column=0, sticky=W)

        self.txtSettDueDate=Entry(LeftFrame1, textvariable=self.SettDueDay, font=('arial',16,'bold'), bd=2,
                                fg="black", width=14, justify=LEFT).grid(row=1,column=1)

        self.lblPaymentD=Label(LeftFrame1, font=('arial', 18, 'bold'), text="Payment Due:",padx=1,pady=2, bg="gainsboro")
        self.lblPaymentD.grid(row=1, column=2, sticky=W)
        

        self.cboPaymentD=ttk.Combobox(LeftFrame1, textvariable=self.PaymentD, state='readonly', 
                              font=('arial', 18, 'bold'), width=10)
        self.cboPaymentD['value']=('', 'Select an option', 'Yes', 'No')
        self.cboPaymentD.current(0)
        self.cboPaymentD.grid(row=1, column=3, pady=2)

        self.lblDiscount = Label(LeftFrame1, font=('arial', 18, 'bold'), text="Discount:",padx=1,pady=2, bg="gainsboro")
        self.lblDiscount.grid(row=2, column=0, sticky=W)

        self.cboDiscount=ttk.Combobox(LeftFrame1, textvariable=self.Discount, state='readonly', 
                                    font=('arial', 18, 'bold'), width=12)
        self.cboDiscount['value']=('0','5','10','15', '20')
        self.cboDiscount.current(0)
        self.cboDiscount.grid(row=2, column=1, pady=2)

        self.lblDeposit = Label(LeftFrame1, font=('arial', 18, 'bold'), text="Deposit:",padx=1,pady=2, bg="gainsboro")
        self.lblDeposit.grid(row=2, column=2, sticky=W)

        self.cboDeposit=ttk.Combobox(LeftFrame1, textvariable=self.Deposit, state='readonly', 
                                    font=('arial', 18, 'bold'), width=10)
        self.cboDeposit['value']=('', 'Select an option', 'Yes', 'No')
        self.cboDeposit.current(0)
        self.cboDeposit.grid(row=2, column=3, pady=2)

        self.lblPayDueDateDay = Label(LeftFrame1, font=('arial', 18, 'bold'), text="Pay Day Due:",padx=1,pady=2, bg="gainsboro")
        self.lblPayDueDateDay.grid(row=3, column=0, sticky=W)

        self.txtPayDueDateDay=Entry(LeftFrame1, textvariable=self.PayDueDay, font=('arial',16,'bold'), bd=2,
                                fg="black", width=14, justify=LEFT).grid(row=3,column=1)

        self.lblPaymentM = Label(LeftFrame1, font=('arial', 18, 'bold'), text="Payment Method:",padx=0,pady=4, bg="gainsboro")
        self.lblPaymentM.grid(row=3, column=2, sticky=W)
        
        self.cboPaymentM=ttk.Combobox(LeftFrame1, textvariable=self.PaymentM, state='readonly',
                              font=('arial', 18, 'bold'), width=10)
        self.cboPaymentM['value']=('', 'Select an option', 'Cash', 'Visa Card', 'Master Card')
        self.cboPaymentM.current(0)
        self.cboPaymentM.grid(row=3, column=3, pady=2)

        # ================================================LeftFrame2==================================================
        
        LeftFrame2LL = Frame(LeftFrame2, bd=5, width=300, height=160, padx=5, bg="gainsboro", relief=RIDGE)
        LeftFrame2LL.grid(row=0, column=0)
        LeftFrame2LR = Frame(LeftFrame2, bd=5, width=300, height=160, padx=5, bg="black", relief=RIDGE)
        LeftFrame2LR.grid(row=0, column=1)
        
         # ================================================LeftFrame2LL==================================================

        self.chkCheckCredit = Checkbutton(LeftFrame2LL, text="Check Credit ", variable=self.var1, onvalue=1, offvalue=0,
                                        font=('arial', 16, 'bold'), bg="gainsboro").grid(row=0, sticky=W)

        self.chkTermAgreed = Checkbutton(LeftFrame2LL, text="Term Agreed ", variable=self.var2, onvalue=1, offvalue=0,
                                        font=('arial', 16, 'bold'), bg="gainsboro").grid(row=1, sticky=W)

        self.chkAccountOnHold = Checkbutton(LeftFrame2LL, text="Account On Hold ", variable=self.var3, onvalue=1, offvalue=0,
                                        font=('arial', 16, 'bold'), bg="gainsboro").grid(row=2, sticky=W)

        self.chkRestrictMailing = Checkbutton(LeftFrame2LL, text="Restrict Mailing ", variable=self.var4, onvalue=1, offvalue=0,
                                            font=('arial', 16, 'bold'), bg="gainsboro").grid(row=3, sticky=W)
        
        # ========================LeftFrame2LR==========================
        self.txtInfo0 = Text(LeftFrame2LR, height=2, width=63, font=('arial', 9, 'bold'))
        self.txtInfo0.grid(row=0, column=0, pady=2)

        self.txtInfo1 = Text(LeftFrame2LR, height=2, width=63, font=('arial', 9, 'bold'))
        self.txtInfo1.grid(row=1, column=0, pady=2)

        self.txtInfo2 = Text(LeftFrame2LR, height=2, width=63, font=('arial', 9, 'bold'))
        self.txtInfo2.grid(row=2, column=0, pady=2)

        self.txtInfo3 = Text(LeftFrame2LR, height=2, width=63, font=('arial', 9, 'bold'))
        self.txtInfo3.grid(row=3, column=0, pady=2)


        # ========================LeftFrame3===============================================================================
        self.btnTotal = Button(LeftFrame3, padx=33, pady=2, bd=4, fg="black", font=('arial', 20, 'bold'), width=9, height=2,
                            bg="gainsboro", text="Total").grid(row=0, column=0)

        self.btnReset = Button(LeftFrame3, padx=33, pady=2, bd=4, fg="black", font=('arial', 20, 'bold'), width=9, height=2,
                            bg="gainsboro", text="Reset").grid(row=0, column=1)

        self.btnExit = Button(LeftFrame3, padx=34, pady=2, bd=4, fg="black", font=('arial', 20, 'bold'), width=9, height=2,
                            bg="gainsboro", text="Exit").grid(row=0, column=2)


if __name__=='__main__':
    root = Tk()
    application = Rental_Inventory(root)
    root.mainloop()
'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python GFer.py
    or if it doesn't work use this one:
        python3 GFer.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''

from mpmath import *
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry , Button , Style

mp.dps = 50000; mp.pretty = True

class GFer(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("GFer")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global base
        base = StringVar()
        global exp
        exp = StringVar()
        global res
        res = StringVar()

        frame1 = Frame(self,style='My.TFrame')
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Enter the base :", width=16,background='orange')
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1,textvariable=base,style='My.TEntry')
        entry1.pack(fill=X, padx=5, expand=True)
		
        frame2 = Frame(self,style='My.TFrame')
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Enter the exponent :", width=16,background='orange')
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2,textvariable=exp,style='My.TEntry')
        entry2.pack(fill=X, padx=5, expand=True)

        
        frame3 = Frame(self,style='My.TFrame')
        frame3.pack(fill=X)

        result = Label(frame3, textvariable=res, width=22,background='orange')
        result.pack(side=LEFT, padx=70, pady=5)

		
        frame4 = Frame(self,style='My.TFrame')
        frame4.pack(fill=X)

        btntest = Button(frame4, text="Test", width=10, command=self.test,style='My.TButton')
        btntest.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclear = Button(frame4, text="Clear", width=10, command=self.clear,style='My.TButton')
        btnclear.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclose = Button(frame4, text="Close", width=10, command=self.quit,style='My.TButton')
        btnclose.pack(side=LEFT, anchor=N, padx=5, pady=5)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
    
        
    

    def test(self):
        try:
            b = int(base.get())
            n = int(exp.get())
            def polynomial(m,x):
                if m==1:
                    return x
                else:
                    p0=2
                    p1=x
                    l=2
                    while l<=m:
                        p=x*p1-p0
                        p0=p1
                        p1=p
                        l=l+1
                    return p
            def jacobi(a,q):
                j=1
                while a != 0:
                    while a%2==0:
                        a=a/2
                        if q%8==3 or q%8==5:
                            j=-j
                    #interchange(a,q)
                    c=a
                    a=q
                    q=c
                    if a%4==3 and q%4==3:
                        j=-j
                    a=fmod(a,q)
                if q==1:
                    return j
                else:
                    return 0
            F=b**2**n+1
            d=3
            while not(jacobi(d-2,F)==-1 and jacobi(d+2,F)==-1):
                d=d+1
            s=polynomial(b/2,polynomial(b/2,d))%F
            ctr=1
            while ctr<=2**n-2:
                s=polynomial(b,s)%F
                ctr=ctr+1
            if int(s)==0:
                value=str(b) + "^2^" + str(n) + "+1 is prime"
                res.set(self.makeAsItIs(value))
            else:
                value=str(b) + "^2^" + str(n) + "+1 is composite"
                res.set(self.makeAsItIs(value))
            

          
        except:
            self.errorMsg('error')
			
    def clear(self):
        try:
            res.set('')
            base.set('')
            exp.set('')
        except:
            self.errorMsg('error')
			
    
    def makeAsItIs(self, value):
        return value

def main():
    root = Tk()
    root.resizable(0,0)
    s = Style()
    s.configure('My.TFrame', background='orange')
    s.configure('My.TButton', background='light gray')
    s.configure('My.TEntry', fieldbackground='light gray')
    root.geometry("300x112")
    gfer = GFer(root)
    root.mainloop()

if __name__ == '__main__':
    main()

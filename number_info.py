from tkinter import *

window = Tk()

def prime():
   try :
      n = int(e1.get())
      if n > 1 :
         for i in range(2,n):
            if n%i == 0:
               t1.delete('1.0',END)
               t1.insert(END,"COMOSITE NUMBER")
               break
         else:
            t1.delete('1.0',END)
            t1.insert(END,"PRIME NUMBER")
      else:
         t1.delete('1.0',END)
         t1.insert(END,"COMOSITE NUMBER")
   except :
      t1.delete('1.0',END)
      t1.insert(END,"ERROR")            


def reverse():
   try : 
      n = int(e1.get())
      f = 0
      while n > 0 :
         i = n % 10
         f = f * 10 + i
         n = n // 10
      t2.delete('1.0',END)
      t2.insert(END,f)
   except :
      t2.delete('1.0',END)
      t2.insert(END,"ERROR") 

def palindrome() :
   try : 
      n = int(e1.get())
      j = n
      f = 0
      while j > 0 :
         i = j % 10
         f = f * 10 + i
         j = j // 10
      if n == f :
            t3.delete('1.0',END)
            t3.insert(END,"It's a Palindrome")
      else :
         t3.delete('1.0',END)
         t3.insert(END,"It is NOT a Palindrome")
   except:
      t3.delete('1.0',END)
      t3.insert(END,"ERROR") 

def cube():
   try:
      result = float(e1.get())**3
      t4.delete('1.0',END)
      t4.insert(END,result)           
   except :
      t4.delete('1.0',END)
      t4.insert(END,"ERROR")  

def cube_root():
   try:
      result = float(e1.get())**(1/3)
      t5.delete('1.0',END)
      t5.insert(END,result)           
   except :
      t5.delete('1.0',END)
      t5.insert(END,"ERROR")

def square():
   try:
      result = float(e1.get())**2
      t6.delete('1.0',END)
      t6.insert(END,result)           
   except :
      t6.delete('1.0',END)
      t6.insert(END,"ERROR")

def square_root():
   try:
      result = float(e1.get())**(1/2)
      t7.delete('1.0',END)
      t7.insert(END,result)           
   except :
      t7.delete('1.0',END)
      t7.insert(END,"ERROR")
 
l1 = Label(window,height = 1,width = 17,text="Enter the number")
l1.grid(row=0,column=0)

b1 = Button(window,height = 1,width = 17,text="PRIME or COMPOSITE",command=prime)
b1.grid(row=1,column=0)

b2 = Button(window,height = 1,width = 17,text="REVERSE",command=reverse)
b2.grid(row=2,column=0)

b3 = Button(window,height = 1,width = 17,text="PALINDROME",command=palindrome)
b3.grid(row=3,column=0)

b4 = Button(window,height = 1,width = 17,text="CUBE",command=cube)
b4.grid(row=4,column=0)

b5 = Button(window,height = 1,width = 17,text="CUBE ROOT",command=cube_root)
b5.grid(row=5,column=0)

b6 = Button(window,height = 1,width = 17,text="SQUARE",command=square)
b6.grid(row=6,column=0)

b7 = Button(window,height = 1,width = 17,text="SQUARE ROOT",command=square_root)
b7.grid(row=7,column=0)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = Text(window,height = 1,width = 25)
t1.grid(row = 1 , column =1)

t2 = Text(window,height = 1,width = 25)
t2.grid(row = 2 , column =1)

t3 = Text(window,height = 1,width = 25)
t3.grid(row = 3 , column =1)

t4 = Text(window,height = 1,width = 25)
t4.grid(row = 4 , column =1)

t5 = Text(window,height = 1,width = 25)
t5.grid(row = 5 , column =1)

t6 = Text(window,height = 1,width = 25)
t6.grid(row = 6 , column =1)

t7 = Text(window,height = 1,width = 25)
t7.grid(row = 7 , column =1)


window.mainloop() 

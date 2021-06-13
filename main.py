from tkinter import *
#Easy Weekend Project
root = Tk()
root.title("Ezy Calculator")

main_num=Entry(root,width=50)
main_num.grid(row=0,column=0,columnspan=3,pady=10,padx=10)

def button_click(num):
    current=main_num.get()
    main_num.delete(0,END)
    main_num.insert(0,str(current)+str(num))

def button_delete():
    current=main_num.get()
    deleted_current=current[0:len(current)-1]
    main_num.delete(0,END)
    main_num.insert(0,str(deleted_current))

def button_clear():
    main_num.delete(0,END)

def button_add():
    first_num=main_num.get()
    global numm
    global math
    math="addition"
    numm=int(first_num)
    main_num.delete(0,END)

def button_equal():
    sec_number=main_num.get()
    main_num.delete(0,END)
    if math=="addition":
        main_num.insert(0,numm+int(sec_number))
    elif math=="subtraction":
        main_num.insert(0, numm - int(sec_number))
    elif math=="division":
        main_num.insert(0, numm / int(sec_number))
    elif math=="multiplication":
        main_num.insert(0, numm * int(sec_number))

def button_subtract():
    first_num = main_num.get()
    global numm
    global math
    math = "subtraction"
    numm = int(first_num)
    main_num.delete(0, END)

def button_divide():
    first_num = main_num.get()
    global numm
    global math
    math = "division"
    numm = int(first_num)
    main_num.delete(0, END)

def button_multiply():
    first_num = main_num.get()
    global numm
    global math
    math = "multiplication"
    numm = int(first_num)
    main_num.delete(0, END)


butoon_1=Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
butoon_2=Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
butoon_3=Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
butoon_4=Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
butoon_5=Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
butoon_6=Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
butoon_7=Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
butoon_8=Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
butoon_9=Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
butoon_0=Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
button_plus=Button(root,text="+",padx=40,pady=20,command=button_add)
button_equal=Button(root,text="=",padx=40,pady=20,command=button_equal)
button_clear=Button(root,text="Clear",padx=40,pady=20,command=button_clear)
button_delete=Button(root,text="Delete",padx=40,pady=20,command=button_delete)
button_subtract=Button(root,text="-",padx=40,pady=20,command=button_subtract)
button_multiply=Button(root,text="*",padx=40,pady=20,command=button_multiply)
button_divide=Button(root,text="/",padx=40,pady=20,command=button_divide)

butoon_1.grid(row=1,column=0)
butoon_2.grid(row=1,column=1)
butoon_3.grid(row=1,column=2)
butoon_4.grid(row=2,column=0)
butoon_5.grid(row=2,column=1)
butoon_6.grid(row=2,column=2)
butoon_7.grid(row=3,column=0)
butoon_8.grid(row=3,column=1)
butoon_9.grid(row=3,column=2)
butoon_0.grid(row=4,column=0)
button_plus.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_delete.grid(row=5,column=0)
button_clear.grid(row=5,column=1)

root.mainloop()
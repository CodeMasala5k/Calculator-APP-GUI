from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        ans = eval(scvalue.get())
        scvalue.set(str(ans))
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


root = Tk()
root.geometry("644x900")
root.title("CODE MASALA - Calculator")
p1 = PhotoImage(file= "Icon.png")
root.iconphoto(False, p1)

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=20)

f =  Frame(root)
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)

for i in range (1,4):
    b = Button(f, text=f"{i}", padx=40,pady=10, font = "lucida 25 bold", bg="black", foreground="white")
    b.bind("<Button-1>", click)
    b.pack(side=LEFT,padx=20,pady=10)

for j in range (4,7):
    b = Button(f1, text=f"{j}", padx=40,pady=10, font = "lucida 25 bold", bg="black", foreground="white")
    b.bind("<Button-1>", click)
    b.pack(side=LEFT,padx=20,pady=10)

for k in range (7,10):
    b = Button(f2, text=f"{k}", padx=40,pady=10, font = "lucida 25 bold", bg="black", foreground="white")
    b.bind("<Button-1>", click)
    b.pack(side=LEFT,padx=20,pady=10)


b = Button(f3, text="0", padx=40,pady=10, font = "lucida 25 bold", bg="black", foreground="white")
b.bind("<Button-1>", click)
b.pack(side=LEFT,padx=20,pady=10)

b = Button(f3, text="-", padx=40,pady=10, font = "lucida 25 bold", bg="black", foreground="white")
b.bind("<Button-1>", click)
b.pack(side=LEFT,padx=20,pady=10)

b = Button(f3, text="+", padx=40,pady=10, font = "lucida 25 bold", bg="black", foreground="white")
b.bind("<Button-1>", click)
b.pack(side=LEFT,padx=20,pady=10)

b = Button(f4, text="*", padx=40,pady=10, font = "lucida 25 bold", bg="black", foreground="white")
b.bind("<Button-1>", click)
b.pack(side=LEFT,padx=20,pady=10)

b = Button(f4, text="/", padx=40,pady=10, font = "lucida 25 bold", bg="black", foreground="white")
b.bind("<Button-1>", click)
b.pack(side=LEFT,padx=20,pady=10)

b = Button(f4, text="=", padx=40,pady=10, font = "lucida 25 bold", bg="black", foreground="white")
b.bind("<Button-1>", click)
b.pack(side=LEFT,padx=20,pady=10)

b = Button(f5, text="%", padx=40,pady=10, font = "lucida 25 bold", bg="black", foreground="white")
b.bind("<Button-1>", click)
b.pack(side=LEFT,padx=20,pady=10)

b = Button(f5, text="C", padx=90,pady=10, font = "lucida 25 bold", bg="black", foreground="white")
b.bind("<Button-1>", click)
b.pack(side=LEFT,padx=40,pady=10)

f3.pack()
f4.pack()
f2.pack()
f1.pack()
f.pack()
f5.pack()

root.mainloop()
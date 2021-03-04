from tkinter import*
import wikipedia

def searc():
    value=tb.get()
    text.delete(1.0,END)
    try:
        avalue=wikipedia.summary(value)
        text.insert(INSERT,avalue)
    except:
        text.insert(INSERT,"please check your input")
win=Tk()
win.geometry("300x300")
win.title("search app")
win.config(bg="lime")

tb=Entry(win,width=25,justify=CENTER)
tb.pack(padx=10,pady=10)

btn=Button(win,width=10,text="search",command=searc,justify=CENTER)
btn.pack(padx=15,pady=20)

frame=Frame(win)

scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=Y)

text=Text(frame,width=25,height=6,wrap=WORD)
text.pack()

scroll.config(command=text.yview)

frame.pack()

win.mainloop()

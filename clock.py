from tkinter import *
from time import strftime
root= Tk()
root.title('digital clock')
root.geometry('400x50')
text= ('Boulder',20,'bold')
lbl= Label(root,font=text)
lbl.pack(anchor='center')
def time():
    livetime= strftime('%H:%M:%S %Z')
    lbl.config(text=livetime)
    lbl.after(1000,time)
time()    
mainloop()
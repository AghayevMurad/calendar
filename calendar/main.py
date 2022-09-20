from tkinter import*
from tkcalendar import *
 

root=Tk()

def selectDate():
     myDate=mycal.get_date()
     selectDate=Label(text=myDate)
     selectDate.pack(padx=2,pady=2)

mycal=Calendar(root,setmode="day",Date_pattern="d/m//yy")
mycal.pack(padx=15,pady=15)

open_cal=Button(root,text="select Date",command=selectDate)
open_cal.pack(padx=15,pady=15)

root.geometry("300x300")
root.title("Calendar")
root.configure(bg="Green")
root.mainloop()
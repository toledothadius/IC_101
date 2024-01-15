from tkinter import *
import calendar

win=Tk()
win.title("Calendar")

def text():
    month_str=month.get()
    year_str=year.get()
    month_int=int(month_str)
    year_int=int(year_str)
    cal=calendar.month(year_int,month_int)
    textfield.delete(0.0,END)
    textfield.insert(INSERT,cal)

#This is Month Label
monthLabel=Label(win,text="Month :")
monthLabel.grid(row=0,column=0)

#creating a spinbox for Month from 1 to 12
month=Spinbox(win,from_=1,to=12,width=5)
month.grid(row=1,column=0)

#This is Year Label
yearLabel=Label(win,text="Year :")
yearLabel.grid(row=0,column=1)

#creating a spinbox for Year from 1970 to 2100
year=Spinbox(win,from_=1970,to=2100,width=12)
year.grid(row=1,column=1,padx=8)

#Creating a Go button with command to display the calendar in TextField
button=Button(win,text="GO",command=text)
button.grid(row=1,column=2)


textfield=Text(win,height=10,width=25,foreground="blue")
textfield.grid(row=3,columnspan=3)

win.mainloop()
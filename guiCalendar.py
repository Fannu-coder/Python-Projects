from tkinter import *
import calendar

def calendar_see():
  window=Tk()
  window.config(background="gray")
  window.title("Complete your Calendar")
  window.geometry("570x620")
  get_year=int(year_entry.get())
  window_content=calendar.calendar(get_year)

  year_cal=Label(window,text=window_content,font=("poppins",10,"bold"))
  year_cal.grid(row=5,column=1,padx=20)

  window.mainloop()

if __name__=='__main__':
  root=Tk()
  root.config(background="black")
  root.title("GUI Calendar")
  root.geometry("280x170")

  name=Label(root,text="Calendar",bg="silver",font=("poppins",20,"bold"))
  name.grid(row=1,column=1)

  year=Label(root,text="Enter Year",bg="blue",font=("poppins",20,"bold"))
  year.grid(row=2,column=1)

  year_entry=Entry(root,font=("poppins",15,"bold"))
  year_entry.grid(row=3,column=1)

  show_button=Button(root,text="show Calendar!",fg="red",bg="white",font=("poppins",15,"bold"),command=calendar_see)
  show_button.grid(row=4,column=1)

  root.mainloop()
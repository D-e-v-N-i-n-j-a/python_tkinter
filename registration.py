import http
from tkinter import *

root = Tk();

root.geometry("500x500")
# VALIDATE FIELDS
def getData(self,event):
    firstNameVariable = event;



Label(root,text="USER REGISTRATION FORM",font="arial 15 bold").grid(row= 0,column = 3)

# OUR LABEL FIELD HERE
first_name = Label(root,text="FIRST NAME")
last_name = Label(root,text="LAST NAME")
age = Label(root,text="AGE")
gender = Label(root,text="GENDER")
phone = Label(root,text="PHONE")

#PACK ALL LABEL HERE
first_name.grid(row=1,column=2)
last_name.grid(row=2,column=2)
age.grid(row=3,column=2)
gender.grid(row=4,column=2)
phone.grid(row=4,column=2)

# VARIABLES HERE
firstNameVariable = StringVar
lastNameVariable = StringVar
ageVariable = StringVar
genderVariable = StringVar
phoneVariable = StringVar
checkVariable = IntVar 

# PLACE ENTRY FIELD HERE
first_name_entry = Entry(root,textvariable=firstNameVariable,width=50)
lastNameEntry = Entry(root,textvariable=lastNameVariable,width=50)
ageEntry = Entry(root,textvariable=ageVariable,width=50)
genderEntry = Entry(root,textvariable=ageVariable,width=50)
phoneEntry = Entry(root,textvariable=phoneVariable,width=50)

# PACK ENTRY HERE
first_name_entry.grid(row=1,column=3)
lastNameEntry.grid(row=2,column=3)
ageEntry.grid(row=3,column=3)
genderEntry.grid(row=4,column=3)
phoneEntry.grid(row=1,column=3)

# CHECKBOX

checkBtn = Checkbutton(text="Remember me",variable=checkVariable)
checkBtn.grid(row=6,column=3)

# SUBMIT BUTTON
Button(text="Submit",command=getData).grid(row=7,column=3)


 



root.mainloop()
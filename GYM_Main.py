from tkinter import *        # GUI
from tkinter import ttk      # Tab
import mysql.connector       # Connecting MySql with python
from datetime import date    # Date and Time from datetime import datetime
import tkinter.messagebox    # Message pop up



# Connecting Gym database with python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aakash",
    database="gym"
)


root = Tk()
root.title("Gym")     # Set the title of the window
root.minsize(width=667, height=507)    # Minimum Size of Window
root.maxsize(width=700, height=555)    # Maximum Size of window
root.iconbitmap("cc.ico")   # Set the icon only in ico format


notebook = ttk.Notebook(root)  # widget that manages a collection of windows/displays


# creating New Frames for all processes and set it's background color black
Welcome = Frame(notebook, bg="black")
New_registration = Frame(notebook, bg="black")
Delete_record = Frame(notebook, bg="black")
Pay_fee = Frame(notebook, bg="black")


notebook.add(Welcome, text="Welcome Page")
notebook.add(New_registration, text="New Registration")
notebook.add(Delete_record, text="Delete Record")
notebook.add(Pay_fee, text="Pay Fee")
notebook.add(Welcome, text="Welcome Page")

notebook.pack(expand=True, fill="both")  # expand = expand to fill any space


# New Registration Tab Design

def clear():
    """Function for clearing the inputs from the Window"""
    selected_gender.set(False)
    selected_name.set("")
    selected_age.set("")
    selected_mobile.set("")
    selected_address.set("")
    selected_plan.set(False)
    selected_coach.set(False)


def submit():
    """This Function store all the details of new registration in registration table gym database"""



    mycursor = mydb.cursor()

    sql = "INSERT INTO registration (name, age, mobile, address, gender, personal_coach, plan, register_date, pending_amount)" \
          " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (selected_name.get(), selected_age.get(), selected_mobile.get(), selected_address.get(), selected_gender.get()
           , selected_coach.get(), selected_plan.get(), date.today(), "0")
    mycursor.execute(sql, val)

    mydb.commit()  # mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

    tkinter.messagebox.showinfo('New Registration',
                                'Successfully Added')  # Pop up window that show record successfully added

    clear()


# Label for Name Age Mobile no. Address
Label(New_registration, text="You Are Registering With Us", bg="black", fg="white", font=("Times", 28)).place(x=105,
                                                                                                              y=40)
Label(New_registration, text="Name", bg="black", fg="white", font=("Helvetica", 14)).place(x=138, y=110)
Label(New_registration, text="Age", bg="black", fg="white", font=("Helvetica", 14)).place(x=138, y=160)
Label(New_registration, text="Mobile no.", bg="black", fg="white", font=("Helvetica", 14)).place(x=138, y=210)
Label(New_registration, text="Address", bg="black", fg="white", font=("Helvetica", 14)).place(x=138, y=260)
Label(New_registration, text="Personal Coach", bg="black", fg="white", font=("Helvetica", 18)).place(x=280, y=305)
Label(New_registration, text="Plans", bg="black", fg="white", font=("Helvetica", 18)).place(x=30, y=100)

# Variables for storing values of 1.Name 2.Age 3.Mobile no. 4.Gender 5.Address 6.Plan 7.coach
selected_name = StringVar()
selected_age = StringVar()
selected_mobile = StringVar()
selected_gender = StringVar()
selected_address = StringVar()
selected_plan = StringVar()
selected_coach = StringVar()

# Radio Button for Gender, Personal Coach And Plan
selected_gender.set(False)  # set the initial value of both False
selected_coach.set(False)
selected_plan.set(False)

# Set the variable of both the radio button same for making them mutually exclusive
Radiobutton(New_registration, text="MALE", value="male", font=("Helvetica", 10), variable=selected_gender).place(x=60,
                                                                                                                 y=310)
Radiobutton(New_registration, text="FEMALE", value="female", font=("Helvetica", 10), variable=selected_gender).place(
    x=140, y=310)
Radiobutton(New_registration, text="Yes", value="Yes", font=("Helvetica", 12), variable=selected_coach).place(x=470,
                                                                                                              y=310)
Radiobutton(New_registration, text="No", value="No", font=("Helvetica", 12), variable=selected_coach).place(x=535,
                                                                                                            y=310)
Radiobutton(New_registration, text="Basic", value="Basic", font=("Helvetica", 10), variable=selected_plan).place(x=30,
                                                                                                                 y=140)
Radiobutton(New_registration, text="Gold", value="Gold", font=("Helvetica", 10), variable=selected_plan).place(x=30,
                                                                                                               y=180)
Radiobutton(New_registration, text="Diamond", value="Diamond", font=("Helvetica", 10), variable=selected_plan).place(
    x=30, y=220)
Radiobutton(New_registration, text="Platinum", value="Platinum", font=("Helvetica", 10), variable=selected_plan).place(
    x=30, y=260)

# Entry Box for input Variable
Entry(New_registration, textvariable=selected_name, font=("Helvetica", 14)).place(x=250, y=110)
Entry(New_registration, textvariable=selected_age, font=("Helvetica", 14)).place(x=250, y=160)
Entry(New_registration, textvariable=selected_mobile, font=("Helvetica", 14)).place(x=250, y=210)
Entry(New_registration, textvariable=selected_address, font=("Helvetica", 14)).place(x=250, y=260)

# Button for submit the detail
Button(New_registration, command=submit, text="Submit", bg="black", fg="white", font=("Helvetica", 14)).place(x=265,
                                                                                                              y=360)

# Designing the Welcome Tab

# Label For displaying Text
Label(Welcome, text="Welcome in Aakash's GYM", bg="black", fg="white", font=("Times", 28)).place(x=105, y=30)
Label(Welcome, text="Basic plan -> 17.00 per/day ", bg="black", fg="white", font=("Helvetica", 14)).place(x=110, y=110)
Label(Welcome, text="Gold plan -> 27.00 per/day ", bg="black", fg="white", font=("Helvetica", 14)).place(x=110, y=140)
Label(Welcome, text="Diamond plan -> 40 per/day ", bg="black", fg="white", font=("Helvetica", 14)).place(x=110, y=170)
Label(Welcome, text="Platinum plan -> 50 per/day ", bg="black", fg="white", font=("Helvetica", 14)).place(x=110, y=200)
Label(Welcome, text="Address -> ABC Road Near XYZ", bg="black", fg="white", font=("Helvetica", 14)).place(x=280, y=305)
Label(Welcome, text="Pincode -> 123456 ", bg="black", fg="white", font=("Helvetica", 14)).place(x=280, y=335)
Label(Welcome, text="Contact No. -> 987654321, 123456789 ", bg="black", fg="white", font=("Helvetica", 14)).place(x=280,
                                                                                                                  y=365)

# Displaying picture on window
photo1 = PhotoImage(file="a.png")
Label(Welcome, image=photo1).place(x=20, y=300)
photo2 = PhotoImage(file="b.png")
Label(Welcome, image=photo2).place(x=430, y=80)




# Designing The Delete Record Tab


def clear1():
    """Function for clearing the inputs from the Window"""
    selected_mobile1.set("")
    selected_name1.set("")


def delete():
    """Function for deleting the record from the registration table GYM database"""
    mycursor = mydb.cursor()

    sql = "DELETE FROM registration WHERE mobile = '%s'" % selected_mobile1.get()

    mycursor.execute(sql)

    mydb.commit()  # It is required to make the changes, otherwise no changes are made to the table.
    tkinter.messagebox.showinfo('Deleting Record',
                                'Successfully Deleted')  # Pop up window that show record successfully added
    clear1()


# Label For displaying Text
Label(Delete_record, text="Deleting Your Record...", bg="black", fg="white", font=("Times", 28)).place(x=135, y=30)
Label(Delete_record, text="Name", bg="black", fg="white", font=("Helvetica", 14)).place(x=138, y=110)
Label(Delete_record, text="Mobile no.", bg="black", fg="white", font=("Helvetica", 14)).place(x=138, y=160)

# Variables for storing values of 1.Name 2.Mobile number
selected_name1 = StringVar()
selected_mobile1 = StringVar()

# Entry Box for input Variable
Entry(Delete_record, textvariable=selected_name1, font=("Helvetica", 14)).place(x=250, y=110)
Entry(Delete_record, textvariable=selected_mobile1, font=("Helvetica", 14)).place(x=250, y=160)

# Displaying picture on window
photo3 = PhotoImage(file="d.png")
Label(Delete_record, image=photo3).place(x=60, y=280)

# Button for deleting the record
Button(Delete_record, command=delete, text="Delete", bg="black", fg="white", font=("Helvetica", 16)).place(x=265, y=210)







# Designing The Pay fee Tab

def pay():


    def pay_fee():
        """This function pop up a message of successful payment"""

        tkinter.messagebox.showinfo('Fee Pay',
                                    'Successfully Payed')  # Pop up window that show record successfully added

        mycursor = mydb.cursor()

        sql = "UPDATE registration SET register_date = ('%s') WHERE mobile = ('%s')"
        data = (date.today(), selected_mobile2.get())

        mycursor.execute(sql, data)

        mydb.commit()









    # Extracting the Plan, Personal_coach, register_date, pending_amount from registration table

    mycursor = mydb.cursor()

    mycursor.execute("SELECT plan, personal_coach, register_date, pending_amount"
                     " FROM registration WHERE mobile ='%s'" % selected_mobile2.get())
    myresult = mycursor.fetchall()

    # storing Plan as p, personal_coach as c, register_date as d, pending_amount as p_a


    # variable for storing fetched data
    plan = StringVar()
    coach = StringVar()
    date1 = StringVar()
    total_amount = StringVar()
    pending_amount = StringVar()
    amount = StringVar()

    p = "a"
    c = "a"
    d = "a"
    p_a = "a"


    for row in myresult:
        p = row[0]
        c = row[1]
        d = row[2]
        p_a = row[3]

    plan.set("%s" % p)
    coach.set("%s" % c)
    pending_amount.set("%s" % p_a)

    d = d - date.today()
    d = d.days


    if p == "Basic":
        c = d * 17
        total_amount.set("%s" % c)
    elif p == "Gold":
        c = d * 27
        total_amount.set("%s" % c)
    elif p == "Diamond":
        c = d * 40
        total_amount.set("%s" % c)
    else:
        c = d * 50
        total_amount.set("%s" % c)

    p_a = p_a + c
    pending_amount.set("%s" % p_a)


    date1.set("%s" % d)

    Label(Pay_fee, textvariable=plan, bg="black", fg="white", font=("Helvetica", 14)).place(x=200, y=280)
    Label(Pay_fee, textvariable=coach, bg="black", fg="white", font=("Helvetica", 14)).place(x=290, y=280)
    Label(Pay_fee, textvariable=date1, bg="black", fg="white", font=("Helvetica", 14)).place(x=200, y=330)
   # Label(Pay_fee, textvariable=total_amount, bg="black", fg="white", font=("Helvetica", 14)).place(x=230, y=380)
    Label(Pay_fee, textvariable=pending_amount, bg="black", fg="white", font=("Helvetica", 14)).place(x=230, y=380)



    Label(Pay_fee, text="Plan and Coach -> " , bg="black", fg="white",
          font=("Helvetica", 14)).place(x=38, y=280)
    Label(Pay_fee, text="Number of days ->", bg="black", fg="white", font=("Helvetica", 14)).place(x=38, y=330)
    #Label(Pay_fee, text="Total Amount to pay ->", bg="black", fg="white", font=("Helvetica", 14)).place(x=38, y=380)
    Label(Pay_fee, text="You have to pay ->", bg="black", fg="white", font=("Helvetica", 14)).place(x=38, y=380)
    Label(Pay_fee, text="Amount", bg="black", fg="white", font=("Helvetica", 14)).place(x=340, y=340)
    Entry(Pay_fee, textvariable=amount, font=("Helvetica", 14)).place(x=435, y=340)

    Button(Pay_fee, command=pay_fee, text="Pay", bg="black", fg="white", font=("Helvetica", 16)).place(x=430, y=390)
    print(amount.get())

    mycursor = mydb.cursor()

    sql = "UPDATE registration SET pending_amount = '%s' WHERE mobile = '%s'" % p_a % selected_mobile2.get()

    mycursor.execute(sql)

    mydb.commit()








# Label For displaying Text
Label(Pay_fee, text="Paying Monthly Fee...", bg="black", fg="white", font=("Times", 28)).place(x=140, y=30)
Label(Pay_fee, text="Name", bg="black", fg="white", font=("Helvetica", 14)).place(x=138, y=110)
Label(Pay_fee, text="Mobile no.", bg="black", fg="white", font=("Helvetica", 14)).place(x=138, y=160)

# Variables for storing values of 1.Name 2.Mobile number
selected_name2 = StringVar()
selected_mobile2 = StringVar()

# Entry Box for input Variable
Entry(Pay_fee, textvariable=selected_name2, font=("Helvetica", 14)).place(x=250, y=110)
Entry(Pay_fee, textvariable=selected_mobile2, font=("Helvetica", 14)).place(x=250, y=160)

# Button for deleting the record
Button(Pay_fee, command=pay, text="Ready", bg="black", fg="white", font=("Helvetica", 16)).place(x=265, y=210)

# Run the window in a  infinite loop until we cross it
root.mainloop()

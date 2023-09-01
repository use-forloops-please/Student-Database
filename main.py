from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import Database
from tkintermapview import TkinterMapView
from tkinter.messagebox import askyesno
from PIL import ImageTk, Image
import re
import customtkinter
import subprocess
import sys
import time

customtkinter.set_appearance_mode("light")

root = customtkinter.CTk()  # create CTk window like you do with the Tk window

db = Database("Students.db") #set db as Students table
# root = Tk()
root.title("Student Management System")
root.geometry("1920x1080+0+0")
# root.resizable(False, False)
root.config(bg="#153160")
root.state("zoomed")

name = StringVar()
surname = StringVar()
email = StringVar()
gender = StringVar()
contact = StringVar()
campus = StringVar()
degree = StringVar()

# Entries Frame
entries_frame = customtkinter.CTkFrame(root)
# entries_frame.pack(side=TOP, fill=X)

canvas = Canvas(root, width = 135, height = 135) #create canvas placement for image
canvas.grid(row=0, column=0, padx=10, pady=10)
img = ImageTk.PhotoImage(Image.open("eduvos_logo.jpeg")) # load image from file
canvas.create_image(-5, -5, anchor=NW, image=img) #

##logo image##
title = customtkinter.CTkLabel(master=root, text="STUDENT MANAGEMENT SYSTEM", text_font=("Roboto Medium", 18), text_color="white")
title.grid(row=0, column=1, padx=0, pady=20)

# Name - Label and Entry
lblName = customtkinter.CTkLabel(master=root, text="Name", text_font=("Roboto Medium", -16), text_color="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")

txtName = customtkinter.CTkEntry(master=root, width=300, textvariable=name, text_font=("Roboto Medium", -16))
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Surname - Label and Entry

lblSurname = customtkinter.CTkLabel(master=root, text="Surname", text_font=("Roboto Medium", -16), text_color="white")
lblSurname.grid(row=1, column=2, padx=10, pady=10, sticky="w")

txtSurname = customtkinter.CTkEntry(master=root, width=300, textvariable=surname, text_font=("Roboto Medium", -16))
txtSurname.grid(row=1, column=3, padx=10, pady=10, sticky="w")

# E-mail - Label and Entry
lblEmail = customtkinter.CTkLabel(master=root, text="Email", text_font=("Roboto Medium", -16), text_color="white")
lblEmail.grid(row=2, column=0, padx=10, pady=15, sticky="w")

txtEmail = customtkinter.CTkEntry(master=root, width=300, textvariable=email, text_font=("Roboto Medium", -16))
txtEmail.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Gender - Label and Combobox
lblGender = customtkinter.CTkLabel(master=root, text="Gender", text_font=("Roboto Medium", -16), text_color="white")
lblGender.grid(row=2, column=2, padx=10, pady=15, sticky="w")
comboGender = customtkinter.CTkComboBox(master=root, text_font=("Roboto Medium", -16), width=300, variable=gender,
                                        values=["Female", "Male"], bg="black")
comboGender.grid(row=2, column=3, padx=10, sticky="w")

# Contact - Label and Entry
lblContact = customtkinter.CTkLabel(master=root, text="Contact", text_font=("Roboto Medium", -16), text_color="white")
lblContact.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txtContact = customtkinter.CTkEntry(master=root, width=300, textvariable=contact, text_font=("Roboto Medium", -16))
txtContact.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Campus - Label and Combobox
lblCampus = customtkinter.CTkLabel(master=root, text="Campus", text_font=("Roboto Medium", -16), text_color="white")
lblCampus.grid(row=3, column=2, padx=10, pady=10, sticky="w")
comboCampus = customtkinter.CTkComboBox(master=root, text_font=("Roboto Medium", -16), width=300, variable=campus,
                                        state="normal", values=['Tygervalley', "Claremont", "Durban", "Nelson Mandela Bay",
                                                                "East London",
                                              "Bedfordview", "Midrand", "Vanderbijlpark", "Pretoria", "Bloemfontein",
                                              "Mbombela", "Potchefstroom"
                                                                ])
comboCampus.grid(row=3, column=3, padx=10, pady=10, sticky="w")

# Degree - Label and Entry
lblDegree = customtkinter.CTkLabel(master=root, text="Degree", text_font=("Roboto Medium", -16), text_color="white")
lblDegree.grid(row=4, column=0, padx=10, pady=15, sticky="w")

txtDegree = customtkinter.CTkEntry(master=root, width=300, textvariable=degree, text_font=("Roboto Medium", -16))
txtDegree.grid(row=4, column=1, padx=10, pady=10, sticky="w")

# Campus ListBox
slctCampus = customtkinter.CTkLabel(master=root, text="Select Campus:", text_font=("Roboto Medium", -18), text_color="white")
slctCampus.place(relx=0.7, rely=0.15)

listbox = customtkinter.CTkOptionMenu(master=root,
                                      values=["Tygervalley", "Claremont", "Durban", "Nelson Mandela Bay", "East London",
                                              "Bedfordview", "Midrand", "Vanderbijlpark", "Pretoria", "Bloemfontein",
                                              "Mbombela", "Potchefstroom"
                                              ], fg_color="white", text_color="#153160", dropdown_color="white", text_font=("Roboto Medium", -16))
listbox.place(relx=0.8, rely=0.15)

# Map View
map_widget = TkinterMapView(master=root, corner_radius=0)
map_widget.place(width=555, height=280, relx=0.70, rely=0.2)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

map_widget.set_marker(-33.8706505, 18.6381351, text="Tygervalley Campus")
map_widget.set_marker(-33.9832147, 18.4699982, text="Claremont")
map_widget.set_marker(-29.7213518, 31.0719163, text="Durban")
map_widget.set_marker(-33.9538902, 25.5848943, text="Nelson Mandela Bay")
map_widget.set_marker(-32.99351200588712, 27.909801454784997, text="East London")
map_widget.set_marker(-26.171668990589744, 28.134008583417007, text="Bedfordview")
map_widget.set_marker(-26.02049316787268, 28.13366939690451, text="Midrand")
map_widget.set_marker(-26.696654227385125, 27.832171259871068, text="Vanderbijlpark")
map_widget.set_marker(-25.77678010730726, 28.26894446806185, text="Pretoria")
map_widget.set_marker(-29.110563763313575, 26.206737810482657, text="Bloemfontein")
map_widget.set_marker(-25.443441125030493, 30.96291518339789, text="Mbombela")
map_widget.set_marker(-26.695731183274155, 27.094780641103636, text="Potchefstroom")

map_widget.set_position(-33.8706505, 18.6381351)
map_widget.set_zoom(10)

################################
def mapcampus():

    if (listbox.get() == "Tygervalley"):   # tygervalley campus
            map_widget.set_position(-33.8706505, 18.6381351)
            map_widget.set_zoom(10)

    if (listbox.get() == "Claremont"): # Claremont
            map_widget.set_position(-33.9832147,18.4699982)
            map_widget.set_zoom(10)

    if (listbox.get() == "Durban"):  # Durban
        map_widget.set_position(-29.7213518,31.0719163)
        map_widget.set_zoom(10)

    if (listbox.get() == "Nelson Mandela Bay"): # Nelson Mandela Bay
            map_widget.set_position(-33.9538902,25.5848943)
            map_widget.set_zoom(10)

    if (listbox.get() == "East London"): # East London
            map_widget.set_position(-32.99351200588712, 27.909801454784997)
            map_widget.set_zoom(10)

    if (listbox.get() == "Bedfordview"): # Bedfordview
            map_widget.set_position(-26.171668990589744, 28.134008583417007)
            map_widget.set_zoom(10)

    if (listbox.get() == "Midrand"): # Midrand
            map_widget.set_position(-26.02049316787268, 28.13366939690451)
            map_widget.set_zoom(10)

    if (listbox.get() == "Vanderbijlpark"): # Vanderbijlpark
            map_widget.set_position(-26.696654227385125, 27.832171259871068)
            map_widget.set_zoom(10)

    if (listbox.get() == "Pretoria"): # Pretoria
            map_widget.set_position(-25.77678010730726, 28.26894446806185)
            map_widget.set_zoom(10)

    if (listbox.get() == "Bloemfontein"): # Bloemfontein
            map_widget.set_position(-29.110563763313575, 26.206737810482657)
            map_widget.set_zoom(10)

    if (listbox.get() == "Mbombela"): # Mbombela
            map_widget.set_position(-25.443441125030493, 30.96291518339789)
            map_widget.set_zoom(10)

    if (listbox.get() == "Potchefstroom"): # Potchefstroom
            map_widget.set_position(-26.695731183274155, 27.094780641103636)
            map_widget.set_zoom(10)


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    surname.set(row[2])
    email.set(row[3])
    gender.set(row[4])
    contact.set(row[5])
    campus.set(row[6])
    degree.set(row[7])


def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_student():
    if (
            validation_name() and validation_surname() and validation_email() and validation_contact() and validation_degree() and comboCampus.get() != "" and comboGender.get() != ""):
        db.insert(txtName.get(), txtSurname.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
                  comboCampus.get(),
                  txtDegree.get())
        messagebox.showinfo("Success!", "Record Inserted.")
        clearAll()
        displayAll()
    else:
        if comboCampus.get() == "":
            messagebox.showerror("Input Error!", "A campus was not selected...")
        elif comboGender.get() == "":
            messagebox.showerror("Input Error!", "A gender was not selected...")
        return


def update_student():
    if (
            validation_name() and validation_surname() and validation_email() and validation_contact() and validation_degree()):
        db.update(row[0], txtName.get(), txtSurname.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
                  comboCampus.get(), txtDegree.get())
        messagebox.showinfo("Success!", "Record Updated.")
        clearAll()
        displayAll()
    else:
        return


def delete_students():
    db.remove(row[0])
    messagebox.showinfo("Record Deleted!", "Record has been deleted.")
    clearAll()
    displayAll()


def clear_filter():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)
    messagebox.showinfo("Campus filter", "Now displaying all campuses!")
    listbox.set("Tygervalley")


def print_campus():
    tv.delete(*tv.get_children())
    for row in db.get_students(listbox.get()):
        tv.insert("", END, values=row)
    messagebox.showinfo("Success!", (listbox.get() + "'s students are displayed!"))


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
    sys.exit()


def log_out():
    answer = askyesno(title='confirmation',
                    message='Are you sure that you want to log off?')
    if answer:
        subprocess.Popen(['python', 'Login_menu.py'])
        countdown(1)


def clearAll():
    name.set("")
    surname.set("")
    email.set("")
    gender.set("")
    campus.set("")
    contact.set("")
    degree.set("")


def validation_name():
    string = txtName.get()
    if (string == ""):
        messagebox.showerror("Input Error!", "Name field is empty...")
    else:
        if (len(string) < 3):
            messagebox.showerror("Input Error!", "Name field is too short...")
        else:
            if (re.match('^[0-9]*$', string)):
                messagebox.showerror("Input Error!", "Name field contains digits...")
            else:
                return True


def validation_surname():
    string = txtSurname.get()
    if (string == ""):
        messagebox.showerror("Input Error!", "Surname field is empty...")
    else:
        if (len(string) < 3):
            messagebox.showerror("Input Error!", "Surname field is too short...")
        else:
            if (re.match('^[0-9]*$', string)):
                messagebox.showerror("Input Error!", "Surname field contains digits...")
            else:
                return True


def validation_email():
    string = txtEmail.get()
    if (string == ""):
        messagebox.showerror("Input Error!", "Email field is empty...")
    else:
        if (len(string) < 8):
            messagebox.showerror("Input Error!", "Email field is too short...")
        else:
            return True


def validation_contact():
    string = txtContact.get()
    if (string == ""):
        messagebox.showerror("Input Error!", "Contact field is empty...")
    else:
        if (len(string) != 10):
            messagebox.showerror("Input Error!", "Contact field is too short...")
        else:
            if (re.match('^[0-9]*$', string) == True):
                messagebox.showerror("Input Error!", "Contact field should only contain digits...")
            else:
                return True


def validation_degree():
    string = txtDegree.get()
    if (string == ""):
        messagebox.showerror("Input Error!", "Degree field is empty...")
    else:
        if (len(string) <= 3):
            messagebox.showerror("Input Error!", "Degree field is too short...")
        else:
            if (re.match('^[0-9]*$', string)):
                messagebox.showerror("Input Error!", "Degree field should not contain digits...")
            else:
                return True


# Buttons

btnAdd = customtkinter.CTkButton(master=root, command=add_student, text="Add Details", height=40, bg="#16a085", bd=0, fg_color="white", text_color="#153160", hover_color="#c4daff", text_font=("Roboto Medium", -16))
btnAdd.place(relx=0.11, rely=0.5)

btnEdit = customtkinter.CTkButton(master=root, command=update_student, text="Update Details", height=40, bg="#16a085", bd=0, fg_color="white", text_color="#153160", hover_color="#c4daff", text_font=("Roboto Medium", -16))
btnEdit.place(relx=0.21, rely=0.5)

btnDelete = customtkinter.CTkButton(master=root, command=delete_students, text="Delete Details", height=40, fg_color="#bf3b53", hover_color="#962e41", bg="#16a085", text_color="white", bd=0, text_font=("Roboto Medium", -16))
btnDelete.place(relx=0.31, rely=0.5)

btnClear = customtkinter.CTkButton(master=root, command=clearAll, text="Clear Details", height=40, bg="#16a085", bd=0, fg_color="white", text_color="#153160", hover_color="#c4daff", text_font=("Roboto Medium", -16))
btnClear.place(relx=0.41, rely=0.5)

btnCampus = customtkinter.CTkButton(master=root, text="Show Students", command=print_campus, fg_color="white", text_color="#153160", hover_color="#c4daff", text_font=("Roboto Medium", -16), height=40)
btnCampus.place(relx=0.7, rely=0.5)

btnClearCampus = customtkinter.CTkButton(master=root, text="Clear Filter", command=clear_filter, fg_color="white", text_color="#153160", hover_color="#c4daff",  text_font=("Roboto Medium", -16), height=40)
btnClearCampus.place(relx=0.8, rely=0.5)

btnMapcampus = customtkinter.CTkButton(master=root, text="Map Campus", command=mapcampus, fg_color="white", text_color="#153160", hover_color="#c4daff", text_font=("Roboto Medium", -16), height=40)
btnMapcampus.place(relx=0.9, rely=0.5)

btnLogOut = customtkinter.CTkButton(master=root, text="Log out", command=log_out, fg_color="#bf3b53", hover_color="#962e41", text_color="white", text_font=("Roboto Medium", -16), height=40)
btnLogOut.place(relx=0.9, rely=0.04)

# Table Frame
tree_frame = customtkinter.CTkFrame(master=root)
tree_frame.place(x=0, y=480, width=1920, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 15),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=2)
tv.heading("2", text="Name")
tv.column("2", width=6)
tv.heading("3", text="Surname")
tv.column("3", width=10)
tv.heading("4", text="E-mail")
tv.column("4", width=25)
tv.heading("5", text="Gender")
tv.column("5", width=3)
tv.heading("6", text="Contact")
tv.column("6", width=8)
tv.heading("7", text="Campus")
tv.column("7", width=6)
tv.heading("8", text="Degree")
tv.column("8", width=5)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

displayAll()
root.mainloop()

import subprocess
import sys
import time
from tkinter import *
import os
import customtkinter
from PIL import Image, ImageTk
from tkinter import messagebox


def countdown_exit(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
    sys.exit()


def countdown_main(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
    subprocess.Popen(['python', 'main.py'])


# Implementing event on login button
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()

        else:
            password_not_recognised()

    else:
        user_not_found()


def login_success():
    messagebox.showinfo('Success', 'You have been successfully logged in!')
    countdown_main(1)
    countdown_exit(1)


# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found
def user_not_found():
    messagebox.showerror("Input Error!", "User does not exist!")


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def login_exit():
    subprocess.Popen(['python', 'login_menu.py'])
    countdown_exit(1)



def login():
    global login_screen
    login_screen = customtkinter.CTk()
    # login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("800x550+563+200")
    login_screen.resizable(False, False)
    # p1 = PhotoImage(file='eduvos_logo.jpeg')
    # login_screen.iconphoto(False, p1)

    login_screen.image = ImageTk.Image.open("Background.jpeg")
    login_screen.bg = ImageTk.PhotoImage(login_screen.image)
    login_screen.bg_image = customtkinter.CTkLabel(image=login_screen.bg).place(x=0, y=2, relwidth=1, relheight=1)

    # Label
    # customtkinter.CTkLabel(text="Please enter the details below to login:", bg="White", width=300, height=2, text_font=("Arial Black", 13)).pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    # Frame
    Frame_Login = customtkinter.CTkFrame(fg_color="#153160", bg_color="#153160")
    Frame_Login.place(x=230, y=75, width=400, height=500)

    canvas = customtkinter.CTkCanvas(master=Frame_Login, width=135, height=135, border=0)
    canvas.place(relx=0.5, rely=0.2, anchor=CENTER)
    img = ImageTk.PhotoImage(Image.open("eduvos_logo.jpeg"))
    canvas.create_image(-5, -5, anchor=NW, image=img)

    # Username - Label and Entry
    customtkinter.CTkLabel(master=Frame_Login, text="Username:", text_font=("Roboto Medium", -16), height=2, text_color="white").place(relx=0.1, rely=0.4)
    username_login_entry = customtkinter.CTkEntry(master=Frame_Login, textvariable=username_verify, text_font=("Roboto Medium", -16), width=200)
    username_login_entry.place(relx=0.19, rely=0.46)

    # Password - Label and Entry
    customtkinter.CTkLabel(master=Frame_Login, text="Password:", text_font=("Roboto Medium", -16), height=2, text_color="white").place(relx=0.1, rely=0.55)
    password_login_entry = customtkinter.CTkEntry(master=Frame_Login, textvariable=password_verify, show='*', text_font=("Roboto Medium", -16), width=200)
    password_login_entry.place(relx=0.19, rely=0.6)

    # Buttons
    btn_login = customtkinter.CTkButton(master=Frame_Login, text="Login", height=40, width=100, text_font=("Roboto Medium", -16), command=login_verify)
    btn_login.place(relx=0.3, rely=0.82, anchor=CENTER)
    btn_exit = customtkinter.CTkButton(master=Frame_Login, text="Back", height=40, width=100, text_font=("Roboto Medium", -16), command=login_exit)
    btn_exit.place(relx=0.7, rely=0.82, anchor=CENTER)

    login_screen.mainloop()


login()
import subprocess
import sys
import time
import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


def countdown_exit(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
    sys.exit()


def countdown_menu(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
    subprocess.Popen(['python', 'login_menu.py'])


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    messagebox.showinfo("Successful registration!", "You will now be returned to the main menu...")
    countdown_menu(1)
    countdown_exit(1)


def register_exit():
    subprocess.Popen(['python', 'login_menu.py'])
    countdown_exit(1)


def register():
    global register_screen
    register_screen = customtkinter.CTk()
    # register_screen = Tk()
    register_screen.title("Register")
    register_screen.geometry("800x550+563+200")
    register_screen.resizable(False, False)
    # p1 = PhotoImage(file='Icon.png')
    # register_screen.iconphoto(False, p1)

    # background image
    register_screen.image = ImageTk.Image.open("Background.jpeg")
    register_screen.bg = ImageTk.PhotoImage(register_screen.image)
    register_screen.bg_image = Label(image=register_screen.bg).place(x=0, y=0, relwidth=1, relheight=1)

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    # Frame
    Frame_Login = customtkinter.CTkFrame(fg_color="#153160", bg_color="#153160")
    Frame_Login.place(x=230, y=75, width=400, height=500)

    canvas = customtkinter.CTkCanvas(master=Frame_Login, width=135, height=135, border=0)
    canvas.place(relx=0.5, rely=0.2, anchor=CENTER)
    img = ImageTk.PhotoImage(Image.open("eduvos_logo.jpeg"))
    canvas.create_image(-5, -5, anchor=NW, image=img)

    # Username - Label and Entry
    customtkinter.CTkLabel(master=Frame_Login, text="Username:", text_font=("Roboto Medium", -16), height=2, text_color="white").place(relx=0.1, rely=0.4)
    username_entry = customtkinter.CTkEntry(master=Frame_Login, textvariable=username, text_font=("Roboto Medium", -16), width=200)
    username_entry.place(relx=0.19, rely=0.46)

    # Password - Label and Entry
    customtkinter.CTkLabel(master=Frame_Login, text="Password:", text_font=("Roboto Medium", -16), height=2, text_color="white").place(relx=0.1, rely=0.55)
    password_entry = customtkinter.CTkEntry(master=Frame_Login, textvariable=password, show='*', text_font=("Roboto Medium", -16), width=200)
    password_entry.place(relx=0.19, rely=0.6)

    # Buttons
    btn_register = customtkinter.CTkButton(master=Frame_Login, text="Register", height=40, width=100, text_font=("Roboto Medium", -16), command=register_user)
    btn_register.place(relx=0.3, rely=0.82, anchor=CENTER)
    btn_exit = customtkinter.CTkButton(master=Frame_Login, text="Back", height=40, width=100, text_font=("Roboto Medium", -16), command=register_exit)
    btn_exit.place(relx=0.7, rely=0.82, anchor=CENTER)

    register_screen.mainloop()


register()
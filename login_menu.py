import subprocess
import sys
import time
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import askyesno


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
    sys.exit()


def menu_login():
    subprocess.Popen(['python', 'login_login.py'])
    countdown(1)


def menu_register():
    subprocess.Popen(['python', 'login_register.py'])
    countdown(1)


def menu_exit():
    answer = askyesno(title='confirmation', message='Are you sure that you want to exit?')
    if answer:
        exit()


def main_account_screen():
    global main_screen
    # main_screen = Tk()
    main_screen = customtkinter.CTk()
    main_screen.title("Menu")
    main_screen.geometry("800x550+563+200")
    main_screen.resizable(False, False)
    # p1 = PhotoImage(file='logo.jpg')
    # main_screen.iconphoto(False, p1)

    # Background Images
    main_screen.image = ImageTk.Image.open("Background.jpeg")
    main_screen.bg = ImageTk.PhotoImage(main_screen.image)
    main_screen.bg_image = customtkinter.CTkLabel(image=main_screen.bg).place(x=0, y=2, relwidth=1, relheight=1)

    # Frame
    Frame_Login = customtkinter.CTkFrame(fg_color="#153160", bg_color="#153160")
    Frame_Login.place(x=230, y=75, width=400, height=500)

    canvas = customtkinter.CTkCanvas(master=Frame_Login, width=135, height=135, border=0)
    canvas.place(relx=0.5, rely=0.2, anchor=CENTER)
    img = ImageTk.PhotoImage(Image.open("eduvos_logo.jpeg"))
    canvas.create_image(-5, -5, anchor=NW, image=img)

    # Buttons
    btn_login = customtkinter.CTkButton(master=Frame_Login, text="Login", height=40, text_font=("Roboto Medium", -16), command=menu_login, fg_color="white", text_color="#153160", hover_color="#c4daff")
    btn_login.place(relx=0.5, rely=0.5, anchor=CENTER)
    btn_register = customtkinter.CTkButton(master=Frame_Login, text="Register", height=40, text_font=("Roboto Medium", -16), command=menu_register, fg_color="white", text_color="#153160", hover_color="#c4daff")
    btn_register.place(relx=0.5, rely=0.65, anchor=CENTER)
    btn_exit = customtkinter.CTkButton(master=Frame_Login, text="Exit", height=40, text_font=("Roboto Medium", -16), command=menu_exit, fg_color="white", text_color="#153160", hover_color="#c4daff")
    btn_exit.place(relx=0.5, rely=0.8, anchor=CENTER)

    main_screen.mainloop()


main_account_screen()
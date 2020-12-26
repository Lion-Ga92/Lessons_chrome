from tkinter import *
from tkinter import ttk
import sys

root = Tk()
root.geometry("700x420")
root.resizable(False, False)
frame_1 = Frame(root)
frame_1.pack()
frame_2 = Frame(root)
frame_2.pack()
txt_greet = Text(frame_1, width=50, height=10)
txt_greet.pack()

def wish_joy():
    txt_greet.insert("1.0", "To all my friends and Famly!")
    root.after(2000, merry_xmas)

def merry_xmas():
    txt_greet.insert("2.0", "\nA Very Merry Christmas!!!! ")
    root.after(1000, happy_new_year)

def happy_new_year():
    txt_greet.insert("3.0", "\nAnd a joyful and happy New Years!!!\n From us at the Garcia Family!!!!!!")

bttn_joy = Button(frame_2, text="Merry Christmas!!!", command=wish_joy)
bttn_joy.pack()

def close_app():
    exit()


bttn_clr = Button(frame_2, text="Good bye!!", command=close_app)
bttn_clr.pack()
root.mainloop()

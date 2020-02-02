from tkinter import *
from tkinter import Tk, font

def main():
    root = Tk()
    root.title("Launcher")
    root.geometry("500x500")

    # ----- Widgets -----
    var = StringVar()
    title_label = Label(root, textvariable = var)
    title_label.config(font=("Courier", 18))
    var.set("A MineSweeper made for Ants")



    # ----- /Widgets -----

    title_label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
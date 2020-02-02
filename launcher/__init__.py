from tkinter import *
from tkinter import Tk, font, ttk
import game
import subprocess

def newgame_callback():
    print("New Game button clicked")

    game.main()  # temporary solution

def main():
    root = Tk()
    root.title("Launcher")
    # root.geometry("500x500")
    # root.resizable(width=False, height=False)

    # ----- Fonts -----
    title_font = font.Font(family="Courier", size=21, weight="normal")
    # ----- /Fonts -----

    # ----- Title -----
    title_var = StringVar()
    title_var.set("A MineSweeper made for Ants")
    title_label = Label(root, textvariable = title_var, font=title_font)
    # ----- /Title -----

    # ----- Dimensions submenu -----
    dimensions_separator = ttk.Separator(root, orient=HORIZONTAL)

    dimensions_var = StringVar()
    dimensions_var.set("Dimensions:")
    dimensions_label = Label(root, textvariable = dimensions_var)

    dimensions_separator_end = ttk.Separator(root, orient=HORIZONTAL)

    dimensions_radiobutton_var = IntVar()
    dimensions_radiobutton1 = Radiobutton(root, text="Game Mode", variable=dimensions_radiobutton_var, value=1)
    dimensions_radiobutton2 = Radiobutton(root, text="Fullscreen Game", variable=dimensions_radiobutton_var, value=2)
    dimensions_radiobutton3 = Radiobutton(root, text="Custom", variable=dimensions_radiobutton_var, value=3)

    # ----- /Dimensions submenu -----

    # ----- Bombs submenu -----
    bombs_separator = ttk.Separator(root, orient=HORIZONTAL)

    bombs_var = StringVar()
    bombs_var.set("Bombs:")
    bombs_label = Label(root, textvariable = bombs_var)

    bombs_separator_end = ttk.Separator(root, orient=HORIZONTAL)

    bombs_checkbutton_var = IntVar()
    bombs_radiobutton1 = Radiobutton(root, text="Standard", variable=bombs_checkbutton_var, value=1)
    bombs_radiobutton2 = Radiobutton(root, text="Number", variable=bombs_checkbutton_var, value=2)
    bombs_radiobutton3 = Radiobutton(root, text="Ratio", variable=bombs_checkbutton_var, value=3)

    # ----- /Bombs submenu -----

    # ----- Tilesize submenu -----
    tilesize_separator = ttk.Separator(root, orient=HORIZONTAL)

    tilesize_var = StringVar()
    tilesize_var.set("Tile Size:")
    tilesize_label = Label(root, textvariable = tilesize_var)

    tilesize_separator_end = ttk.Separator(root, orient=HORIZONTAL)
    # ----- /Tilesize submenu -----

    # ----- Fitsscreen submenu -----
    fitsscreen_separator = ttk.Separator(root, orient=HORIZONTAL)

    fitsscreen_var = StringVar()
    fitsscreen_var.set("Fits Screen?")
    fitsscreen_label = Label(root, textvariable = fitsscreen_var)

    fitsscreen_separator_end = ttk.Separator(root, orient=HORIZONTAL)
    # ----- /Fitsscreen submenu -----

    # ----- Newgame submenu -----
    newgame_separator = ttk.Separator(root, orient=HORIZONTAL)

    newgame_button = Button(root, text ="New Game", command = newgame_callback)
    newgame_separator_end = ttk.Separator(root, orient=HORIZONTAL)
    # ----- /Newgame submenu -----

    # ----- About submenu -----
    about_var = StringVar()
    about_var.set("\u00A9 2020 Andreas Kuoppa")
    about_label = Label(root, textvariable = about_var)
    # ----- /About submenu -----

    # ----- Packing -----
    title_label.pack()

    dimensions_separator.pack(fill="x")
    dimensions_label.pack()
    dimensions_separator_end.pack(fill="x")

    dimensions_radiobutton1.pack(anchor="w")
    dimensions_radiobutton2.pack(anchor="w")
    dimensions_radiobutton3.pack(anchor="w")

    bombs_separator.pack(fill="x")
    bombs_label.pack()
    bombs_separator_end.pack(fill="x")

    bombs_radiobutton1.pack(anchor="w")
    bombs_radiobutton2.pack(anchor="w")
    bombs_radiobutton3.pack(anchor="w")

    tilesize_separator.pack(fill="x")
    tilesize_label.pack()
    tilesize_separator_end.pack(fill="x")

    fitsscreen_separator.pack(fill="x")
    fitsscreen_label.pack()
    fitsscreen_separator_end.pack(fill="x")

    newgame_separator.pack(fill="x")
    newgame_button.pack()
    newgame_separator_end.pack(fill="x")

    about_label.pack()
    # ----- /Packing -----

    root.mainloop()


if __name__ == "__main__":
    main()
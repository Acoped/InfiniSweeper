from tkinter import *
from tkinter import Tk, font, ttk

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
    # ----- /Dimensions submenu -----

    # ----- Bombs submenu -----
    bombs_separator = ttk.Separator(root, orient=HORIZONTAL)

    bombs_var = StringVar()
    bombs_var.set("Bombs:")
    bombs_label = Label(root, textvariable = bombs_var)
    # ----- /Bombs submenu -----

    # ----- Tilesize submenu -----
    tilesize_separator = ttk.Separator(root, orient=HORIZONTAL)

    tilesize_var = StringVar()
    tilesize_var.set("Tile Size:")
    tilesize_label = Label(root, textvariable = tilesize_var)
    # ----- /Tilesize submenu -----

    # ----- Fitsscreen submenu -----
    fitsscreen_separator = ttk.Separator(root, orient=HORIZONTAL)

    fitsscreen_var = StringVar()
    fitsscreen_var.set("Fits Screen?")
    fitsscreen_label = Label(root, textvariable = fitsscreen_var)
    # ----- /Fitsscreen submenu -----

    # ----- Packing -----
    title_label.pack()

    dimensions_separator.pack(fill="x")
    dimensions_label.pack()

    bombs_separator.pack(fill="x")
    bombs_label.pack()

    tilesize_separator.pack(fill="x")
    tilesize_label.pack()

    fitsscreen_separator.pack(fill="x")
    fitsscreen_label.pack()
    # ----- /Packing -----

    root.mainloop()


if __name__ == "__main__":
    main()
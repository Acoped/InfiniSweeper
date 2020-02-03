from tkinter import *
from tkinter import Tk, font, ttk
import game
from PIL import Image, ImageTk

def newgame_callback():
    print("New Game button clicked")

    game.main()  # temporary solution

def main():
    root = Tk()
    root.title("Launcher")
    # root.geometry("500x500")
    # root.resizable(width=False, height=False)

    # ----- Fonts -----
    title_font = font.Font(size=21, weight="normal")
    fit_font = font.Font(size=12, weight="normal")
    nofit_font = font.Font(size=12, weight="normal")
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
    dimensions_radiobutton2 = Radiobutton(root, text="Fullscreen Game (w? x h?)", variable=dimensions_radiobutton_var, value=2)
    dimensions_radiobutton3 = Radiobutton(root, text="Custom (____ x ____)", variable=dimensions_radiobutton_var, value=3)

    variable = StringVar(root)
    variable.set("Small (? x ?)")  # default value

    dimensions_optionmenu = OptionMenu(root, variable, "Small (w? x h?)", "Medium (w? x h?)", "Large (w? x h?)", "Classic Small (9 x 9)", "Classic Medium (16 x 30)", "Classic Large (30 x 16)")
    dimensions_optionmenu.config(width=30)
    dimensions_optionmenu.config(bg="LIGHTBLUE")
    dimensions_optionmenu.config(activebackground="RED")
    dimensions_optionmenu["menu"].config(bg="WHITE")

    # ----- /Dimensions submenu -----

    # ----- Bombs submenu -----
    bombs_separator = ttk.Separator(root, orient=HORIZONTAL)

    bombs_var = StringVar()
    bombs_var.set("Bombs:")
    bombs_label = Label(root, textvariable = bombs_var)

    bombs_separator_end = ttk.Separator(root, orient=HORIZONTAL)

    bombs_checkbutton_var = IntVar()
    bombs_radiobutton1 = Radiobutton(root, text="Standard (X % ratio)", variable=bombs_checkbutton_var, value=1)
    bombs_radiobutton2 = Radiobutton(root, text="Number (____ bombs)", variable=bombs_checkbutton_var, value=2)
    bombs_radiobutton3 = Radiobutton(root, text="Ratio (____ %)", variable=bombs_checkbutton_var, value=3)

    # ----- /Bombs submenu -----

    # ----- Tilesize submenu -----
    tilesize_separator = ttk.Separator(root, orient=HORIZONTAL)

    tilesize_var = StringVar()
    tilesize_var.set("Tile Set:")
    tilesize_label = Label(root, textvariable = tilesize_var)

    tilesize_separator_end = ttk.Separator(root, orient=HORIZONTAL)

    tilesize_frame = Frame(root)

    tilesize_in_pixels = IntVar()
    tilesize_radiobutton1 = Radiobutton(tilesize_frame, text="64 x 64 (Child/Retiree)", variable=tilesize_in_pixels, value=64)
    tilesize_radiobutton2 = Radiobutton(tilesize_frame, text="32 x 32 (Human)", variable=tilesize_in_pixels, value=32)
    tilesize_radiobutton3 = Radiobutton(tilesize_frame, text="16 x 16 (Inhuman)", variable=tilesize_in_pixels, value=16)
    tilesize_radiobutton4 = Radiobutton(tilesize_frame, text="8 x 8 (Ant)", variable=tilesize_in_pixels, value=8)

    L_image = Image.open("../resources/tiles/L/YYY.png")
    L_photo = ImageTk.PhotoImage(L_image)
    L_label = Label(tilesize_frame, image=L_photo)
    L_label.image = L_photo  # keep a reference!

    M_image = Image.open("../resources/tiles/M/YYY.png")
    M_photo = ImageTk.PhotoImage(M_image)
    M_label = Label(tilesize_frame, image=M_photo)
    M_label.image = M_photo  # keep a reference!

    S_image = Image.open("../resources/tiles/S/YYY.png")
    S_photo = ImageTk.PhotoImage(S_image)
    S_label = Label(tilesize_frame, image=S_photo)
    S_label.image = S_photo  # keep a reference!

    XS_image = Image.open("../resources/tiles/XS/YYY.png")
    XS_photo = ImageTk.PhotoImage(XS_image)
    XS_label = Label(tilesize_frame, image=XS_photo)
    XS_label.image = XS_photo  # keep a reference!

    # ----- /Tilesize submenu -----

    # ----- Fitsscreen submenu -----
    fitsscreen_separator = ttk.Separator(root, orient=HORIZONTAL)

    fitsscreen_var = StringVar()
    fitsscreen_var.set("Fits Screen?")
    fitsscreen_label = Label(root, textvariable = fitsscreen_var)

    fitsscreen_separator_end = ttk.Separator(root, orient=HORIZONTAL)

    fit_var = StringVar()
    fit_var.set("YES, the board fits the screen!")
    fit_label = Label(root, textvariable = fit_var, font=fit_font)

    nofit_var = StringVar()
    nofit_var.set("NO, the board does NOT fit the screen!")
    nofit_label = Label(root, textvariable = nofit_var, font=nofit_font)
    # ----- /Fitsscreen submenu -----

    # ----- Newgame submenu -----
    newgame_separator = ttk.Separator(root, orient=HORIZONTAL)

    newgame_button = Button(root, text ="New Game", command = newgame_callback, font=title_font)
    newgame_separator_end = ttk.Separator(root, orient=HORIZONTAL)
    # ----- /Newgame submenu -----

    # ----- About submenu -----
    about_var = StringVar()
    about_var.set("\u00A9 2020 Andreas Kuoppa")
    about_label = Label(root, textvariable = about_var)
    # ----- /About submenu -----

    # ----- Packing (and gridding...) -----
    title_label.pack()

    dimensions_separator.pack(fill="x")
    dimensions_label.pack()
    dimensions_separator_end.pack(fill="x")

    dimensions_radiobutton1.pack(anchor="w")
    dimensions_optionmenu.pack(anchor="w")
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

    tilesize_frame.pack()

    tilesize_radiobutton1.grid(row=0, column=0, sticky="w")
    tilesize_radiobutton2.grid(row=1, column=0, sticky="w")
    tilesize_radiobutton3.grid(row=2, column=0, sticky="w")
    tilesize_radiobutton4.grid(row=3, column=0, sticky="w")

    L_label.grid(row=0, column=1, sticky="w")
    M_label.grid(row=1, column=1, sticky="w")
    S_label.grid(row=2, column=1, sticky="w")
    XS_label.grid(row=3, column=1, sticky="w")

    fitsscreen_separator.pack(fill="x")
    fitsscreen_label.pack()
    fitsscreen_separator_end.pack(fill="x")

    fit_label.pack()
    nofit_label.pack()

    newgame_separator.pack(fill="x")
    newgame_button.pack(pady=8)
    # newgame_separator_end.pack(fill="x")

    about_label.pack()
    # ----- /Packing (and gridding...) -----

    root.mainloop()


if __name__ == "__main__":
    main()
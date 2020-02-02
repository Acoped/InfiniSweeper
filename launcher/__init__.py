from tkinter import *
from tkinter import Tk, font, ttk
import game

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
    dimensions_radiobutton3 = Radiobutton(root, text="Custom", variable=dimensions_radiobutton_var, value=3)

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
    bombs_radiobutton2 = Radiobutton(root, text="Number", variable=bombs_checkbutton_var, value=2)
    bombs_radiobutton3 = Radiobutton(root, text="Ratio", variable=bombs_checkbutton_var, value=3)

    # ----- /Bombs submenu -----

    # ----- Tilesize submenu -----
    tilesize_separator = ttk.Separator(root, orient=HORIZONTAL)

    tilesize_var = StringVar()
    tilesize_var.set("Tile Set:")
    tilesize_label = Label(root, textvariable = tilesize_var)

    tilesize_separator_end = ttk.Separator(root, orient=HORIZONTAL)

    tilesize_checkbutton_var = IntVar()
    tilesize_radiobutton1 = Radiobutton(root, text="64 x 64 (large)", variable=tilesize_checkbutton_var, value=1)
    tilesize_radiobutton2 = Radiobutton(root, text="32 x 32 (normal)", variable=tilesize_checkbutton_var, value=2)
    tilesize_radiobutton3 = Radiobutton(root, text="16 x 16 (small)", variable=tilesize_checkbutton_var, value=3)
    tilesize_radiobutton4 = Radiobutton(root, text="8 x 8 (ant)", variable=tilesize_checkbutton_var, value=4)
    tilesize_radiobutton5 = Radiobutton(root, text="4 x 4 (binary)", variable=tilesize_checkbutton_var, value=5)
    tilesize_radiobutton6 = Radiobutton(root, text="1 x 1 (pixel)", variable=tilesize_checkbutton_var, value=6)

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

    # ----- Packing -----
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

    tilesize_radiobutton1.pack(anchor="w")
    tilesize_radiobutton2.pack(anchor="w")
    tilesize_radiobutton3.pack(anchor="w")
    tilesize_radiobutton4.pack(anchor="w")
    tilesize_radiobutton5.pack(anchor="w")
    tilesize_radiobutton6.pack(anchor="w")

    fitsscreen_separator.pack(fill="x")
    fitsscreen_label.pack()
    fitsscreen_separator_end.pack(fill="x")

    fit_label.pack()
    nofit_label.pack()

    newgame_separator.pack(fill="x")
    newgame_button.pack(pady=8)
    newgame_separator_end.pack(fill="x")

    about_label.pack()
    # ----- /Packing -----

    root.mainloop()


if __name__ == "__main__":
    main()
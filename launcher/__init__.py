from tkinter import *
from tkinter import Tk, font, ttk
import game
from PIL import Image, ImageTk
import math



class Launcher():

    def newgame_callback(self, width, height, bombs, fullscreen, screen_width, screen_height, increased_border, tile_sz_px):
        print("New Game button clicked")

        print(width, height)

        game.main(width, height, bombs, tile_sz_px, fullscreen, increased_border, [120, 72], [int(screen_width), int(screen_height)], 60, "InfiniSweeper")  # temporary solution

    def bombs_callback(self, sv=None):
        ratio = float(self.sv.get())
        # Need to get width and height here, to calculate number of total cells, then ratio of that, rounded up!
        w = int(self.dimensions_entry_width.get())
        h = int(self.dimensions_entry_height.get())
        bombs =  math.ceil(ratio * 0.01 * w * h)

        print(ratio, w, h)

        self.bombs_entry_number.delete(0, "end")

        self.bombs_entry_number.insert(0, str(bombs))

    def main(self):
        root = Tk()
        root.title("Launcher")
        # root.geometry("500x500")
        root.resizable(width=False, height=False)

        # ----- Fonts -----
        title_font = font.Font(size=21, weight="normal")
        fit_font = font.Font(size=12, weight="normal")
        nofit_font = font.Font(size=12, weight="normal")
        separator_font = font.Font(weight="normal")
        # ----- /Fonts -----

        # ----- Title -----
        title_var = StringVar()
        title_var.set("InfiniSweeper")
        title_label = Label(root, textvariable = title_var, font=title_font)
        # ----- /Title -----

        # ----- resolutions submenu -----
        resolutions_separator = ttk.Separator(root, orient=HORIZONTAL)

        resolutions_var = StringVar()
        resolutions_var.set("Screen Resolution (for fullscreen mode):")
        resolutions_label = Label(root, textvariable = resolutions_var, font=separator_font)

        resolutions_separator_end = ttk.Separator(root, orient=HORIZONTAL)

        resolutions_frame = Frame(root)

        resolutions_entry_width_label = Label(resolutions_frame, text="Width:")
        self.resolutions_entry_width = Spinbox(resolutions_frame, from_=0, to_=999999)
        resolutions_entry_width_cells_label = Label(resolutions_frame, text="px")

        resolutions_entry_height_label = Label(resolutions_frame, text="Height:")
        self.resolutions_entry_height = Spinbox(resolutions_frame, from_=0, to_=999999)
        resolutions_entry_height_cells_label = Label(resolutions_frame, text="px")

        resolutions_checkbutton_var = IntVar()
        resolutions_checkbutton = Checkbutton(
            resolutions_frame, text="Full Screen",
            variable=resolutions_checkbutton_var)
        # ----- /resolutions submenu -----

        # ----- Dimensions submenu -----
        dimensions_separator = ttk.Separator(root, orient=HORIZONTAL)

        dimensions_var = StringVar()
        dimensions_var.set("Dimensions:")
        dimensions_label = Label(root, textvariable = dimensions_var, font=separator_font)

        dimensions_separator_end = ttk.Separator(root, orient=HORIZONTAL)

        dimensions_frame = Frame(root)

        dimensions_entry_width_label = Label(dimensions_frame, text="Width:")
        self.dimensions_entry_width = Spinbox(dimensions_frame, from_=9, to_=1000, command=self.bombs_callback)
        dimensions_entry_width_cells_label = Label(dimensions_frame, text="cells")

        dimensions_entry_height_label = Label(dimensions_frame, text="Height:")
        self.dimensions_entry_height = Spinbox(dimensions_frame, from_=9, to_=1000, command=self.bombs_callback)
        dimensions_entry_height_cells_label = Label(dimensions_frame, text="cells")
        # ----- /Dimensions submenu -----

        # ----- Bombs submenu -----
        bombs_separator = ttk.Separator(root, orient=HORIZONTAL)

        bombs_var = StringVar()
        bombs_var.set("Bombs:")
        bombs_label = Label(root, textvariable = bombs_var, font=separator_font)

        bombs_separator_end = ttk.Separator(root, orient=HORIZONTAL)

        bombs_frame = Frame(root)

        bombs_radiobutton1 = Label(bombs_frame, text="Number")
        bombs_radiobutton2 = Label(bombs_frame, text="Ratio")

        bombs_entry_number_label = Label(bombs_frame, text="bombs")
        self.bombs_entry_number = Spinbox(bombs_frame, from_=0, to_=1000000)

        self.sv = StringVar()
        self.sv.trace("w", lambda name, index, mode, sv=self.sv: self.bombs_callback(sv))

        bombs_entry_ratio_label = Label(bombs_frame, text="%")
        bombs_entry_ratio = Spinbox(bombs_frame, from_=0, to_=100, format="%.1f", increment=0.1, textvariable=self.sv)

        # ----- /Bombs submenu -----

        # ----- Tilesize submenu -----
        tilesize_separator = ttk.Separator(root, orient=HORIZONTAL)

        tilesize_checkbutton_var = StringVar()
        tilesize_checkbutton_var.set("Tile Set:")
        tilesize_label = Label(root, textvariable = tilesize_checkbutton_var, font=separator_font)

        tilesize_separator_end = ttk.Separator(root, orient=HORIZONTAL)

        tilesize_frame = Frame(root)

        tilesize_in_pixels = IntVar()
        tilesize_radiobutton1 = Radiobutton(tilesize_frame, text="64 x 64 (Child/Retiree)", variable=tilesize_in_pixels, value=64)
        tilesize_radiobutton2 = Radiobutton(tilesize_frame, text="32 x 32 (Human)", variable=tilesize_in_pixels, value=32)
        tilesize_radiobutton3 = Radiobutton(tilesize_frame, text="16 x 16 (Inhuman)", variable=tilesize_in_pixels, value=16)
        tilesize_radiobutton4 = Radiobutton(tilesize_frame, text="8 x 8 (Ant)", variable=tilesize_in_pixels, value=8)
        tilesize_radiobutton5 = Radiobutton(tilesize_frame, text="4 x 4 (Super-Ant!)", variable=tilesize_in_pixels, value=4)

        L_image = Image.open("../resources/tiles/standard/L/YYY.png")
        L_photo = ImageTk.PhotoImage(L_image)
        L_label = Label(tilesize_frame, image=L_photo)
        L_label.image = L_photo  # keep a reference!

        M_image = Image.open("../resources/tiles/standard/M/YYY.png")
        M_photo = ImageTk.PhotoImage(M_image)
        M_label = Label(tilesize_frame, image=M_photo)
        M_label.image = M_photo  # keep a reference!

        S_image = Image.open("../resources/tiles/standard/S/YYY.png")
        S_photo = ImageTk.PhotoImage(S_image)
        S_label = Label(tilesize_frame, image=S_photo)
        S_label.image = S_photo  # keep a reference!

        XS_image = Image.open("../resources/tiles/standard/XS/YYY.png")
        XS_photo = ImageTk.PhotoImage(XS_image)
        XS_label = Label(tilesize_frame, image=XS_photo)
        XS_label.image = XS_photo  # keep a reference!
        
        XXS_image = Image.open("../resources/tiles/standard/XXS/YYY.png")
        XXS_photo = ImageTk.PhotoImage(XXS_image)
        XXS_label = Label(tilesize_frame, image=XXS_photo)
        XXS_label.image = XXS_photo  # keep a reference!

        tilesize_checkbutton_var = IntVar()
        tilesize_checkbutton = Checkbutton(
            tilesize_frame, text="Increased border sharpness (16 x 16 px and larger only)",
            variable=tilesize_checkbutton_var)

        # ----- /Tilesize submenu -----

        # ----- Fitsscreen submenu -----
        fitsscreen_separator = ttk.Separator(root, orient=HORIZONTAL)

        fitsscreen_var = StringVar()
        fitsscreen_var.set("Fits Screen?")
        fitsscreen_label = Label(root, textvariable = fitsscreen_var, font=separator_font)

        fitsscreen_separator_end = ttk.Separator(root, orient=HORIZONTAL)

        fit_var = StringVar()
        fit_var.set("YES, the board fits the screen! (to be implemented later...)")
        fit_label = Label(root, textvariable = fit_var, font=fit_font)

        nofit_var = StringVar()
        nofit_var.set("NO, the board does NOT fit the screen! (to be implemented later...)")
        nofit_label = Label(root, textvariable = nofit_var, font=nofit_font)
        # ----- /Fitsscreen submenu -----

        # ----- Newgame submenu -----
        newgame_separator = ttk.Separator(root, orient=HORIZONTAL)

        newgame_button = Button(root, text ="New Game", command= lambda: self.newgame_callback(int(self.dimensions_entry_width.get()), int(self.dimensions_entry_height.get()), int(self.bombs_entry_number.get()), resolutions_checkbutton_var.get(), self.resolutions_entry_width.get(), self.resolutions_entry_height.get(), tilesize_checkbutton_var.get(), tilesize_in_pixels.get()), font=title_font)
        newgame_separator_end = ttk.Separator(root, orient=HORIZONTAL)
        # ----- /Newgame submenu -----

        # ----- About submenu -----
        about_var = StringVar()
        about_var.set("\u00A9 2020 Andreas Kuoppa")
        about_label = Label(root, textvariable = about_var)
        # ----- /About submenu -----

        # ----- Defaults -----
        tilesize_radiobutton2.select()

        self.resolutions_entry_width.delete(0, "end")
        self.resolutions_entry_width.insert(0, 1920)

        self.resolutions_entry_height.delete(0, "end")
        self.resolutions_entry_height.insert(0, 1080)

        bombs_entry_ratio.delete(0, "end")
        bombs_entry_ratio.insert(0, 20.0)
        # ----- /Defaults -----

        # ----- Packing (and gridding...) -----
        title_label.pack()
        
        resolutions_separator.pack(fill="x")
        resolutions_label.pack()
        resolutions_separator_end.pack(fill="x")
        
        resolutions_frame.pack()

        resolutions_entry_width_label.grid(row=0, column=0)
        self.resolutions_entry_width.grid(row=0, column=1, sticky="e", padx=30)
        resolutions_entry_width_cells_label.grid(row=0, column=2, sticky="w")

        resolutions_entry_height_label.grid(row=1, column=0)
        self.resolutions_entry_height.grid(row=1, column=1, sticky="e", padx=30)
        resolutions_entry_height_cells_label.grid(row=1, column=2, sticky="w")

        resolutions_checkbutton.grid(row=2, column=1)

        dimensions_separator.pack(fill="x")
        dimensions_label.pack()
        dimensions_separator_end.pack(fill="x")

        dimensions_frame.pack()

        dimensions_entry_width_label.grid(row=0, column=0)
        self.dimensions_entry_width.grid(row=0, column=1, sticky="e", padx=30)
        dimensions_entry_width_cells_label.grid(row=0, column=2, sticky="w")

        dimensions_entry_height_label.grid(row=1, column=0)
        self.dimensions_entry_height.grid(row=1, column=1, sticky="e", padx=30)
        dimensions_entry_height_cells_label.grid(row=1, column=2, sticky="w")


        bombs_separator.pack(fill="x")
        bombs_label.pack()
        bombs_separator_end.pack(fill="x")

        bombs_frame.pack()

        bombs_radiobutton1.grid(row=0, column=0, sticky="w")
        bombs_radiobutton2.grid(row=1, column=0, sticky="w")

        self.bombs_entry_number.grid(row=0, column=1, sticky="e", padx=30)
        bombs_entry_number_label.grid(row=0, column=2, sticky="w")

        bombs_entry_ratio.grid(row=1, column=1, sticky="e", padx=30)
        bombs_entry_ratio_label.grid(row=1, column=2, sticky="w")

        tilesize_separator.pack(fill="x")
        tilesize_label.pack()
        tilesize_separator_end.pack(fill="x")

        tilesize_frame.pack()

        tilesize_radiobutton1.grid(row=0, column=0, sticky="w")
        tilesize_radiobutton2.grid(row=1, column=0, sticky="w")
        tilesize_radiobutton3.grid(row=2, column=0, sticky="w")
        tilesize_radiobutton4.grid(row=3, column=0, sticky="w")
        tilesize_radiobutton5.grid(row=4, column=0, sticky="w")
        tilesize_checkbutton.grid(row=5, column=1, sticky="w")


        L_label.grid(row=0, column=1, sticky="w")
        M_label.grid(row=1, column=1, sticky="w")
        S_label.grid(row=2, column=1, sticky="w")
        XS_label.grid(row=3, column=1, sticky="w")
        XXS_label.grid(row=4, column=1, sticky="w")

        """
        fitsscreen_separator.pack(fill="x")
        fitsscreen_label.pack()
        fitsscreen_separator_end.pack(fill="x")

        fit_label.pack()
        nofit_label.pack()
        """

        newgame_separator.pack(fill="x")
        newgame_button.pack(pady=8)
        # newgame_separator_end.pack(fill="x")

        about_label.pack()
        # ----- /Packing (and gridding...) -----

        root.mainloop()


if __name__ == "__main__":
    launcher = Launcher()

    launcher.main()
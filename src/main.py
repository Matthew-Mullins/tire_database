import tkinter as tk
from tkinter import ttk
import sqlite3

from tire import Size, Tire

'''
Brand
Model
Size(
    Tire Type
    Tire Width
    Aspect Ratio
    Construction Type (R, D, F(Runflats))
    Wheel Diameter
    Load Index
    Speed Rating
)
M+S
SNOWFLAKE
ALL-SEASON
Load Range / Ply Rating
Tread Depth
Quantity
Price
Notes
Location
Status(
    Pictures
    Posted
    NFS
)
'''

class TireFrame(tk.Frame):
    def __init__(self, master, tire):
        tk.Frame.__init__(self, master)
        self.configure(bd=2, relief=tk.GROOVE, width=1200)
        self.tire = tire
        self.create_frame()

    def create_frame(self):
        label_brand = tk.Label(self, text='Goodyear Wrangler SR-A')
        label_brand.grid(row=0, column=0, columnspan=3, sticky=tk.W)

        frame_icons = tk.Frame(self)
        frame_icons.grid(row=0, column=4, sticky=tk.NSEW)

        label_size = tk.Label(self, text='LT265/60R20')
        label_size.grid(row=1, column=0, columnspan=2, sticky=tk.W)

        label_load_index = tk.Label(self, text='121/118S')
        label_load_index.grid(row=1, column=2, sticky=tk.E)

        label_load_range = tk.Label(self, text='E')
        label_load_range.grid(row=1, column=3, sticky=tk.NSEW)

        label_quantity = tk.Label(self, text='2')
        label_quantity.grid(row=2, column=0, sticky=tk.W)

        label_tread_depth = tk.Label(self, text='10.10')
        label_tread_depth.grid(row=2, column=1, sticky=tk.NSEW)

        label_price = tk.Label(self, text='$300.00')
        label_price.grid(row=2, column=2, sticky=tk.E)

        label_location = tk.Label(self, text='A1')
        label_location.grid(row=2, column=3, sticky=tk.NSEW)

        label_status = tk.Label(self, text='TAGGED')
        label_status.grid(row=2, column=4, sticky=tk.NSEW)

        label_notes = tk.Label(self, text='Notes: Rock rash. Piece of shit tire.')
        label_notes.grid(row=3, column=0, columnspan=5, sticky=tk.W)

        for x in range(5):
            tk.Grid.columnconfigure(self, x, weight=1)

        # for y in range(4):
        #     tk.Grid.rowconfigure(self, y, weight=1)

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.initialize()
        self.pack(expand=True, fill=tk.BOTH)

    def initialize(self):
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
        frame_scrollable = ttk.Frame(canvas)
        frame_scrollable.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=frame_scrollable, anchor=tk.NW)
        canvas.update_idletasks()
        canvas.configure(yscrollcommand=scrollbar.set)

        for _ in range(10):
            tire_frame = TireFrame(frame_scrollable, None)
            tire_frame.configure(width=800)
            tire_frame.pack(side=tk.TOP)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def run(self):
        self.master.mainloop()

def main():
    root = tk.Tk()
    app = Application(root)
    app.run()

if __name__ == "__main__":
    main()
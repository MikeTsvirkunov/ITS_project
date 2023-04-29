import tkinter as tk
import Menu
from tkinter import messagebox as mb


class MapBTN:
    def __init__(self, window, rl, cl):
        self.window = window
        self.rl = rl
        self.cl = cl
        self.map_btn = tk.Entry(self.window, width=3)
        self.born()

    def born(self):
        self.map_btn.grid(row=self.rl, column=self.cl, padx=3, pady=2)


class WindowOfInputMap:
    def __init__(self, window):
        self.window = window
        self.map_mass = list()

        self.input_frame = tk.Frame(self.window, bg="black")
        self.map_frame = tk.Frame(self.window, bg="black")

        self.n = tk.Label(self.input_frame, bg='black', fg='green', text='n:=')
        self.enter_n = tk.Entry(self.input_frame)

        self.button_print = tk.Button(self.input_frame, text="Create field", command=self.create_field)
        self.button_find_out = tk.Button(self.input_frame, text="Find out", command=self.rasch)
        self.button_back = tk.Button(self.input_frame, text="Back to menu", command=self.back_to_menu)

        self.solution = tk.Label(self.input_frame, bg='black', fg='green', text='')

    def create_field(self):
        self.map_frame.destroy()
        self.map_frame = tk.Frame(self.window, bg="black")
        self.map_frame.grid(column=3, row=0, rowspan=int(self.enter_n.get()))
        self.button_find_out.grid(row=3, column=2)
        self.solution.grid(row=3, column=3)
        self.map_mass = []
        for i in range(int(self.enter_n.get())):
            self.map_mass.append([])
            for i1 in range(int(self.enter_n.get())):
                self.map_mass[i].append(MapBTN(window=self.map_frame, rl=i, cl=i1))
        self.input_frame["bg"] = "black"

    def born_window(self):
        self.input_frame.grid(column=0, row=0)
        self.n.grid(row=0, column=0)
        self.enter_n.grid(row=0, column=1)

        self.button_back.grid(row=3, column=0)
        self.button_print.grid(row=3, column=1)

    def back_to_menu(self):
        self.input_frame.grid_forget()
        self.map_frame.grid_forget()
        x = Menu.MainMenu(self.window)
        x.window_born()

    def rasch(self):

        x = int(self.enter_n.get())
        i = 0
        way = 0
        mass_i = list()
        mass_i2 = list()
        while x > 0:
            min_elt = -1
            min_ind = -1
            for i2 in range(len(self.map_mass[i])):
                print('way = ', way)
                print('x=', x)
                print('i=', i, 'i2=', i2)
                print('mass_i=', mass_i)
                v = self.map_mass[i][i2].map_btn.get()
                print('v=', v)
                print('min_elt=', min_elt)
                print('-------------------------------------------------')
                if i2 not in mass_i:
                    if v != ' ' and v != '' and v != '-':
                        if int(v) <= min_elt or min_elt <= 0:
                            min_ind = i2
                            min_elt = int(v)
            if min_elt >= 0 and min_ind >= 0:
                mass_i.append(i)
                way += min_elt
                i = min_ind
                mass_i2.append(min_elt)
            x -= 1
        w = "["
        for i in mass_i: w+=str(i)+", "
        w += "]"
        mb.showinfo(title="Anser", message=('anser = ' + str(way) + "\nmass_znach= " + w))

        print('anser:', way)
        print('mass_znach=', mass_i2)

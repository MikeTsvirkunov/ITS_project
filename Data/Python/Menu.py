import tkinter as tk
import Menu_of_map_input


class MainMenu:
    def __init__(self, window):
        self.window = window
        self.frame_menu = tk.Frame(self.window, bg="black")
        self.main_label = tk.Label(self.frame_menu, bg='black', fg='green', text='Поиск пути без СМС и регистрации')
        self.btn_btn_input = tk.Button(self.frame_menu, bg='black', fg='red', text='By yourself',
                                       command=self.btn_input)
        self.btn_exit = tk.Button(self.frame_menu, bg='black', fg='red', text='Exit', command=self.close_program)

    def close_program(self):
        self.window.destroy()

    def btn_input(self):
        self.frame_menu.grid_forget()
        x = Menu_of_map_input.WindowOfInputMap(self.window)
        x.born_window()

    def window_born(self):
        self.frame_menu.grid(column=0, row=0)
        self.btn_btn_input.grid(column=0, row=1, pady=30, padx=30, ipady=10, ipadx=10)
        self.btn_exit.grid(column=0, row=3, pady=30, padx=30, ipady=10, ipadx=10)
        self.main_label.grid(column=0, row=0, pady=30, padx=30, ipady=10, ipadx=10)

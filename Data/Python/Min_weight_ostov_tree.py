import tkinter as tk
import Menu

r = tk.Tk()
r.title("Поиск пути без СМС и регистрации")
r["bg"] = "black"

x = Menu.MainMenu(r)
x.window_born()

r.mainloop()
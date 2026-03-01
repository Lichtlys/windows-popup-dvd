import tkinter as tk
import random

root = tk.Tk()

# SMALLER SIZE
w = 200
h = 100

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

x = 100
y = 100

dx = 4
dy = 4

root.overrideredirect(True)
root.geometry(f"{w}x{h}+{x}+{y}")

label = tk.Label(root, text="DVD", font=("Arial", 30, "bold"), fg="white")
label.pack(fill="both", expand=True)

def change_color():
    color = "#%02x%02x%02x" % tuple(random.randint(0,255) for _ in range(3))
    label.config(bg=color)
    root.after(2000, change_color)  # 2 seconds now

def move_window():
    global x, y, dx, dy

    x += dx
    y += dy

    if x + w >= screen_w or x <= 0:
        dx = -dx
    if y + h >= screen_h or y <= 0:
        dy = -dy

    root.geometry(f"{w}x{h}+{x}+{y}")
    root.after(20, move_window)

change_color()
move_window()

root.mainloop()
from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("Color Change Button")

# starting color
current_color = "green"

def change_color():
    global current_color

    if current_color == "green":
        current_color = "blue"
    elif current_color == "blue":
        current_color = "red"
    elif current_color == "red":
        current_color = "yellow"
    else:
        current_color = "green"

    btn.config(bg=current_color)

btn = Button(root, text="Click Me", width=20, height=2, bg=current_color, command=change_color)
btn.pack(pady=100)

root.mainloop()
import random
import tkinter as tk


def show_thanks():
	for widget in root.winfo_children():
		widget.destroy()

	tk.Label(
		root,
		text="THANKS FOR UNDERSTANDING ME, YOU'RE THE BEST ADVISER OF MINE",
		font=("Arial", 16, "bold"),
		wraplength=420,
		justify="center",
	).pack(expand=True, padx=20, pady=20)


def move_no_button(_event=None):
	max_x = max(0, area.winfo_width() - no_button.winfo_width())
	max_y = max(0, area.winfo_height() - no_button.winfo_height())
	no_button.place(x=random.randint(0, max_x), y=random.randint(0, max_y))


root = tk.Tk()
root.title("I AM SORRY")
root.geometry("460x260")
root.resizable(False, False)

tk.Label(root, text="I AM SORRY", font=("Arial", 22, "bold")).pack(pady=(25, 10))

area = tk.Frame(root, width=420, height=150)
area.pack(padx=20, pady=10)
area.pack_propagate(False)

tk.Button(area, text="YES", width=10, command=show_thanks).place(x=90, y=55)
no_button = tk.Button(area, text="NO", width=10, command=move_no_button)
no_button.place(x=235, y=55)
no_button.bind("<Enter>", move_no_button)

root.mainloop()

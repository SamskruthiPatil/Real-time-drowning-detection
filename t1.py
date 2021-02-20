import tkinter as tk 
from tkinter import messagebox 
import threading


def warn():
	root = tk.Tk()
	root.title("Warning")
	root.geometry("300x200")
	#p=playsound('alarm_2.mp3')
	#p.pack()
	
	label = tk.Label(root, text="Person in danger zone")
	label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
	button = tk.Button(root, text="OK", command=lambda: root.destroy())
	button.pack(side="bottom", fill="none", expand=True)
	#playsound('alarm_2.mp3')
	#root.after(5000, root.destroy())
	

	root.mainloop()



if __name__ == "__main__":
  warn()
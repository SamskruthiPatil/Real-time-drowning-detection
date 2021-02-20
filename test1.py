import tkinter as tk 
from tkinter import messagebox 
import test as s

def warn():
	root = tk.Tk()
	root.title("Warning")
	root.geometry("300x200")
	#p=playsound('alarm_2.mp3')
	#p.pack()
	
	label = tk.Label(root, text="Maximum occupancy reached")
	label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
	button = tk.Button(root, text="OK", command=lambda: root.destroy() ) #command = s.pause1()
	button.pack(side="bottom", fill="none", expand=True)

	#button1 = tk.Button(root, text="close", command=lambda: root.destroy() )
	#button1.pack(side="right", fill="none", expand=True)
	#playsound('alarm_2.mp3')
	#root.after(5000, root.destroy())
	

	root.mainloop()



if __name__ == "__main__":
  warn()
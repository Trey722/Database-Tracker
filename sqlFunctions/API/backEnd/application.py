import tkinter as tk 

window = tk.Tk()


standeredLabelWidth = 0 
standeredLabelHeight = 0 

greeting = tk.Label(text="Enter the password for your application", foreground="white", background="black", width=standeredLabelWidth, height = standeredLabelHeight)

greeting.pack()

entry = tk.Entry(fg="white", bg="black", width=50)

entry.pack()



window.mainloop()
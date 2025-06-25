import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time

#making the root
root = tk.Tk()
root.title("Hello world")
root.geometry("300x300")

#variables
number_var=tk.StringVar()

#start progresssbar function
def progress_popup():
  #creating popup
  global analysing
  analysing = tk.Toplevel(root)
  analysing.title("Analysing")
  analysing.geometry("200x200")
  
  #text label
  anylysing_memories = tk.Label(analysing, text="Analysing Memories...")
  anylysing_memories.pack()
  
  #progress bar
  progress_bar = ttk.Progressbar(analysing, orient="horizontal", length=100, mode="determinate")
  progress_bar.pack()
  
  #updating
  def step():
    for x in range(5):
      progress_bar['value'] += 20
      root.update_idletasks()
      time.sleep(1)
  step()

  #deleting
  if progress_bar['value'] == 100.0:
    analysing.destroy()
    open_popup()
  
#popup screen function
def open_popup():
  messagebox.showinfo("Mind Read", "Your mind has been read!")
  submit()
  
#submit function
def submit():
  number=number_var.get()
  messagebox.showinfo("Results", "You are thinking of the number " + number)
  number_var.set("")

#think of number
think_of_number = tk.Label(text="Think of a number!").pack()

#input number thought of
number_entry = tk.Entry(textvariable=number_var).pack()

#submit button
submit_button = tk.Button(text="Read my mind!", command = progress_popup).pack()

tk.mainloop()
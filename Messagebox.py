from tkinter import * 

from tkinter import messagebox 

root = Tk() 

root.geometry("300x200") 
  
w = Label(root, text ='GeeksForGeeks', font = "10")  
w.pack()
  
messagebox.showwarning("Hacker Detected!", "Your phone has been hacked") 

root.mainloop()

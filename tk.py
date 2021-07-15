from tkinter import *
from PIL import Image, ImageTk

root = Tk()

image = Image.open("AI.png")

resize_image = image.resize((600, 450))
  
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img)
label1.image = img
label1.pack()
root.mainloop()

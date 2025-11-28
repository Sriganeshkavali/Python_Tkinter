import tkinter as tk

window=tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=500)

label=tk.Label(text="Hello World",font=("Arial",24,"bold"))
label.pack(side="left")

label['text']="New Text"
label.config(text="New Text")   

#button 
button=tk.Button(text="Click Me")
button.pack()

def button_clicked():
    label.config(text="Button Clicked")
    print("button clicked")

button2=tk.Button(text="Click Me",command=button_clicked)
button2.pack()
#input
input=tk.Entry(width=10)
input.pack()

def in_text():
    text_new=input.get()
    label.config(text=text_new)

button3=tk.Button(text="Click Me",command=in_text)
button3.pack()

window.mainloop()



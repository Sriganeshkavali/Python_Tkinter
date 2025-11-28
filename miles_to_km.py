import tkinter as tk

def calculate_km():
    km=float(entry.get())*1.60934
    text = tk.Text(height=2, width=10)
    text.insert(tk.END, km)
    text.grid(column=1,row=2)

window = tk.Tk()
window.title("Miles to KM")
window.minsize(width=300, height=200)

my_label=tk.Label(text="Miles to KM Converter")
my_label.grid(column=0,row=0)

label_mile=tk.Label(text="Miles")
label_mile.grid(column=0,row=1)
entry = tk.Entry(width=10)
entry.grid(column=1,row=1)
entry.insert(tk.END,"0")


button = tk.Button(text="Calculate", command=calculate_km)
button.grid(column=1,row=3)

window.mainloop()
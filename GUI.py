import tkinter as tk
from tkinter import messagebox
universal_font = ('Arial', 20, 'Bold')

root = tk.Tk()
def calculate_bmi():
    w = weight.get()
    h = height.get()
    ans = w/h**2
    ans_label.config(text=f"BMI:{ans}")
    messagebox.showinfo("Results", f"Your BMI is:{ans}")


weight = tk.DoubleVar()
height =tk.DoubleVar()
# ans = calculate_bmi()


weight_label = tk.Label(root, text="Weight (in kg)")
weight_label.grid(row=0, column=0)

weight_entry = tk.Entry(root, textvariable=weight, width=40, bd=6)
weight_entry.grid(row=0, column=1)

height_label = tk.Label(root, text="Height (in m)")
height_label.grid(row=1, column=0)

height_entry = tk.Entry(root, textvariable=height, width=40, bd=6)
height_entry.grid(row=1, column=1)

button = tk.Button(root, command=calculate_bmi, text="Calculate BMI", pady=5)
button.grid(row=3, columnspan=3)

ans_label = tk.Label(root, font=('Arial', 20))
ans_label.grid(row=4, columnspan=4)


root.title("BMI calc")
root.resizable(False, False)
root.mainloop() # to spin the app
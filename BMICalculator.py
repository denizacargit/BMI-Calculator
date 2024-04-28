from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=200, height=150)

weight_label = Label(text="Enter your weight(kg)", font=("Helvetica", 10, "normal"))
weight_label.pack()
weight_entry = Entry(width=10)
weight_entry.pack()

height_label = Label(text="Enter your height(m)", font=("Helvetica", 10, "normal"))
height_label.pack()
height_entry = Entry(width=10)
height_entry.pack()

result_label = Label()
result_label.config(font=("Helvetica", 10, "normal"))


def button_clicked():
    if height_entry == int or height_entry == float and weight_entry == int or height_entry == float:
        bmi_value = float(int(weight_entry.get()) / float(height_entry.get()) ** 2)
        if bmi_value <= 18.5:
            result_label.config(text=f"Your BMI is {bmi_value}.You are underweight")

        elif bmi_value > 18.5 and bmi_value <= 24.9:
            result_label.config(text=f"Your BMI is {bmi_value}.Your weight is healthy")

        elif bmi_value > 24.9 and bmi_value <= 29.9:
            result_label.config(text=f"Your BMI is {bmi_value}.You are overweight")

        elif bmi_value > 29.9:
            result_label.config(text=f"Your BMI is {bmi_value}.You are obese")

        else:
            print("Please enter valid values")

    else:
        result_label.config(text="Please enter valid numbers")


my_button = Button(text="Calculate", command=button_clicked)
my_button.pack()

result_label.pack()

window.mainloop()

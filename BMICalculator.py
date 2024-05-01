import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=30, pady=30)

weight_label = tkinter.Label(text="Enter your weight(kg)", font=("Helvetica", 10, "normal"))
weight_label.pack()

weight_entry = tkinter.Entry(width=10)
weight_entry.pack()

height_label = tkinter.Label(text="Enter your height(cm)", font=("Helvetica", 10, "normal"))
height_label.pack()

height_entry = tkinter.Entry(width=10)
height_entry.pack()




def calculate_bmi():
    weight = weight_entry.get()
    height = height_entry.get()
    if height == "" or weight == "":
        result_label.config(text="Enter both height and weight!")

    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")
def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight!"
    elif 25 < bmi <= 30:
        result_string += "overweight!"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string


calculate_button = tkinter.Button(text="Calculate", command=calculate_bmi)
calculate_button.pack()
result_label = tkinter.Label(font=("Helvetica", 8, "normal"))
result_label.pack()




window.mainloop()




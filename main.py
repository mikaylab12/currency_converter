# Mikayla Beelders
# currency converter task
from tkinter import *
from tkinter import messagebox
import requests

root = Tk()
root.geometry("600x600")
root.title("Currency Converter")
root.config(bg="#6dc9a9")

# heading
heading = Label(root, text="Convert To USD", bg="#6dc9a9", fg="white", font=("Helvertica", 25, "bold"))
heading.place(relx=0.26, rely=0)

# amount that user enters: labels and entry
amount_label = Label(root, text="Please enter an amount:", bg="#6dc9a9", fg="white", font=("Helvertica", 15))
amount_label.place(relx=0.3, rely=0.1)
amount_entry = Entry(root)
amount_entry.place(relx=0.36, rely=0.17)

# converted answer : answer and currency label
usd_answer = Label(root,  font=("Helvertica", 25, 'bold'), bg="#6dc9a9", fg="white")
usd_answer.place(relx=0.19, rely=0.85)
usd_label = Label(root, text="USD", bg="#6dc9a9", fg="white", font=("Helvertica", 25, 'bold'))
usd_label.place(relx=0.6, rely=0.85)

# making the request
response = requests.get('https://prime.exchangerate-api.com/v5/d15f5d23ca3cd1c7094c5e89/latest/USD')
data = response.json()
standard_rate = data['conversion_rates']
print(standard_rate)

# covert label and listbox
convert_label = Label(root, text="Please select a currency: ",  bg="#6dc9a9", fg="white", font=("Helvertica", 15))
convert_label.place(relx=0.3, rely=0.25)
convert_list = Listbox(root, width=20)
for i in standard_rate.keys():
    convert_list.insert(END, str(i))
convert_list.place(relx=0.36, rely=0.3)

# convert function
def convert():
    try:
        amount = float(amount_entry.get())
        print(data['conversion_rates'][convert_list.get(ACTIVE)])
        converted_amount = amount / data['conversion_rates'][convert_list.get(ACTIVE)]
        usd_answer['text'] = round(converted_amount, 2)  # round conversion off to 2 decimal places
    except ValueError:
        messagebox.showerror("Error", "Invalid input.\nPlease enter integers.")
        amount_entry.delete(0, END)
        usd_answer.config(text="")
        convert_list.select_clear(0, END)


# convert button
convert_btn = Button(root, text="Convert", borderwidth=5, padx=15, pady=10, bg="#6dc9a9", fg="White", command=convert, font=("Helvertica", 15))
convert_btn.place(relx=0.1, rely=0.7)


# clear function
def clear():
    amount_entry.delete(0, END)
    usd_answer.config(text="")
    convert_list.select_clear(0, END)


# clear button
clear_btn = Button(root, text="Clear", borderwidth=5, padx=27, pady=10, bg="#6dc9a9", fg="White", command=clear, font=("Helvertica", 15))
clear_btn.place(relx=0.4, rely=0.7)

# exit program
def exit():
    root.destroy()


# exit button
exit_btn = Button(root, text="Exit", borderwidth=5, padx=30, pady=10, bg="#6dc9a9", fg="White", command=exit, font=("Helvertica", 15))
exit_btn.place(relx=0.7, rely=0.7)

root.mainloop()
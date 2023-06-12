import tkinter as tk
from tkinter import messagebox, simpledialog
from subprocess import call

def redirect_current_account():
    call(["python", "test_2.py"])

def redict_savings_account():
    call(["python", "test.py"])

def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":

        title = title_entry.get()
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:
            age = age_spinbox.get()

            current_account = current_account_var.get()
            saving_account = saving_account_var.get()
            account_number = account_number_entry.get()
            pin = account_pin_entry.get()

            print("Title", title, "First Name:", firstname, "Last Name:", lastname)
            print("age:", age, "Current Account:", current_account, "Saving Account:", saving_account)
            print("Account Number", account_number, "Pin:", pin)
        else:
            tk.messagebox.showwarning(title="Error", message="First Name & Last Name are Required")
    else:
        tk.messagebox.showwarning(title="Error", message=" You Have Not Accepted The Terms!")


window = tk.Tk()
window.geometry("550x550")
window.title("Piggy_Vest")

frame = tk.Frame(master=window)
frame.pack()

user_info_frame = tk.LabelFrame(master=frame, text="user Information", width=200)
user_info_frame.grid(row=0, column=0)

title_label = tk.Label(master=user_info_frame, text="Title")
title_label.grid(row=0, column=0)
first_name_label = tk.Label(master=user_info_frame, text="First Name")
first_name_label.grid(row=0, column=1)
last_name_label = tk.Label(master=user_info_frame, text="last Name")
last_name_label.grid(row=0, column=2)

title_entry = tk.Entry(master=user_info_frame)
first_name_entry = tk.Entry(master=user_info_frame)
last_name_entry = tk.Entry(master=user_info_frame)
title_entry.grid(row=1, column=0)
first_name_entry.grid(row=1, column=1)
last_name_entry.grid(row=1, column=2)

age_label = tk.Label(master=user_info_frame, text="Age")
age_spinbox = tk.Spinbox(master=user_info_frame, from_=18, to=30)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

account_frame = tk.LabelFrame(master=frame, text="Account Info")
account_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

account_label = tk.Label(master=account_frame, text="Account")
current_account_var = tk.StringVar(value="Not Registered")
current_account_check = tk.Checkbutton(master=account_frame, text="Current Account", variable=current_account_var,
                                       onvalue="Registered", offvalue="Not Registered", command=redirect_current_account)
saving_account_var = tk.StringVar(value="Not Registered")
saving_account_check = tk.Checkbutton(master=account_frame, text="Savings Account", variable=saving_account_var,
                                      onvalue="Registered", offvalue="Not Registered", command=redict_savings_account)
account_number_label = tk.Label(master=account_frame, text="Account Number")
account_pin_label = tk.Label(master=account_frame, text="Pin")
account_label.grid(row=0, column=0)
current_account_check.grid(row=1, column=0)
saving_account_check.grid(row=2, column=0)
account_number_label.grid(row=0, column=1)
account_pin_label.grid(row=0, column=2)

account_number_entry = tk.Entry(master=account_frame)
account_number_entry.grid(row=1, column=2)

account_pin_entry = tk.Entry(master=account_frame)
account_pin_entry.grid(row=1, column=1)

for widget in account_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tk.LabelFrame(master=frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(master=terms_frame, text="I accept the terms and condition.", variable=accept_var,
                             onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

button = tk.Button(master=frame, text="Submit Data!", command=enter_data)
button.grid(row=3, column=0, sticky='news', padx=20, pady=10)


window.mainloop()

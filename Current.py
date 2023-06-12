import tkinter as tk
from tkinter import messagebox, simpledialog

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            messagebox.showinfo("Deposit", f"Deposited {amount} successfully!")
        else:
            messagebox.showerror("Error", "Invalid amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            messagebox.showinfo("Withdraw", f"Withdrawn {amount} successfully!")
        else:
            messagebox.showerror("Error", "Invalid amount or insufficient balance!")

class AccountApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Account App")

        self.current_account = Account(0.0)

        self.create_widgets()

    def create_widgets(self):
        # Create labels
        self.current_label = tk.Label(self, text="Current Account")
        self.current_label.pack()

        self.current_balance_label = tk.Label(self, text=f"Balance: {self.current_account.balance}")
        self.current_balance_label.pack()
        self.current_balance_entry = tk.Entry(self)
        self.current_balance_entry.pack()

        self.current_buttons_frame = tk.Frame(self)
        self.current_buttons_frame.pack()

        self.current_deposit_button = tk.Button(self.current_buttons_frame, text="Deposit", command=self.current_deposit)
        self.current_deposit_button.pack(side=tk.LEFT)

        self.current_withdraw_button = tk.Button(self.current_buttons_frame, text="Withdraw", command=self.current_withdraw)
        self.current_withdraw_button.pack(side=tk.LEFT)


    def current_deposit(self):
        amount = self.get_amount()
        if amount:
            self.current_account.deposit(amount)
            self.current_balance_label.config(text=f"Balance: {self.current_account.balance}")

    def current_withdraw(self):
        amount = self.get_amount()
        if amount:
            self.current_account.withdraw(amount)
            self.current_balance_label.config(text=f"Balance: {self.current_account.balance}")

    def get_amount(self):
        amount = simpledialog.askfloat("Amount", "Enter the amount:")
        if amount is not None:
            return amount

if __name__ == "__main__":
    app = AccountApp()
    app.mainloop()
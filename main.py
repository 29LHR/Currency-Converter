import tkinter as tk
from tkinter import ttk, messagebox

# Exchange rates relative to USD (approximate rates as of 2024-01-01)
RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.50,
    "CAD": 1.36,
    "AUD": 1.53,
    "CHF": 0.90,
    "CNY": 7.24,
    "INR": 83.12,
    "MXN": 17.15,
    "BRL": 4.97,
    "KRW": 1325.0,
    "SGD": 1.34,
    "HKD": 7.82,
    "NOK": 10.55,
    "SEK": 10.42,
    "DKK": 6.89,
    "NZD": 1.63,
    "ZAR": 18.63,
    "RUB": 89.50,
}

CURRENCIES = sorted(RATES.keys())


def convert():
    amount_text = amount_entry.get().strip()
    if not amount_text:
        messagebox.showerror("Input Error", "Please enter an amount.")
        return
    try:
        amount = float(amount_text)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a valid number.")
        return
    if amount <= 0:
        messagebox.showerror("Input Error", "Amount must be a positive number.")
        return

    from_currency = from_var.get()
    to_currency = to_var.get()

    try:
        amount_in_usd = amount / RATES[from_currency]
        converted = amount_in_usd * RATES[to_currency]
    except ZeroDivisionError:
        messagebox.showerror("Conversion Error", "Invalid exchange rate.")
        return

    result_var.set(f"{amount:,.2f} {from_currency} = {converted:,.2f} {to_currency}")


root = tk.Tk()
root.title("Currency Converter")
root.resizable(False, False)

padding = {"padx": 12, "pady": 6}

# Title
title_label = tk.Label(root, text="Currency Converter", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=(16, 8))

# Amount
tk.Label(root, text="Amount:").grid(row=1, column=0, sticky="e", **padding)
amount_entry = tk.Entry(root, width=18, font=("Helvetica", 12))
amount_entry.grid(row=1, column=1, columnspan=2, sticky="w", **padding)

# From currency
tk.Label(root, text="From:").grid(row=2, column=0, sticky="e", **padding)
from_var = tk.StringVar(value="USD")
from_menu = ttk.Combobox(root, textvariable=from_var, values=CURRENCIES, state="readonly", width=10)
from_menu.grid(row=2, column=1, sticky="w", **padding)

# To currency
tk.Label(root, text="To:").grid(row=3, column=0, sticky="e", **padding)
to_var = tk.StringVar(value="EUR")
to_menu = ttk.Combobox(root, textvariable=to_var, values=CURRENCIES, state="readonly", width=10)
to_menu.grid(row=3, column=1, sticky="w", **padding)

# Convert button
convert_btn = tk.Button(root, text="Convert", command=convert, font=("Helvetica", 11), width=10)
convert_btn.grid(row=4, column=0, columnspan=3, pady=(8, 4))

# Result
result_var = tk.StringVar(value="")
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 12, "bold"), fg="#2a7ae2")
result_label.grid(row=5, column=0, columnspan=3, pady=(4, 16))

root.mainloop()

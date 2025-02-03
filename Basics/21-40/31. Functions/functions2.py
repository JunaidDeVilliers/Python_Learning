def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of R{amount:.2f} is due: {due_date}")

display_invoice("Junaid", 42.50, "01/01")
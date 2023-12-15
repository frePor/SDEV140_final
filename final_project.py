import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Welcome screen; main window

class StudentBudgetBuddy:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Budget Buddy")

        # Navigation bar
        self.navBar = ttk.Frame(root)
        self.navBar.grid(row=0, column=0, sticky="nsew")

        # Centers each button in nav bar
        self.navBar.columnconfigure(0, weight=1)
        self.navBar.columnconfigure(1, weight=1)

        ttk.Button(self.navBar, text="Home", command=self.showHome).grid(row=0, column=0)
        ttk.Button(self.navBar, text="Expenses", command=self.showExpenses).grid(row=0, column=1)
        self.showHome()

    def showHome(self):
        self.clearScreen()
        ttk.Label(self.root, text="Welcome to Student Budget Buddy!", font=("Helvetica", 16)).grid(row=1, column=0)
        ttk.Label(self.root, text="Financial Tip: Saving for your future starts now!").grid(row=2, column=0)

    def showExpenses(self):
        ExpensesWindow(self.root, self)

    def clearScreen(self):
        for widget in self.root.winfo_children():
            if widget != self.navBar:
                widget.destroy()

# Expenses window

class ExpensesWindow:
    def __init__(self, root, parent):
        self.expensesWindow = tk.Toplevel(root)
        self.expensesWindow.title("Expenses")
        self.parent = parent

        # Create category 
        ttk.Label(self.expensesWindow, text="Category:").pack()
        self.categoryEntry = ttk.Entry(self.expensesWindow)
        self.categoryEntry.pack()

        # Input amount for the created category
        ttk.Label(self.expensesWindow, text="Amount:").pack()
        self.amountEntry = ttk.Entry(self.expensesWindow)
        self.amountEntry.pack()

        ttk.Button(self.expensesWindow, text="Add Expense", command=self.addExpense).pack()

        # Displays existing categories and amounts
        ttk.Label(self.expensesWindow, text="Existing Categories and Amounts:").pack()
        self.expensesListbox = tk.Listbox(self.expensesWindow, width=40)
        self.expensesListbox.pack()

        # Button to delete selected category
        ttk.Button(self.expensesWindow, text="Delete Category", command=self.deleteCategory).pack()

        # Button to clear all expenses
        ttk.Button(self.expensesWindow, text="Clear All Expenses", command=self.clearExpenses).pack()

        # Label to display total amount
        ttk.Label(self.expensesWindow, text="Total Amount:").pack()
        self.totalAmountLabel = ttk.Label(self.expensesWindow, text="")
        self.totalAmountLabel.pack()

    def addExpense(self):
        category = self.categoryEntry.get()
        amount = self.amountEntry.get()

        # Checks to see if both fields have values
        if category and amount:
            # Message showing the category and the amount in the terminal
            print(f"Category: {category}, Amount: {float(amount)}")  # Amount only allows float value to be entered, preventing letters from being accepted

            # Add the category and amount to the listbox if not already present
            expenseEntry = f"{category}: {float(amount)}"
            if expenseEntry not in self.expensesListbox.get(0, tk.END):
                self.expensesListbox.insert(tk.END, expenseEntry)

            self.categoryEntry.delete(0, tk.END)
            self.amountEntry.delete(0, tk.END)

            # Update the total amount label
            self.calculateTotalAmount()

        else:  # Checks if the user put in a value or not and warns them
            messagebox.showwarning("Missing Information", "Please fill in both Category and Amount fields.")

    def deleteCategory(self):
        selectedCategoryIndex = self.expensesListbox.curselection()

        if selectedCategoryIndex:
            # Removes the selected category from the listbox
            self.expensesListbox.delete(selectedCategoryIndex)

            # Updates the total amount label
            self.calculateTotalAmount()

    def clearExpenses(self):
        # Clear all categories and associated expenses
        self.expensesListbox.delete(0, tk.END)

        # Updates the total amount label
        self.calculateTotalAmount()

    def calculateTotalAmount(self):
        # Calculate and display the total amount
        totalAmount = sum(float(entry.split(":")[1]) for entry in self.expensesListbox.get(0, tk.END))
        self.totalAmountLabel.config(text=f"{totalAmount:.2f}")

   
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentBudgetBuddy(root)
    root.mainloop()


# Student_expense_tracker

A simple, command-line utility for students (or anyone!) to track and manage their daily and monthly expenses. This tool allows users to quickly add expenses, view a list of all records, delete entries, and calculate the total spending for any given month.

Features

Add Expense: Record new expenses with details including date, amount, category, and description.
View Expenses: Display a numbered list of all recorded expenses.
Delete Expense: Remove a specific expense from the list using its number.
Monthly Total: Calculate and display the cumulative spending for a specified month (e.g., YYYY-MM).
Simple Interface: Easy-to-use menu-driven command line interface.

Getting Started

Prerequisites
You need Python 3 installed on your system.

Installation
No special installation is required!
Save the Code: Save the provided code into a file named expense_tracker.py.
Run the Program: Open your terminal or command prompt, navigate to the directory where you saved the file, and run:

*python expense_tracker.py*

Usage
Once the program is running, you'll see a menu:

===== Student Expense Tracker =====
1. Add Expense 
2. View All Expenses
3. Delete Expense
4. Monthly Total
0. Exit

Option	Command	Description

1	Add Expense	Prompts for date (YYYY-MM-DD), amount, category, and description.
2	View All Expenses	Lists all expenses with an index number.
3	Delete Expense	Lists expenses, then asks for the index number of the item to remove.
4	Monthly Total	Asks for the month in YYYY-MM format and calculates the sum of expenses for that period.
0	Exit	Closes the program.

Limitations

Data Volatility: This program stores all expenses in memory (expenses = []). When the program is closed (0. Exit), all data is lost.
No File I/O: There is currently no functionality to save or load expenses to/from a file (like CSV or JSON).

Contributing

This is a basic starter project. If you'd like to extend it, here are some ideas:
Implement data persistence (e.g., saving data to a file upon exit and loading it on startup).
Add a reporting feature (e.g., total per category).
Add input validation (e.g., ensuring the date format is correct or that the amount is a valid number).

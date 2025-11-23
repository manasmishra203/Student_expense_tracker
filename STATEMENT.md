Project Statement: Student Expense Tracker

This project is a fundamental proof-of-concept application demonstrating core programming principles (functions, loops, data structures, and basic I/O) applied to a real-world task: personal financial tracking.

I. Rationale and Goal

Problem Addressed
The primary challenge for budget-conscious individuals, especially students, is the manual overhead and lack of instant visibility into spending habits. This application aims to provide a zero-overhead, terminal-based solution that minimizes the barrier to entry for tracking personal finances.

Core Objectives
1.Functional Simplicity: Create an application that performs its designated functions (CRUD-like operations on expense data) reliably.
2.Learnability: Serve as a clear example of procedural Python programming, emphasizing the use of lists and dictionaries.
3.Immediate Feedback: Provide users with immediate calculation results, particularly the monthly total, for quick budget assessment.

II. Technical Deep Dive

A. Data Flow and State Management
The application's state is maintained solely by the global expenses list.
1.Input: User interaction occurs via the built-in input() function within add_expense() or main().
2.Processing: Data is converted to the appropriate type (e.g., using float() for the amount) before being stored.
3.Aggregation: The monthly_total() function processes the data by iterating over the list and using a conditional check (e["date"].startswith(month)) to accumulate the amount into a running total.

B. Function Specifics
add_expense(): Utilizes a dictionary literal to create structured data, ensuring each expense record is consistent.
view_expenses(): Employs enumerate(expenses, start=1) for a user-friendly, 1-based index display, which is critical for the delete_expense interaction.
delete_expense(): Handles the necessary index conversion (num - 1) because users interact with the 1-based list index, while Python's pop() method requires a 0-based index.

III. Future Development and Scalability

While the current implementation is intentionally minimal, future iterations would prioritize transforming the tool from a session-based utility into a persistent application:
1.Persistence Layer: Integration of the json module to handle saving the expenses list to a file before exiting and loading it upon startup.
2.Error Handling: Implementation of try...except blocks, particularly in add_expense() and delete_expense(), to gracefully handle non-numeric input (e.g., if the user enters text for the amount).
3.Advanced Reporting: Adding functions to calculate and report totals per category, offering deeper insights into spending patterns.

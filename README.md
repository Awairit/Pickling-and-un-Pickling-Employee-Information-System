# 🧑‍💻 Employee Information System (EIS) - Pickling & Unpickling

## 🌟 Project Overview

This repository contains a simple Employee Information System (EIS) built purely with Python. The primary purpose of this project is to demonstrate **data persistence** using Python's built-in `pickle` module for serialization and deserialization.

The system allows users to manage employee records (Add, View, Update, Delete) and ensures that all data is saved to a binary file (`employees.dat`) and restored when the program is run again.

---

## 🚀 Key Python Concepts Demonstrated

This project is structured using best practices to utilize the following core Python concepts:

* **Pickling (`pickle` module):** Used to convert employee data (objects/dictionaries) into a byte stream for writing to a file (`employees.dat`).
* **Unpickling (`pickle` module):** Used to reconstruct the data structure from the file back into memory.
* **Modules & Functions:** The system is modularized, with separate files/functions handling distinct operations (e.g., `employee_add.py`, `employee_delete.py`) for clean, reusable code.
* **Error Handling:** Robust `try...except` blocks are implemented to handle critical exceptions like `FileNotFoundError` (for the first run) and `EOFError` (for empty/corrupted data files) during unpickling.

---

## 📂 Project Files and Structure

The application is broken down into modular files for clarity:

| File Name | Purpose |
| :--- | :--- |
| `emp_menu.py` | Contains the main command-line interface (CLI) and menu loop logic. |
| `employee_mainProject.py` | The primary execution file, which imports and calls the menu logic. |
| `employee_add.py` | Handles the logic for collecting and saving new employee data. |
| `employee_delete.py` | Handles the logic for removing an existing employee record. |
| `employee_update.py` | Handles the logic for modifying existing employee data. |
| `employee_view.py` | Handles the logic for displaying all stored employee records. |
| `employees.dat` | **(Hidden/Ignored by Git)** The binary file used for data storage. |

---

## ⚙️ How to Run the Application

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Awairit/Employee-EIS.git](https://github.com/Awairit/Employee-EIS.git) 
    cd Employee-EIS 
    ```
2.  **Run the Main File:**
    ```bash
    python EmployeeMainProject.py
    ```
3.  The main menu will appear, allowing you to begin managing employee records.

---

## 📝 Future Enhancements

* Implement a dedicated `Employee` **Class** instead of using dictionaries for better object-oriented practice.
* Add data validation to ensure user input (like ID) is in the correct format.
* Migrate data storage to a simple text file (CSV) for comparison with the `pickle` method.


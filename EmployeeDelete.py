#EmployeeDelete.py<---File Name and Module Name
import pickle
def delete_employee():

    emp_no = int(input("Enter Employee Number to Delete:"))

    records = []
    with open("emp.txt", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break

    found=False
    for record_index in range(len(records)):
        if(records[record_index][0]==emp_no):
            index=record_index
            found=True
            break

    if(found):
        records.pop(index)
        print("\tEMPLOYEE RECORD DELETED")
        with open("emp.txt","wb") as fp:
            for record in records:
                  pickle.dump(record,fp)
    else:
        print("\tEMPLOYEE RECORD DOES NOT EXIT")

#==========================================================================================================

'''import pickle  # Line 1: Imports the pickle module, which allows us to serialize and deserialize Python objects.

def deleteemployee():  # Line 2: Defines a function named `deleteemployee` to delete an employee record.
    empno = int(input("Enter Employee Number to Delete:"))  # Line 3: Prompts the user to input an employee number and converts it to an integer.

    # Get all the records from File
    records = []  # Line 5: Initializes an empty list called `records` to store employee records.

    with open("employee.pick", "rb") as fp:  # Line 7: Opens the "employee.pick" file in read-binary mode.
        while (True):  # Line 8: Starts an infinite loop to read records.
            try:
                record = pickle.load(fp)  # Line 10: Attempts to load an employee record from the file using pickle.
                records.append(record)  # Line 11: Adds the loaded record to the `records` list.
            except EOFError:  # Line 12: Catches the end-of-file error, which indicates no more records can be read.
                break  # Line 13: Exits the loop when no more records can be loaded.

    found = False  # Line 15: Initializes a variable `found` to track if the employee record is found.
    for recindex in range(len(records)):  # Line 16: Iterates through the indices of the `records` list.
        if(records[recindex][0] == empno):  # Line 17: Checks if the employee number matches the input.
            index = recindex  # Line 18: If found, saves the index of the record.
            found = True  # Line 19: Sets `found` to True to indicate the record has been located.
            break  # Line 20: Breaks the loop once the record is found.

    if(found):  # Line 22: Checks if the record was found.
        records.pop(index)  # Line 23: Deletes the record from the list using the index.
        print("\tEMPLOYEE RECORD DELETED")  # Line 24: Prints a confirmation message.
        # After Removing the Records, save the remaining in file by replacing the existing records
        with open("employee.pick", "wb") as fp:  # Line 26: Opens the file in write-binary mode to save updated records.
            for record in records:  # Line 27: Iterates over each remaining record.
                pickle.dump(record, fp)  # Line 28: Writes each record back to the file.
    else:  # Line 30: If the record was not found.
        print("\tEMPLOYEE RECORD DOES NOT EXIT")  # Line 31: Prints a message saying the record does not exist.
'''
#EmployeeSearch.py<---File Name and Module Name
import pickle

def search_employee():

    emp_no = int(input("Enter Employee Number to view Other Details:"))

    records = []
    with open("emp.txt", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    found = False
    for record in records:
        if (record[0] == emp_no):
            found = True
            break
    print("-" * 50)
    if (found):
        print("\tEMPLOYEE EXIST IN COMPANY")
    else:
        print("\tINVALID EMPLOYEE-DOES NOT EXIST")
    print("-" * 50)

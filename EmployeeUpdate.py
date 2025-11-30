#EmployeeUpdate.py<---File Name and Module Name
import pickle
def update_employee():
    emp_no = int(input("Enter Employee Number to update salary:"))
    # get all the records from File
    records = []  # for adding records--outer list
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
        new_sal=float(input("Enter New Employee Salary:"))
        records[index][2]=new_sal
        with open("emp.txt","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\tEMPLOYEE SALARY UPDATED--VERIFY")
    else:
        print("\tEMPLOYEE NUMBER DOES NOT EXIST")


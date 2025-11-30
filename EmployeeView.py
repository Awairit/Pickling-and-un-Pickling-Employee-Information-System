#EmployeeView.py<--File Name and Module Name

import pickle

def view_employee():

    emp_no=int(input("Enter Employee Number to view Other Details:"))

    records=[]
    with open("emp.txt","rb") as fp:
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break

    found=False
    for record in records:
        if(record[0]==emp_no):
            found=True
            # rec=record
            break
    print("-"*50)

    if(found):
        print("\tEmployee Number:{}".format(record[0]))
        print("\tEmployee Name:{}".format(record[1]))
        print("\tEmployee Salary:{}".format(record[2]))
    else:
        print("\tEmployee Number Does not Exist")
    print("-" * 50)

def view_all_employee():
    try:
        print("-"*50)
        print("\tENO\t\tNAME\tSAL")
        print("-" * 50)
        with open("emp.txt","rb") as fp:
            while(True):
                try:
                    record = pickle.load(fp)
                    for val in record:
                        print("\t{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("-" * 50)
                    break
    except FileNotFoundError:
        print("File Does not Exist")


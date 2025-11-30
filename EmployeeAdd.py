#EmployeeAdd.py<---File Name and Module Name
import pickle
def add_employee():
    with open("emp.txt","ab") as fp:
        try:
            print("-"*50)
            emp_no=int(input("Enter Employee Number:"))
            emp_name=input("Enter Employee Name:")
            emp_sal=float(input("Enter Employee Salary:"))
            print("-" * 50)
            #Place the employee values in iterable Object
            lst=list() # create an empty list
            lst.append(emp_no)
            lst.append(emp_name)
            lst.append(emp_sal)
            #Save the Iterable Object data into the file
            pickle.dump(lst,fp)
            print("Employee Record Saved in File Sucessfully")
            print("-" * 50)
        except ValueError:
            print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR EMPNO AND SALARY")

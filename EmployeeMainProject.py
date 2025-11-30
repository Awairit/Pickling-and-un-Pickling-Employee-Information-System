#EmployeeMainProject.py<---Main Project
from EmpMenu import menu
from EmployeeAdd import add_employee
from EmployeeView import view_all_employee,view_employee
from EmployeeSearch import search_employee
from EmployeeDelete import delete_employee
from EmployeeUpdate import update_employee
while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice:"))
        match(ch):
            case 1:
                add_employee()
            case 2:
                delete_employee()
            case 3:
                update_employee()
            case 4:
                view_employee()
            case 5:
                view_all_employee()
            case 6:
                search_employee()
            case 7:
                print("\tTHX FOR USING THIS PROJECT")
                break
            case _:
                print("\tUR SELECTION OF OPERATION IS WRONG-TRY AGAIN")
    except ValueError:
        print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR CHOICE-TRY AGAIN")
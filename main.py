
from employee import Employee
from employee_manger import EmployeeManger
from tabulate  import tabulate
from prettytable import PrettyTable
from texttable import Texttable

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

    
   








if __name__ =="__main__":
    # fake data to test  :
    manger = EmployeeManger()
    test_list = [("ahmed",22,1500),("ebrahim",25,2500),("Adel",30,4000)]
    for name , age ,salary in test_list:
        manger.add_employee(name, age, salary)


    print(F"""{Fore.YELLOW}
           WELCOME TO ABDALLAH COMPANY APP
           please select from down list 
    
    """)
    option = f"{Fore.GREEN}1)add new employee \n2)print all employee \n3)delete by age \n4)update salary by name "

    user_input =None
    while True :
        if  user_input != True:
            print(option)
            user_input = int(input())
        if user_input == 1:
           emp_name = input(f"{Fore.MAGENTA}enter employee name: ")
           emp_age  = input("enter employee age : ")
           emp_salary = input("enter employee salary")
           manger.add_employee(emp_name, emp_age, emp_salary)
           user_input =None
           continue
        if user_input == 2:
            user_list = manger.list_employee()
            print(f"{Fore.CYAN}all company employees")
            if user_list :
               t = Texttable()
               t.add_row([f"{Fore.YELLOW} name","age","salary"])
               for te  in user_list:
                 t.add_row([te.name, te.age,te.salary])
               print(t.draw()) 
            user_input =None
            continue     
        if user_input ==3 :
            age = int(input("enter age you want to delete: "))
            for el in manger.employees_list:
                if el.age == age:
                    manger.employees_list.remove(el)
            user_input = 2
            continue    
        if user_input == 4 :
            username = input("enter employee name to update:")
            salary = input("enter new salary : ")
            for el in manger.employees_list :
                if el.name == username:
                    el.salary = salary
            user_input ==None
            continue        
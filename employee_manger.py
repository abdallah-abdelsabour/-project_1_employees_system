
from employee import Employee


class EmployeeManger:
  employees_list =[]
  def __init__(self):
    pass  
  
  def add_employee(self,name,age,salary):

      emp = Employee(name, age, salary)
      if emp not in self.employees_list:
        self.employees_list.append(emp)


      

  def list_employee(self):
      return self.employees_list

  def find_employee_byName(self,name):
      emp = None
      for el in self.employees_list:
        if el.name ==name:
           emp  = el
      return emp

     
  
  def update_salary_byname(self , name,salary):
    emp = None
    for el in self.employees_list:
      if el.name == name:
         el.salary = salary
         emp = el   
    return emp

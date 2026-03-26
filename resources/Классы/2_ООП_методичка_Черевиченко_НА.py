from abc import ABC, abstractmethod 
import os

class Employee:
    new_id = 1
    def __init__(self):
        self.id = self.new_id
        Employee.new_id += 1
    
    def say_id(self):
        print(f'My id is {self.id}')

e1 = Employee()
e2 = Employee()

e1.say_id(), e2.say_id()

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
    
    def say_user_info(self):
        print(f'My username is {self.username} and my role is {self.role}')

class Admin(Employee, User):
    
    def __init__(self):
        Employee.__init__(self)
        User.__init__(self, 'Admin Admin', 'Admin')

    def say_id(self):
        print('I am an Admin and', end = ' ')
        return super().say_id()


e3 = Admin()
e3.say_id()
e3.say_user_info()

class Manager(Admin):
    def say_id(self):
        print('I am in charge!', end = ' ')
        return super().say_id()

e4 = Manager()
e4.say_id()

os.system('cls')
meeting = [e1, e3, e4]
for person in meeting:
    person.say_id()


class Meeting:
    def __init__(self):
        self.attendees = list()
    
    def __add__(self, employee):
        print(f'Employee with id {employee.id} added to the meeting')
        self.attendees.append(employee)
        return self

    def __len__(self):
        return len(self.attendees)

m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3

print(len(m1))


os.system('cls')
class AbstractEmployee(ABC):
    new_id = 1
    def __init__(self):
        self.id = self.new_id
        AbstractEmployee.new_id += 1
    
    @abstractmethod
    def say_id(self):
        pass
    
class Employee(AbstractEmployee):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def say_id(self):
        print(f'My id is {self.id}')
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def del_name(self):
        del self._name

e1 = Employee('name')
e1.say_id()


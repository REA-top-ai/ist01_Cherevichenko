class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name
    
    def get_role_info(self):
        return f'Персона с именем {self.__name}'


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__grades = [100]

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            return 'Ошибка: баллы студента должны быть в диапазоне [0, 100]'
    
    def avg_grade(self):
        return sum(self.__grades) / len(self.__grades)

    def get_role_info(self):
        return f'Студент {self.get_name()}, ID: {self.__student_id}, Средний балл: {self.avg_grade()}'

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject
        self.__salary = 0
    
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            return f'Ошибка: зарплата должна быть больше 0'
    
    def get_salary(self):
        return self.__salary

    def get_role_info(self):
        return f'Преподаватель {self.get_name()}, ведёт дисциплину {self.__subject}'






























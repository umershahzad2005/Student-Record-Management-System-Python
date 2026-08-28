from abc import ABC, abstractmethod
class Person(ABC):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @abstractmethod
    def displayInfo(self):
        pass




class Student(Person):

    def __init__(self, name, rollNo, age, dept, section, cgpa):
        super().__init__(name, age)
        self.__rollNo = rollNo
        self.__dept = dept
        self.__section = section
        self.__cgpa = cgpa

    @property
    def rollNo(self):
        return self.__rollNo

    @property
    def dept(self):
        return self.__dept

    @dept.setter
    def dept(self, value):
        self.__dept = value

    @property
    def section(self):
        return self.__section

    @section.setter
    def section(self, value):
        self.__section = value

    @property
    def cgpa(self):
        return self.__cgpa

    @cgpa.setter
    def cgpa(self, value):
        self.__cgpa = value

    def displayInfo(self):
        print(f"Name: {self.name}", end="\n")
        print(f"Roll No: {self.rollNo}", end="\n")
        print(f"Age: {self.age}", end="\n")
        print(f"Department: {self.dept}", end="\n")
        print(f"Section: {self.section}", end="\n")
        print(f"CGPA: {self.cgpa}", end="\n")
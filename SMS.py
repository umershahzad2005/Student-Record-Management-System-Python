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

class StudentRecordManagement:

    def __init__(self):
         self.students = []
     
    def addStudent(self):
            name = input("Enter Name: ")
            rollNo = input("Enter Roll #: ")
            age = input("Enter age: ")
            dept = input("Enter Department: ")
            section = input("Enter Section: ")
            cgpa = input("Enter CGPA: ")


            student = Student(
                name,
                rollNo,
                age,
                dept,
                section,
                cgpa
            )

            self.students.append(student)
            
            print("Record Added successfully")



    def deleteAll(self):
        if not self.students:
            print("No record found")

        confirmation = input("Are you sure to delete all student records (y/n): ")

        if confirmation.lower() == 'y':
            self.students.clear()
            print("Delete all record successfully")
        else:
            print("Operation Failed")


    def viewAll(self):
        if not self.students:
            print("No Record found")
        else:
            for i in self.students:
                i.displayInfo()
                return


    def searchRoll(self):
        if not self.students:
                    print("No record found")

        inputRollno = input("Enter Roll No: ")

        for student in self.students:

            if student.rollNo == inputRollno:
                student.displayInfo()
                return

        print("No Record Found")
                


    def updateRecord(self):

        if not self.students:
            print("No record found")

        inputRecord = input("Enter Roll No: ")

        for std in self.students:
            if std.rollNo == inputRecord:
                std.name = input("Enter Name: ")
                std.age = input("Enter Age: ")
                std.dept = input("Enter Department: ")
                std.section = input("Enter Section: ")
                std.cgpa = input("Enter CGPA: ")
                print("Record Update Successfully")
                return
      
        print("No record found")


    def removeRecord(self):
        if not self.students:
            print("No record found")

        inputRecord = input("Enter Roll No: ")

        for std in self.students:
            if std.rollNo == inputRecord:
                self.students.remove(std)
                print("Remove Data Successfully")
                return

        print("No Record found")

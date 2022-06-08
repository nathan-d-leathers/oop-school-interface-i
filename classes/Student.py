import csv
import os.path
from classes.Person import Person

class Student(Person):
    student_list = []
    def __init__(self, name, age, password, role, school_id):
        super().__init__(name,age,password,role,)
        self.school_id = school_id

   
    @classmethod
    def objects(cls):
        students = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(Student(**dict(row)))
        return students
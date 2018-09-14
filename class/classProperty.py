class Student:
    num_students=0
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        Student.num_students+=1

    def print_all(self):
        print("\nname: " + self.name + " \nage:" + str(self.age) + " \ngender:" + self.gender)

    def add_marks(self,marks):
        self.marks=marks
#defining class method
    @classmethod
    def print_num(cls):
        print(cls.num_students)
ram=Student('Ram',27,'M')
sita=Student('Sita','23','F')

print(Student.num_students)

'''after using classmethod'''

Student.print_num()





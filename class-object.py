class Employee:
    empid = 100
    name = 'khushi'
    # salary = 10000

    def __init__(self,name,salary) -> None: 
        self.name = name
        self.salary = salary

    @staticmethod
    def f1():
        print("hello")

    @classmethod
    def f2(cls):
        print(cls.name)

t1=Employee("khushi",20000)
t1.f1() 
t1.f2()       
Employee.f2()
Employee.f1()
       
    
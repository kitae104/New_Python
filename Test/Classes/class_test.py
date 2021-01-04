class Person:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age


    def aboutMe(self):
        print("저의 이름은 " + self.Name + "이구요, 제 나이는 " + self.Age + "살 입니다.")

p = Person("홍길동", "20")
p.aboutMe()

class Employee(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.Salary = salary

    def doWork(self):
        print("열심히 일을 합니다.")

    def aboutMe(self):
        Person.aboutMe(self)
        print("제 급여는 " + self.Salary + "원 입니다.")

objectEmployee = Employee("김철수", "18", "5000000")
objectEmployee.doWork()
objectEmployee.aboutMe()
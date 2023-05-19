class person:
    def __init__(self,Name,phone,NID,program):
        self.Name=Name
        self.phone=phone
        self.__NID=NID
        self.faculty="commerce"
        self.program=program
        self.semester="2"
        self.year="2023"

    def person_acc_detail(self):
            print("Name:",self.Name,"\nphone:",self.phone,"\nNID:",self.__NID,"\nfaculty:"
                  ,self.faculty,"\nprogram:",self.program,"\nsemster:",self.semester,"\nyear:",self.year)
class doctor(person):
    def __init__(self,Name, NID, phone, program,doctorCode,course,salary,hoursWorked=0):
        super(doctor, self).__init__(Name, NID, phone, program)
        self.doctorCode=doctorCode
        self.course=course
        self.salary=salary
        self.hoursWorked=int(hoursWorked)

    def doc_account_details(self):
        person.person_acc_detail(self)
        print("doctor code:",self.doctorCode,"\ncourse:",self.course,"\nsalary:",self.salary,"\nhours worked:",self.hoursWorked)
    def check_course(self):
        print("the current course is:",self.course)
    def change_course(self,NewCourse):
        self.course=NewCourse
        print("the new course is:",self.course)
    def check_hours_worked(self):
        print("hours worked is:",self.hoursWorked)
    def check_the_salary(self):
        if self.hoursWorked>30:
            overtime=self.hoursWorked-30
            overtimeAmount=(overtime*(self.salary/30))
            total_salary=self.salary+overtimeAmount
            print("the total salary is:",total_salary)
        else:
            print("the total salary is:",self.salary)
    def add_hours_worked(self,addedHours):
        self.hoursWorked=self.hoursWorked+addedHours
        print("hours after addition :",self.hoursWorked)
    def exit(self):
        print("you've logged out!\nEXIT")
class student(person):
    def __init__(self,Name, NID, phone, program,studentID,uniEmail):
        super(student, self).__init__(Name, NID, phone, program)
        self.studentID=studentID
        self.uniEmail=uniEmail
    def studentAccDetails(self):
        person.person_acc_detail(self)
        print("student ID:",self.studentID,"\nUniveristy email:",self.uniEmail)
    def checkNID(self):
        print("the NID is:",self._person__NID)
    def changeNID(self,newNID):
        self._person__NID=newNID
        print("the new NID is:",self._person__NID)
    def exit(self):
        print("you have logged out!\nEXIT")
obj1=doctor("doctor.bahlol","010012345", 2122557, "bis", 12345, "python", 20000, 40)
obj2=student("gehad", "0100123455", "2122345", "bis", 2122519, "gehadwael@gmail.com")
obj1.doc_account_details()
obj1.check_course()
obj1.change_course("java")
obj1.check_hours_worked()
obj1.check_the_salary()
obj1.add_hours_worked(5)
obj1.exit()
obj2.studentAccDetails()
obj2.checkNID()
obj2.changeNID(123457897)
obj2.checkNID()
obj2.exit()




















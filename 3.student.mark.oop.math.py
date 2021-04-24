#Importing the library math and numpy 
import math
import numpy as np
import curses 

#student management 
Student=[]
StudentID=[]
Course=[]
CourseID=[]
Mark=[]
Credit=[]
gpa_s=[]



        #------------------------ Class for Student, Course, Mark ------------------------#
#Create class and object for student, course,mark
class Students:
    def __init__(self,id,name,dob):
        self.__id=id
        self.__name=name
        self.__dob=dob
        Student.append(self)
        StudentID.append(self.__id)

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob    


class Courses:
    def __init__(self,id,name,credits):
        self._id=id
        self._name=name
        self._credits=credits 
        Course.append(self)
        CourseID.append(self._id)
        Credit.append(self._credits)

    def get_id(self):
        return self._id
    def get_name(self):
        return self.name 
    def get_credit(self):
        return self._credits


class Marks:
    def __init__(self,a,b,mark,Gpa=0):
        self._a=a
        self._b=b
        self._mark=mark
        Mark.append(self)

    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    def get_mark(self):
        return self.mark
    def set_GPa(self):
        self.Gpa=Gpa
   

        #--------------------Create function get data from user------------------------------#  

#Create input of number of student 
def numberofstudent():
    student_class=int(input("Enter the number of student in  class:"))
    if(student_class<=0):
        print("Doesn't exits")
        return 'False'
    else:
        return student_class


#Create function and add-student-information into this function
def add_student_infor():
    print("=== ADD STUDENT INFORMATION ===")
    
    id=input("Enter the ID:")
    name=input("Enter the student name:")
    dob=input("Enter the dob student:")
    st_infor={
        'id':id,
        'name':name,
        'dob':dob
    }
    StudentID.append(id)
    Student.append(st_infor)
    


#Create function to input number of course
def number_course():
    print("====NUMBER COURSE===")
    number_course=int(input("Enter the number of course are:"))
    if(number_course<=0):
        print("Doesn't exits")
        return 0
    else:
        return number_course

#Create a function to add course         
def add_course():
    name=input("Enter the name course:")
    id=input("Enten the ID course: ")
    cd=input("Enter the credits are:")
    course_f={
        'cd':cd,
        'name':name,
        'id':id
    }
    Course.append(course_f)
    CourseID.append(id)


#Create mark for students
def mark_mana(): 
    g=1
    tu=len(Student)
    while g<=tu:
        g+=1
        a= input("Enter the ID Student: ")
        if a in StudentID:
            for i in range(0,len(Course)):
                b= input("Enter the ID Course: ")
                if b in CourseID:
                    mark=math.floor(float(input("Enter mark of Student: ")))
                    kk={
                       'a':a,
                       'b':b,
                       'mark':mark
                
                   }
                else:
                    print("Flase ID Student")
                    break
                Mark.append(kk)

        else:
            print("False ID course")
            break
def aver_gpa(self):
    print("===++++++======")
    value=np.array([self.mark])
    cre=np.array([self.credit])
    ol=input("Enter the ID student:")
    if ol in self.id:
        for i in range (len(Mark)):
            gpa=value[i]/cre[i]
            return gpa
    print(gpa)

def caculate_mark(self):
    print("=====GPA FIND ======")
    id_a=input("Enter the ID:")
    if id_a in self.id:
        marks=input("Enter the mark:")
    Mark.append(marks)

    cre_value=[Credit]
    mark_val=[Mark]
    name_again=input("Enter the name_that you want to caculate are:")
    gpa=mark_val/cre_value
    return gpa
    
         #-------------Function to show information of student, course,mark,GPA-----------------#

#Create a function to show all of student in class
def show_student():
    print("==== LÍST STUDENT === ")
    for i in range(0,len(Student)):
        print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")

#Create a function to show all of student course 
def show_course():
    print("=== LIST COURSE ===")
    for i in range(0,len(Course)):
        print(f"ID:{Course[i]['id']}  Name :{Course[i]['name']} Credits:{Course[i]['cd']}")

#Function to show the mark of student 
def show_mark():
    print("=== LIST MARK ===")
    for i in range(0,len(Mark)):
        print(f"ID-course: {Mark[i]['b']} ID-Student: {Mark[i]['a']}  mark:{Mark[i]['mark']}")

#Function to show the GPA of Student
def GPA_decending():
    arr=np.array([gpa_s])
    arr[::-1].sort()
    print("=====LIST====")
    print("The list is %s:\n"%(arr))
    #-------------------------------------MAIN-------------------------------_----#


#recall student 
s=int(numberofstudent())
l=1
while l<=s: 
    l+=1
    add_student_infor()
show_student()

#recall course 
c=int(number_course())
p=1
while p<=c:
    p+=1
    add_course()
show_course()


#recall mark
mark_mana()

print("""===YOUR OPTION===""")
print("1.YES")
print("2.NO")
for i in range (0,len(Course)):
    ol=int(input("Enter your option are:"))
    if ol ==1:
        print("====MARK OF STUDENT ====")
        show_mark()
        break
    else:
        break   

#recall Gpa_student
l=aver_gpa()
l.getaver_gpa()
caculate_mark()
# 5. Create Student class | rno,name,email,marks(int), __cno |
#    | __get_grade() : Grade | display_info : rno,name,email,cno,grade |

class Student:
    def __init__(self, rno, name, emailid, marks, cno):
        self.__cn = cno
        self.rno=rno
        self.name=name
        self.emailid=emailid
        self.marks=marks

    def __get_grade(self):
       if self.marks >= 90:
            return "A"
       elif self.marks >= 80:
            return "B"
       elif self.marks >= 70:  # True
            return "C"
       elif self.marks >= 60:
            return "D"
       else:
            return "F"

    def display_info(self):
        print(f"Rno : {self.rno} | Name : {self.name}")
        print(f"Email : {self.emailid} | Grade {self.__get_grade()}")

std_1 = Student(1,"sbc","xyz",91, 89522)
std_1.display_info()


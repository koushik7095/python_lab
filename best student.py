class student:
    def __init__(self,name,yr):
        self.name=name
        self.yr=yr
    def display_stud_details(self):
        print(f"name:{self.name},class:{self.yr}")

class skills:
    def __init__(self,sk1,sk2,sk3):
        self.sk1=sk1
        self.sk2=sk2
        self.sk3=sk3
    def skills(self):
        print(f"skills are {self.sk1},{self.sk2},{self.sk3}")

class beststudent(student,skills):
    def __init__(self,fname,cls,sk1,sk2,sk3,rno):
        student. __init__(self,fname,cls)
        skills. __init__(self,sk1,sk2,sk3)
        self.rno=rno
    def display_student(self):
        print("the best student...")
        self.display_stud_details()
        self.skills()
        print(f"student id:{self.rno}",end="\n")

chandu=beststudent("chandu pasula yadav","2nd year","python","dbms","stld","96")
santoosh=beststudent("santoosh","2nd year","com","sdc","AI","104")
sai=beststudent("sai","2nd year","engineering graphics","stld","dm","90")

chandu.display_student()
santoosh.display_student()
sai.display_student()

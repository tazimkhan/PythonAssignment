class student:
    def __init__(self,x,y,z,v):
        self.rollno=x
        self.name=y
        self.sem=z
        self.branch=v
s1=student(100,"amit",2,'IT')
s2=student(102,'aashu',4,'CS')
print(s1.rollno,s1.name,s1.sem,s1.branch)
print(s2.rollno,s2.name,s2.sem,s2.branch)
'''
print(s1.__dict__)
'''

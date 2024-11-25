student={}
Is=[]
n=int(input("enter the number of students:"))
for i in range(n):
	name=str(input("enter the student's name:"))
	age=int(input("enter the student's age:"))
	grade=str(input("enter the student's grade:"))
	student[name]=(age,grade)
print(student)

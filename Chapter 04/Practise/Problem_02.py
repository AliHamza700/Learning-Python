Marks=[]
n=int(input("Enter the Number of the students : "))
for i in range(n):
    mark=int(input("Enter the marks of the student : "))
    Marks.append(mark)
    Marks.sort()#Sort the list in ascending order
print(Marks)
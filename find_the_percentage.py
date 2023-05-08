#asking number of students
n = int(input("Enter number of students: "))

#creating student empty dictionary
student = {}

#asking key(name) and value(marks) from user and storing it into student dictionary 
for i in range(n):
    user_input = input("Enter student name and marks separated by space: ").split()
    
    #storing name into separate list
    
    #storing marks into separate list
    marks=[]
    for i in range(1,4):
        marks.append(user_input[i])
    
    #appending key and values in dictionary
    student[user_input[0]] = marks


#asking name of student to calculate average marks
name = input("Enter name of student: ")

total = 0
avg = 0
if name in student:
    for mark in student[name]:
        total = float(mark)+total
    avg=float(total/3)
    formatted_avg = format(avg, ".2f")
print(formatted_avg)    


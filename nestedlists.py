#taking input in nested list

n = int(input("Enter number of students: "))
result=[]
marks=[]

for i in range(n):
    name = input("Enter name: ")
    score = float(input("Enter marks: "))
    result.append([name,score])
    marks.append(score)

maximum=max(marks)
print(maximum)

#finding second highest score
#for scores in result:
    #for i in range(n):
        


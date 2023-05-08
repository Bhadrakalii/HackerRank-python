#taking input in nested list

n = int(input("Enter number of students: "))
result=[]
marks=[]

for i in range(n):
    name = input("Enter name: ")
    score = float(input("Enter marks: "))
    result.append([name,score])
    marks.append(score)

minimum=min(marks)

#finding second lowest score
marks.sort()

for i in range(n):
     if(marks[i]!=minimum):
          second_lowest=marks[i]
          break

names=[]
for scores in result:
      if(scores[1]==second_lowest):
            names.append(scores[0])

#arranging name in alphabetic order
names.sort()

#printing names
for items in names: 
    print(items, end='\n')
            
        


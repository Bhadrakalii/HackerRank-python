#asking for number of commands
n = int(input("Enter number of commands:"))
arr=[]

#iterating through loop to ask commands and data
for i in range(n):
    user_input = input("Enter command and values separated by space: ").split()
    command_count = len(user_input)
    if command_count==3:
        index=user_input[1]
        value=user_input[2]
        
        arr.insert(int(index),int(value))

    elif command_count==2:
        value=user_input[1]

        if user_input[0]=='remove':
           arr.remove(int(value))
        else:
            arr.append(int(value))


    else:
        if user_input[0]=='print':
            print(arr)
        elif user_input[0]=='sort':
            arr.sort()
        elif user_input[0]=='reverse':
            arr.reverse()
        else:
            arr.pop()

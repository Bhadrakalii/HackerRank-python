#asking for number of commands
n = int(input("Enter number of commands:"))
arr=[]

#iterating through loop to ask commands and data
for i in range(n):
    user_input = input("Enter command and values separated by space: ").split()
    command_count = len(user_input)  
    print(command_count)
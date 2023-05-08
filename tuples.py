n=int(input("Enter value of n: "))

num = tuple(input("Enter two values separated by a space: ").split())

print(num)

hash_value=hash(num)
print(hash_value)

'''
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))
'''
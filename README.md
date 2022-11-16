# Nalin

1)Python?

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed

2)Create a login function

print('Create User')
User_Name = input('Create User_Name\n')
Password = input('Create Password\n')
Enter_User = input('Enter User Name\n')
Enter_Password=input('Enter the Password\n')
if User_Name == Enter_User and Password == Enter_Password:
    print("Successfully Login")
else:
    print('Incorrect Username or Password')

3)Write a program to find odd or even number ?

print('Find the odd or Even')
Type_Number = int(input('Enter the number\n'))
if Type_Number % 2 == 0:
 print("its even number")
else:
     print("its odd number")

4)Create a list of fruits and iterate through them

print('List of Fruits')
Fruits={'Orange','Apple','Banana','Pineapple','Mango','Watermelon','JackFruit','Peach','Grapes'}
for x in Fruits:
    print(x)

print('Create User')
User_Name = input('Create User_Name\n')
Password = input('Create Password\n')
Enter_User = input('Enter User Name\n')
Enter_Password=input('Enter the Password\n')
if User_Name == Enter_User and Password == Enter_Password:
    print("Successfully Login")
else:
    print('Incorrect Username or Password')


print('Find the odd or Even')
Type_Number = int(input('Enter the number\n'))
if Type_Number % 2 == 0:
 print("its even number")
else:
     print("its odd number")

print('List of Fruits')
Fruits={'Orange','Apple','Banana','Pineapple','Mango','Watermelon','JackFruit','Peach','Grapes'}
for x in Fruits:
    print(x)
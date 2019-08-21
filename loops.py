# counts from negative 20 to 50
for idx in range(-20, 51, 1):
    print(idx)

# counts from 0 to 21 by 2s
for x in range(0, 21, 2):
    print(x)

# gives the average of 3 input numbers
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a final number: "))
averageOfThe3 = (num1 + num2 + num3) / 3
print("The average of", num1, ",", num2, ",and", num3, "is", averageOfThe3)

# prints out only the multiples of 4 between 4 and 100
multOfFours = 4
while multOfFours <= 100:
    print(multOfFours)
    multOfFours = multOfFours + 4

# asks for and confirms a user input password
userPassword = input("Enter a new password: ")
userCheck = input("Confirm your password: ")
while(userPassword != userCheck):
    userCheck = input("That is incorrect. Please enter the correct password or press 'q' to quit: ")
    if userCheck == "q":
        userCheck = userPassword
# step1-create a python lab5 file
# step2- collecting input for user
number1=int(input("Enter number 1:"))
# step3- using if statement to check if input is divisble by 3 and 5
for number in range(1, number1):
    if (number1%3==0) and (number1 %5==0):
        print(number1, "tic tac")
# step4- using the if statement to check if input is divisible by 3
    if (number1%3==0):
        print(number1, "tic")
# step5- using the if statement to check if input is divisible by 5
    if(number1%5==0):
        print(number1,"tac")
# step6- using while loop statement to print numbers from 1-20
i=1
while i<21:
    i+=1
    print(i)
#step7 - using the while loop statement to modify code in step 6
input1=int(input("Enter input:"))
input1=1
while input1<16:
    input1+=1
    if input1%3==0 and input1%5==0:
        print(input1,"tic tac")
    elif input1%3==0:
        print(input1,"tic")
    elif input1%5==0:
        print(input1,"tac")
#step8- using random_generator function to generate random numbers
import random
print(random.randint(1, 5))
#step9-
limit=5
while limit>0:
    user_value = int(input("Enter the value"))
    if user_value>0:
        print(user_value, "/n successful")
        break
    else:
        limit=1
        print("invalid entry, please enter a valid value")
#step10-
import random
user_value = int(input("Enter int value:"))
main = random.randint(4, user_value)
limit = 0
while True:
    limit+=1
    my_value = int(input("first value"))
    if my_value==main:
        print("perfect")
        break
    elif my_value!=main:
        print("both numbers dont match")
    else:
        print("invalid")
import random
while 1:
    op = input('Roll the dice? (y/n): ')
    if(op.lower() == 'y'):
        random_number1 = random.randrange(1 , 10)
        random_number2 = random.randrange(1 , 10)
        print(f"({random_number1} , {random_number2})")
    elif(op.lower() == 'n'):
        print("Thank you for playing")
        break
    else:
        print("Invalid Operation")

        

import random
while 1:
    count = 1
    guss_number = random.randint(1, 100)
    while 1:
        try:
            number = int(input('Guess the number between 1 and 100: '))
            if count == 5:
                print(f"Number is {guss_number}")
                print("You lose! Thanks")
                print("You can guess again")
                break
            if (number > guss_number):
                count+=1
                print("Too high")
            elif number < guss_number:
                count+=1
                print("Too low")
            else:
                print("Congratulations! You guessed the number.")
                break
        except ValueError:
            print("Please enter a valid number")

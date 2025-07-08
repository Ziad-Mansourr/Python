import random
guss_number = random.randint(1, 100)
while 1:
    try:
        number = int(input('Guess the number between 1 and 100: '))
        if (number > guss_number):
            print("Too high")
        elif number < guss_number:
            print("Too low")
        else:
            print("Congratulations! You guessed the number.")
    except ValueError:
        print("Please enter a valid number")

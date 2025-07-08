import random
rps = ['r', 'p', 's']
count = 0
while 1:
    op = input('Rock, Paper, or scissor? (r/p/s): ').lower()
    if op in rps:
        Cop = random.choice(rps)
        if op == 'r' and Cop == 'p':
            print('You chose 🪨')
            print('Computer chose 📄')
            print('You lose')
        elif op == 'r' and Cop == 's':
            print('You chose 🪨')
            print('Computer chose ✂️')
            print('You win')
        elif op == 'r' and Cop == 'r':
            print('You chose 🪨')
            print('Computer chose 🪨')
            print('Draw')
        elif op == 'p' and Cop == 'r':
            print('You chose 📄')
            print('Computer chose 🪨')
            print('You win')
        elif op == 'p' and Cop == 's':
            print('You chose 📄')
            print('Computer chose ✂️')
            print('You lose')
        elif op == 'p' and Cop == 'p':
            print('You chose 📄')
            print('Computer chose 📄')
            print('Draw')
        elif op == 's' and Cop == 'r':
            print('You chose ✂️')
            print('Computer chose 🪨')
            print('You lose')
        elif op == 's' and Cop == 'p':
            print('You chose ✂️')
            print('Computer chose 📄')
            print('You win')
        elif op == 's' and Cop == 's':
            print('You chose ✂️')
            print('Computer chose ✂️')
            print('Draw')
    else:
        print("Invalid Choice")

    c = input('Continue? (y/n): ')
    if (c.lower() == 'y'):
        count += 1
    elif (c.lower() == 'n'):
        print("Thank you for playing")
        break

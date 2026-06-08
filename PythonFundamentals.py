#PYTHON SYNTAX

#if else statement
name = "John" 
if len(name) < 3:
    print("Name must be at least 3 characters long.")
elif len(name) > 50:
    print("Name must be less than 50 characters long.")
else: 
    print("Name look good")

#while loop - guessing game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
    else:    
        print("Sorry, you failed!")



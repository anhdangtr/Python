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

#pratice while - start stop quit game
command = ""
started = False
stopped = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if stopped:
            print("car already stopped")
        else:
            stopped = True
            print("car stopped")
    elif command == "help":
        print(""""
        start - to start 
        stop - to stop
        quit - to quit
        """)
    elif command == "quit":
        print("quit")
        break
    else: 
        print("Unknown command")


#for loop

for item in range(5,10,2): #start, stop, step
    print(item)


#list
numbers = [1,2,3,4,5]
#tuples
numbers = (1,2,3,4,5) #immutable - cannot be changed

#unpacking
coordinates = (1,2,3)
x,y,z = coordinates # x=1, y=2, z=3


#dictionaries
customer = {
    "name": "John Doe",
    "age": 30,
    "is_verified": True
}
print(customer["name"]) #John Doe
print(customer["birthday"]) #key error
print(customer.get("birthday", "January 1, 1990")) #January 1, 1990

#mapping phone
phone = input("Phone: ")

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") #! is not found value

print (output)

#functions
def greet_user():
    print("Hi there!")
    print("Welcome aboard")

greet_user()

def greet_user(name):
    print(f'Hi {name}!')

greet_user("John")


#function convert to emoji
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😞"
    }

    output = "" 
    for word in words:
        output += emojis.get(word, word) + ""
    return output

#exeption
try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be zero")

class Person:
    def __init__(self, name): #constructor
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")
john = Person("John")
print(john.name)
john.talk()

#inheritance
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()

#modules
import converters
print(converters.kg_to_lbs(70))

from converters import kg_to_lbs
print(kg_to_lbs(70))
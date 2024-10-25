import random

n1 = random.randint(10, 99) 
print(n1)
n3 = input("Enter Your Name: ")

print("==================================")
print("Welcome to", n3)
print("==================================")

while True:
    try:
        n2 = int(input("Guess the Number: ")) 
        if n2 > n1:
            print("Sorry!!!.. Enter less than", n2)
        elif n2 < n1:
            print("Sorry!!!.. Enter greater than", n2)
        else:
            print("Number is Match")
            print("*********", n3, "is the Winner **********")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

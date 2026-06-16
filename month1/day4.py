# Key Functions in the random Toolbox
# random.randint(a, b): Generates a random integer between a and b — both a and b are included. e.g., randint(1, 6) simulates a die roll.
# random.randrange(a, b): Similar to randint, but b is excluded. randrange(1, 3) only gives 1 or 2.
# random.random(): Returns a random float between 0.0 and 1.0 (1.0 is never actually reached).
# random.uniform(a, b): Returns a random decimal number within a specific range, like between 1.5 and 5.5.
# random.choice(sequence): Like reaching into a bag and pulling one item out at random. Pass it a list or tuple.
# random.shuffle(sequence): Mixes up the entire sequence in place — like shuffling a deck of cards before a game.
# Pro-Tip: Always prefix these functions with the module name: random.randint(). If you just type randint(), Python won't know which toolbox it belongs to

import random 

#lets make a guessing game 
a=int(input("give me the range u wanna guess the number in"))
b=int(input("give me the range u wanna guess the number in"))
num=random.randint(a,b)
guess=int(input("what is ur guess lil bro :"))
count=0
while guess !=num :
    guess=int(input(" guess again lil bro :"))   
    count=count+1
    if(guess > num ):
        print("hint: a little to the left dawg")
    elif (guess < num): 
        print("hint: a little to the right dawg")
    else:
        print("u figured it !!")    
        
print(f"it took u {count} times to figure the number")
     
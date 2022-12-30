import random
number = random.randint(1,100)
print("I have a number in my mind. Can you Guess it?")
number_of_guess_left = 3
while number_of_guess_left > 0:
    guess = int(input('Guess a number: '))
    if guess != number:
        number_of_guess_left -= 1

    if (guess == number):
        print('"congratulation you win"','Your Score',10)
        break
    elif (guess < number):
        print('"have one more try"','your guess was too small')
    else:
        print('"have one more chance"','Your guess was too high')
if guess == number:
    print('"congratulation you win"','Your Score',10)
else:
    print('"better luck next time"','Your Score',0)


  

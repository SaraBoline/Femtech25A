
num = random.randint(1, 10)
guess = None
guesses = 0

while guess != num:
    guess = input("Guess a number between 1 and 10:")
    guess = int(guess)
    
    if guess == num:
        print ("Congratulations! you won using "+ str(guesses) + " guesses" )
        break
    
    else:
        print ("Nope, sorry, try again!" )
        guesses = guesses +1
        
        #print ("your number of guesses is:" + str(guesses))
        

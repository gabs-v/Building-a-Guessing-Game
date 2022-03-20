#Building a basic guessing game using programing structures I've learned so far! :)

secret_word = "giraffe"
guess = " "
times_guessed = 0 
guess_limit  = 3
out_of_guesses = False 

while guess != secret_word and not (out_of_guesses):
    if times_guessed < guess_limit: #this is checking if they've reached the user has reached the guess limit
        guess = input("Enter guess: ")
        times_guessed += 1
        if times_guessed == 1:
            print("Hint: It's an animal")
        elif times_guessed == 2 :
            print("A tall animal...")
    else:
        out_of_guesses = True


if out_of_guesses:
    print ("Out of guesses. Try again! ")
else:
    print("Yay!You got it!!")

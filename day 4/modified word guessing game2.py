import random
name=input("what is ur name? ")
print("good luck ", name)
words=['saiteja','dinesh','kranthi','swaraj','suryateja','rohan','vamsi','python']
word=random.choice(words)
print("guess the characters")

hint = input("Do you want a hint? (yes/no): ").lower()
if hint == "yes":
    hints = {
        'saiteja': 'HEEROO',
        'dinesh': 'full stack developer',
        'python': 'programming language',
        'suryateja': 'spectacles',
        'rohan': 'smart boy in mechanical',
        'vamsi': 'data analyst',
        'swaraj': 'full stack developer ka baap',
        'kranthi': 'amazon'
    }
    print("Hint:", hints.get(word))
guesses=''
turns=5
while turns>0:
    progress=[char if char in guesses else "_" for char in word]
    print(" ".join(progress))

    if "_" not in progress:
        print("You win!")
        print("The word is:", word)
        break
    guess=input("Guess a character: ")
    guesses+=guess

    if guess not in word:
        turns-=1
        print("Wrong!")
        print("You have", turns, "more guesses")

        if turns==0:
            print("You lose!")


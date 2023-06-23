import random
name=input("what is ur name? ")
print("good luck ", name)
words=['saiteja','dinesh','kranthi','swaraj','suryateja','rohan','vamsi','python']
word=random.choice(words)
print("guess the characters")
print("if you want hint type (yes) else (no): ")
hint=input().lower()
if hint=="yes":
    if word=="saiteja":
        print("hint is HEEROO")
    elif word=="dinesh":
        print("full stack dveloper")
    elif word=="python":
        print("programming language")
    elif word=="suryateja":
        print("hint is spectacles")
    elif word=="rohan":
        print("hint smart boy in mechanical")
    elif word=="vamsi":
        print("hint is data analyst")
    elif word=="swaraj":
        print("full stack developer ka baap")
    elif word=="kranthi":
        print("hint is amazon")
else:
    print("your karma")
guesses=''
turns=5
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed+=1

    if failed==0:
        print("\nu win")
        print("the word is: ", word)
        break
    print()
    guess=input("guess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")

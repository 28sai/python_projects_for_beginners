import random
fn=int(input("enter first number:- "))
ln=int(input("enter last number:- "))
x=random.randint(fn, ln)
print("\n\you have only 3 chances to guess the number\n")
count=0
while count<3:
    count+=1
    guess=int(input("guess a num: "))
    if x==guess:
        print("congratulations you did it in ",count," try")
        break
    elif x>guess:
        print("you guessed too small!")
    elif x<guess:
        print("you guessed too high!")
if count>=3:
    print("\nthe number is %d" % x)
    print("better luck nxt time!")


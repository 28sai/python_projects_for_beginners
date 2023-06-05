lst=[0,1,2,3]
def display(lst):
    print("the current list is: ")
    print(lst)
def user_input(lst):
    choice="wrong"
    while choice not in lst:
        choice=int(input("pick a position: "))
        if choice not in lst:
            print("not a valid input")
    return choice
def replacement(lst,position):
    lst[position]=input("enter new one:")
    return lst
def play():
    choice="wromng"
    while choice not in ['y','n']:
        choice=input("want to play again(y/n)")
        if choice not in ['y','n']:
            print("i dont understand")
    if choice == 'y':
        return True
    else:
        print("bye come back again")
        return False
lst=[0,1,2,3]
game=True
while game:
    display(lst)
    position=user_input(lst)
    lst=replacement(lst,position)
    display(lst)
    game=play()
    
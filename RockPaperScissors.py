import random as R

while True:
    me = input("RockPaperScissors: ")
    if (me == ("Rock" or "Paper" or "Scissors")):
        break
    else:
        print("please enter again")
        continue

bot = ("Rock", "Paper", "Scissors")

def get_number():
    num = R.randint(0, 2)
    return bot[num]

def rps(a, b):
    if (a == b):
        print("draw")
    else:
        if ((a == "Rock") and (b == "Scissors")):
            return print("you win")
        elif ((a == "Paper") and (b == "Rock")):
            return print("you win")
        elif ((a == "Scissors") and (b == "Paper")):
            return print("you win")
        else:
            return print("you lost")
        
bot = get_number()
print("you:", me, "| bot:", bot)
rps(me, bot)
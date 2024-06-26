import random

print("Welcome to Rock paper scissors")
print("Made by me\n")
print("Choose AI's difficulty")
print("1) easy")
print("2) medium")
print("3) hard")
inp = int(input(""))


gmexit = 0
def main():
    while 1 == 1:
        global gmexit, inp
        if inp == 1:
            print("rock, paper or scissors?")
            inp_easy = input()
            if inp_easy == "rock":
                rand_easy_rock =  random.randint(1,10)
                if rand_easy_rock <= 5:
                    print("AI: Scissors")
                    print("You won!")
                elif rand_easy_rock >= 9:
                    print("AI: Rock")
                    print("Draw!")
                else:
                    print("AI: paper")
                    print("You lose!")
            elif inp_easy == "paper":
                rand_easy_paper = random.randint(1,10)
                if rand_easy_paper <= 5:
                    print("AI: rock")
                    print("You won!")
                elif rand_easy_paper >= 9:
                    print("AI: paper")
                    print("Draw!")
                else:
                    print("AI: scissors")
                    print("You lose!")
            elif inp_easy == "scissors":
                rand_easy_scissors = random.randint(1,10)
                if rand_easy_scissors <= 5:
                    print("AI: paper")
                    print("You won!")
                elif rand_easy_scissors >= 9:
                    print("AI: scissors")
                    print("Draw!")
                else:
                    print("AI: rock")
                    print("You lose!")
            else:
                print("incorrect message! please type rock papar or scissors")

        elif inp == 2:

            ai_decision = "unknown"
            print("rock, paper or scissors?")
            rand_normal = random.randint(1,9)
            if rand_normal >= 6:
                ai_decision = "rock"
            elif rand_normal <= 3:
                ai_decision = "paper"
            else:
                ai_decision = "scissors"
            inp_normal = input("")
            if inp_normal == "rock":
                if ai_decision == "rock":
                    print("AI: rock")
                    print("Draw!")
                elif ai_decision == "paper":
                    print("AI: paper")
                    print("You lose!")
                else:
                    print("AI: scissors")
                    print("You win!")
            elif inp_normal == "scissors":
                if ai_decision == "rock":
                    print("AI: rock")
                    print("You lose!")
                elif ai_decision == "paper":
                    print("AI: paper")
                    print("You win!")
                else:
                    print("AI: scissors")
                    print("Draw!")
            elif inp_normal == "paper":
                if ai_decision == "rock":
                    print("AI: rock")
                    print("You win!")
                elif ai_decision == "paper":
                    print("AI: paper")
                    print("draw!")
                else:
                    print("AI: scissors")
                    print("You lose!")
            else:
                print("incorrect message! please type rock papar or scissors")
        elif inp == 3:    
            print("rock, paper or scissors?")
            inp_easy = input()
            if inp_easy == "rock":
                rand_easy_rock =  random.randint(1,10)
                if rand_easy_rock <= 2:
                    print("AI: Scissors")
                    print("You won!")
                elif rand_easy_rock >= 9:
                    print("AI: Rock")
                    print("Draw!")
                else:
                    print("AI: paper")
                    print("You lose!")
            elif inp_easy == "paper":
                rand_easy_paper = random.randint(1,10)
                if rand_easy_paper <= 2:
                    print("AI: rock")
                    print("You won!")
                elif rand_easy_paper >= 9:
                    print("AI: paper")
                    print("Draw!")
                else:
                    print("AI: scissors")
                    print("You lose!")
            elif inp_easy == "scissors":
                rand_easy_scissors = random.randint(1,10)
                if rand_easy_scissors <= 2:
                    print("AI: paper")
                    print("You won!")
                elif rand_easy_scissors >= 9:
                    print("AI: scissors")
                    print("Draw!")
                else:
                    print("AI: rock")
                    print("You lose!")
            else:
                print("incorrect message! please type rock papar or scissors")
        else:
            print("Incorrect number, press enter to exit")
            input("")
        print("Play again or exit?\n1) Play again\n2) Exit")
        end = int(input(""))
        if end == 1:
            main()
        elif end == 2:
            print("Goodbye!")
            gmexit = 1
            break
        else:
            print("Incorrect answer, please type 1 or 2")

if gmexit == 0:
    main()
else:
    print("See you later!")
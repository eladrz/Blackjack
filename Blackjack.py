import random
import os


from pic import logo



def clear_console():


    os.system('cls')



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


total_money = 0


flag = input("Do you want to play Blackjack? type y or n:\n").lower()



def Blackjack_Game():
    clear_console()


    print(logo)


    global flag


    global total_money


    com_card = [random.choice(cards)]


    your_card = [random.choice(cards), random.choice(cards)]
    your_score = sum(your_card)
    com_score = sum(com_card)


    money = float(input("How much money would you like to gamble: $"))


    print(f"your cards {your_card}, total score {your_score} ")


    print(f"dealer cards {com_card}, total score {com_score} ")


    card = random.choice(cards)


    if card == 11 and com_score+11 > 21:
        card = 1


    com_card.append(card)
    com_score = sum(com_card)


    while(com_score < 21 and your_score < 21):


        choose = input("Type y for another card or n to pass: ").lower()


        if choose == 'y':


            card = random.choice(cards)


            if card == 11 and your_score+11 > 21:
                card = 1


                print("you get an As")


            your_card.append(card)
            your_score = sum(your_card)

            print(

                f"your cards {your_card}, total score {your_score}, your bet {money}$ ")


        else:


            if your_score < 16:


                print("Your score is under 16")


            else:


                break


    while com_score < 16:


        card = random.choice(cards)


        if card == 11 and com_score+11 > 21:
            card = 1


        com_card.append(card)
        com_score = sum(com_card)


    if your_score > 21:


        total_money -= money
        print("you lose")

        print(

            f"dealer cards {com_card}, total score {com_score}, you lost {money}$")


    elif your_score <= 21 and your_score > com_score or com_score > 21:


        total_money += money


        print("you win")

        print(

            f"dealer cards {com_card}, total score {com_score},  you earn {money}$ ")


    elif com_score == your_score:

        print("its a draw")

        print(

            f"dealer cards {com_card}, total score {com_score},  you lost nothing")


    else:


        total_money -= money
        print("you lose")

        print(

            f"dealer cards {com_card}, total score {com_score}, you lost {money}$ ")


    money = 0


    flag = input(

        "Good game, do you want to play again? type y if yes: ").lower()



while flag == 'y':


    Blackjack_Game()



if total_money > 0:


    print(f"Good Game you get {total_money}$")


elif total_money < 0:


    print(f"Thank you very much you owe us {abs(total_money)}$ ")


else:


    print("Good bay")

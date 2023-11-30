import random

def spin():
    return random.choice( ['1', '2', '3', '4', '5', '6', '777', '8','9'] )
    # return random.choice( ['777'] )

def win():
    a = '''
___  _ ____  _       _      _  _     
\  \///  _ \/ \ /\  / \  /|/ \/ \  /|
 \  / | / \|| | ||  | |  ||| || |\ ||
 / /  | \_/|| \_/|  | |/\||| || | \||
/_/   \____/\____/  \_/  \|\_/\_/  \|
                                     
'''
    return a

def jackpot():
    a = '''

$$\ $$\                         $$\                            $$\     $$\ $$\ 
$$ |$$ |                        $$ |                           $$ |    $$ |$$ |
$$ |$$ |$$\  $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\ $$$$$$\   $$ |$$ |
$$ |$$ |\__| \____$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\\_$$  _|  $$ |$$ |
\__|\__|$$\  $$$$$$$ |$$ /      $$$$$$  / $$ /  $$ |$$ /  $$ | $$ |    \__|\__|
        $$ |$$  __$$ |$$ |      $$  _$$<  $$ |  $$ |$$ |  $$ | $$ |$$\         
$$\ $$\ $$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ $$$$$$$  |\$$$$$$  | \$$$$  |$$\ $$\ 
\__|\__|$$ | \_______| \_______|\__|  \__|$$  ____/  \______/   \____/ \__|\__|
  $$\   $$ |                              $$ |                                 
  \$$$$$$  |                              $$ |                                 
   \______/                               \__|                                 
'''
    return a

def play():
    tokens = 10  # 초기 토큰 개수
    while True:
        print()
        print(f"You have {tokens} tokens.")
        if tokens <= 1:
            print("Game over.")
            # break
            again = input('Do you like to start the game again?...(y/n) >>>>>')
            if again.lower() in ["yes", "y"]:
                chargeCoins = int(input('How many coins would you like to charge? (10~20) >>>>>'))
                if chargeCoins > 20 :
                    print("The input value exceeded 20, so it was set to 20.")
                    tokens += 20
                    continue
                else:
                    tokens += chargeCoins
                    continue
            else:
                print("Goodbye.")
                break

        answer = input("Do you want to play? ")
        if answer.lower() in ["yes", "y"]:
            tokens -= 2  # 슬롯머신을 돌리기 위해 토큰 하나 소비
            result1 = spin()
            result2 = spin()
            result3 = spin()
            print()
            print(f"{result1} | {result2} | {result3}")
            # 슬롯머신 결과에 따라 토큰을 얻거나 잃음
            if result1 == "777" and result2 == "777" and result3 == "777":
                print(jackpot(), "\nYou get 50 tokens!")
                tokens += 50
            elif result1 == result2 == result3:
                print(win(), "\nYou get 10 tokens!")
                tokens += 10
            elif result1 == result2 or result1 == result3 or result2 == result3:
                print(win(), "\nYou get 3 tokens!")
                tokens += 3
            else:
                print("You lose.")
        else:
            print("Goodbye.")
            break 
      

play()

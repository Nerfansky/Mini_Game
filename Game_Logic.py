import time
from statistics import mean
from Get_Bet import Get_Bet
from Spin import Spin
from Create_Missing_Files import Create_Missing_Files
from Clear_Screen import Clear_Screen
import sys


def Game_Logic(balance):
    try:
        Coefficient = {
            "apple": 1,
            "pear": 1.5,
            "zero": 0.1,
            "cherry": 5,
            "orange": 0.5,
            "jackpot": 10
        }

        chances = {
            "apple": 0.2,
            "pear": 0.1,
            "zero": 0.3,
            "cherry": 0.1,
            "orange": 0.2,
            "jackpot": 0.1
        }

        Create_Missing_Files()

        try:
            with open("last_balance.txt", "r") as f:
                content = f.read()
                if content.strip():
                    balance = float(content)
                else:
                    while True:
                        initial_balance = input("how much dib you buy?  ")
                        if initial_balance.isdigit():
                            balance = float(initial_balance)
                            break
                        else:
                            print("Enter a valid number.")
        except FileNotFoundError:
            while True:
                initial_balance = input("how much dib you buy?  ")
                if initial_balance.isdigit():
                    balance = float(initial_balance)
                    break
                else:
                    print("Enter a valid number.")

        while True:
            bet = Get_Bet(balance)
            spin_result = Spin(chances)
            print("\nSpinning The Wheel\n")
            time.sleep(3)

            for _ in range(3):
                print("rolling\n")
                time.sleep(1)
            print("Spin Result:\n\n", spin_result, "\n")

            convertations = [Coefficient[word] for word in spin_result]
            avg = mean(convertations)
            average = (round(avg))
            win = average * bet
            balance += win
            print("Your winnings are", win, "$\n")
            print("Your current balance is", balance, "$\n")

            with open("last_balance.txt", "w") as f:
                f.write(str(balance))

            with open("Data_Base.txt", "a") as file:
                file.write(str(win) + "\n")

            while True:
                response = input("Continue playing (yes/no): ").lower()
                if response != "yes" and response != "no":
                    print("Please enter 'yes' or 'no'.")
                    continue
                elif response == "no":
                    Clear_Screen()
                    sys.exit()
                else:
                    break

    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except Exception as e:
        print("An error occurred:", e)
        with open("Fatal_error.txt", "a") as f:
            f.write("An error occurred: " + str(e) + "\n")

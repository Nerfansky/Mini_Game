def Get_Bet(balance):
    while True:
        try:
            bet = int(input(
                "Make A Bet (Your Balance is {}): "
                .format(balance))
            )
            if 0 < bet <= balance:
                return bet
            else:
                print("Make a correct bet!\nYour max bet can be {}."
                      .format(balance))
        except ValueError:
            print("Enter a valid number")

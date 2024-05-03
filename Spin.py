import random


def Spin(chances):
    Symbols = ["apple", "pear", "cherry", "orange", "jackpot", "zero"]
    result = []
    for _ in range(3):
        symbols = random.choices(Symbols, weights=list(chances.values()), k=3)
        result.append(symbols)
    return result[0]

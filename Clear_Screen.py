import os


def Clear_Screen():
    if os.name == 'nt':
        os.system('cls')
    elif 'TERM' in os.environ:
        os.system('clear')

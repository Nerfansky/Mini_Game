import os


def Create_Missing_Files():
    for filename in ["last_balance.txt", "last_balance.txt", "Fatal_error.txt"]:
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write("")

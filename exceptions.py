"""try:
    x = int(input("what's x "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")"""
def main():
    c = get_number()
    print(f"you are {c} years old")


def get_number():
    while True:
        try:
            l = int(input("how old are you \n"))
        except ValueError:
            pass
        else:
            return l
import pytest
main()


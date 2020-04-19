import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    number_of_quick_picks = int(input("How many picks do you want?"))
    while number_of_quick_picks < 0:
        print("It is not possible to pick below zero")
        numbers_of_picks = input("How many picks do you want?")

    for i in range(number_of_quick_picks):
        quick_pick = []
        for k in range(NUMBERS_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


if __name__ == '__main__':
    main()

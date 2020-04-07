def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    # a. count in 10s from 0 to 100
    for i in range(0, 110, 10):
        print(i, end=' ')
    print()

    # b. count down from 20 to 1
    for i in range(20, -1, -1):
        print(i, end=' ')
    print()

    # c. print n stars. Ask the user for a number, then print that many stars (*), all on one line
    stars = int(input("Please enter the number of stars you wanted"))
    for i in range(stars):
        print("*", end=' ')
    print()

    # d. print n lines of increasing stars. Using the same number as above print lines of increasing stars, starting
    # at 1. E.g. if 4 was the number entered, your single loop should print
    stars2 = int(input("Please enter the number of stars you wanted"))
    for i in range(1, stars2 + 1):
        print("*" * i)


main()

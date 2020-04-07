def main():
    total = 0
    number_of_items = int(input("Please enter the number of items"))
    # Validation for the number of the item entered cannot be under 0
    while number_of_items < 0:
        print("Please enter the valid number of item")
        number_of_items = int(input("Please enter the number of items"))
    # Do this to enter the price of each item entered from the user
    for i in range(number_of_items):
        price = float(input("Please enter the price of the item:"))
        total = total + price
    # if the total of the price is more than 100 they get 10% discount
    if total > 100:
        total = total * 0.9
    print("Total price for {} items is ${:.2f}".format(number_of_items, total))


main()

from prac_06.guitar import Guitar


def main():
    guitar_list = []
    print("My Guitars")
    name = input("Name:")
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost:"))
        guitar_being_add = Guitar(name, year, cost)
        guitar_list.append(guitar_being_add)
        print(guitar_being_add, "added")
        name = input("Name:")
    print("... snip ...")
    print("These are my guitars")

    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for i, guitar in enumerate(guitar_list):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {}: {:14} ({}), worth {:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                               vintage_string))


main()

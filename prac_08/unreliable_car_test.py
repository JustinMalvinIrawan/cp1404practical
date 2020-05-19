from prac_08.unrealiable_car import UnreliableCar

def main():
    good_car = UnreliableCar("Tesla", 100, 95)
    worst_car = UnreliableCar("Junk", 100, 20)

    for i in range(1,20):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(worst_car.name, worst_car.drive(i)))


if __name__ == '__main__':
    main()
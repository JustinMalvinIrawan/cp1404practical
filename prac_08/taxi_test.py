# Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
# Drive the taxi 40km
# Print the taxi's details and the current fare
# Restart the meter (start a new fare) and then drive the car 100km
# Print the details and the current fare
from prac_08.taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    print(taxi.get_fare())
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print(taxi.get_fare())



if __name__ == '__main__':
    main()
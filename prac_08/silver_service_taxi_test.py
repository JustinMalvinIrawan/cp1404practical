from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    SilverTaxi = SilverServiceTaxi("Silver Taxi", 100, 2)
    SilverTaxi.drive(18)
    print(SilverTaxi)
    print(SilverTaxi.get_fare())


if __name__ == '__main__':
    main()
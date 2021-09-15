from unreliable_car.py import UnreliableCar


def main():

    good_car = UnreliableCar("Good car", 100, 90)
    bad_car = UnreliableCar("Bad car", 100, 9)

    good_car.drive(120)
    bad_car.drive(50)

    print(good_car)
    print(bad_car)
main()
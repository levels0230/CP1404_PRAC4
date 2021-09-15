
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi_test = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi_test.drive(18)
    print(taxi_test)
    print(taxi_test.get_fare())

main()
from car import Car
from truk import Truck


def main():
    try:
        my_car = Car("Toyota", "Corolla", 0)
        my_truck = Truck("Ford", "F-150", 1000)

        # Oprsi mobil
        try:
            my_car.drive()
            my_car.honk()
        except Exception as e:
            print("Error pada Car:", e)

        # Oprsi truk
        try:
            my_truck.drive()
            my_truck.load(1200)  # Akan memunculkan error
        except Exception as e:
            print("Error pada Truck:", e)

    except (ValueError, TypeError) as e:
        print("terjadi error!:", e)

if __name__ == "__main__":
    main()
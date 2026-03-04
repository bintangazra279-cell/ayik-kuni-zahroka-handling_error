from vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)

        # Validasi doors
        if not isinstance(doors, int):
            raise TypeError("Jumlah pintu harus berupa angka.")
        if doors <= 0:
            raise ValueError("Jumlah pintu harus lebih dari 0.")

        self.doors = doors

    def honk(self):
        print("Beep! Beep!")

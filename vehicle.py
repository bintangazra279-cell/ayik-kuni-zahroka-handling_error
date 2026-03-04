class Vehicle:
    def __init__(self, brand, model):
        if not brand or not model:
            raise ValueError("Brand dan model tidak boleh kosong.")
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")



from vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        if load_capacity <= 0:
            raise ValueError("Load capacity harus lebih dari 0.")
        self.load_capacity = load_capacity

    def load(self, weight):
        try:
            if weight > self.load_capacity:
                raise ValueError("Muatan melebihi kapasitas maksimum!")
            print(f"Loaded {weight} kg.")
        except ValueError as e:
            print("Error muatan truck melebihi kapasitas:", e)
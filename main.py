from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, mark, fuel_use, fuel_have, speed, rided_way):
        self.mark = mark
        self.fuel_use = fuel_use
        self.fuel_have = fuel_have
        self.speed = speed
        self.rided_way = rided_way

    pass

    def refuel(self):
        self.fuel_have += self.fuel_use
        if self.fuel_have > 11.4:
            self.fuel_have = 11.4

    def transfer_fuel(self, other_vehicle, amount):
        available_amount = min(amount, self.fuel_have, other_vehicle.tank_volume - other_vehicle.fuel_have)
        self.fuel_have -= available_amount
        other_vehicle.remaining_fuel += available_amount

    @abstractmethod
    def __str__(self):
        pass


class Car(Vehicle):
    def __init__(self, mark, fuel_use, fuel_have, speed, rided_way, passengers_in=4, airbag=True):
        super().__init__(mark, fuel_use, fuel_have, speed, rided_way)
        self.passengers_in = passengers_in
        self.airbag = airbag

    def __str__(self):
        return f"Car: Mark - {self.mark}, Tank volume - {self.fuel_use}, Remaining Fuel - {self.fuel_have}, speed - {self.speed}, rided_way - {self.rided_way}, passengers_count - {self.passengers_in}, Airbag_available - {self.airbag} "


class Motorbike(Vehicle):
    def __init__(self, mark, fuel_use, fuel_have, speed, rided_way, stroller=False, ):
        super().__init__(mark, fuel_use, fuel_have, speed, rided_way)
        self.stroller = stroller

    def __str__(self):
        return f"Car: Mark - {self.mark}, Tank volume - {self.fuel_use}, Remaining Fuel - {self.fuel_have}, speed - {self.speed}, rided way - {self.rided_way}, Stroller - {self.stroller} "


car = Car("Nissan", 40, 10, 100, 2000, 4, True)

motorcycle = Motorbike("harley davidson", 30, 10, 100, 400, False)

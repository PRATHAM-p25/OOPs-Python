class User:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name


class Driver(User):
    def __init__(self, car, **kwargs):
        super().__init__(**kwargs)
        self.car = car


class Rider(User):
    def __init__(self, pickup_location, **kwargs):
        super().__init__(**kwargs)
        self.pickup_location = pickup_location


class Trip(Driver, Rider):
    def __init__(self, name, car, pickup_location):
        super().__init__(
            name=name,
            car=car,
            pickup_location=pickup_location
        )

    def summary(self):
        return f'{self.name} will pick up the rider from {self.pickup_location} using {self.car}.'


t1 = Trip("Amit", "Honda City", "Sector 21")
print(t1.summary())

import random


class Vehicle:
    def __init__(self, make, model, year, weight, needs_maintenance=False, trips_since_maintenance=0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needs_maintenance = needs_maintenance
        self.trips_since_maintenance = trips_since_maintenance

    def repair(self):
        self.trips_since_maintenance = 0
        self.needs_maintenance = False


class Car(Vehicle):
    def __init__(self, make, model, year, weight, is_driving=False):
        Vehicle.__init__(self, make, model, year, weight)
        self.is_driving = is_driving

    def drive(self):
        self.is_driving = True

    def stop(self):
        if self.is_driving:
            self.trips_since_maintenance += 1
            if self.trips_since_maintenance > 100:
                self.needs_maintenance = True
            self.is_driving = False


class Plane(Vehicle):
    def __init__(self, make, model, year, weight, is_flying=False):
        Vehicle.__init__(self, make, model, year, weight)
        self.is_flying = is_flying

    def flying(self):
        self.is_flying = True

    def landing(self):
        if self.is_flying:
            self.trips_since_maintenance += 1
            if self.trips_since_maintenance > 100:
                self.needs_maintenance = True
            self.is_flying = False


def random_car_drives(car):
    drive_times = random.randint(1, 102)
    for i in range(drive_times):
        car.drive()
        car.stop()


def random_flights(plane):
    flight_times = random.randint(1, 102)
    if flight_times > 100:
        print(f"{plane.make} {plane.model} can't fly until it's repaired")
        plane.repair()
    else:
        for k in range(flight_times):
            plane.flying()
            plane.landing()


car1 = Car("Mercedez Benz", "E-Class", 2020, 4000)
car2 = Car("Audi", "A5", 2019, 3500)
car3 = Car("BMW", "Grand Coupe", 2018, 3700)


plane1 = Plane("Airbus", "A380", 2016, 575000)
plane2 = Plane("Boeing", "747", 2012, 183500)


random_car_drives(car1)
random_car_drives(car2)
random_car_drives(car3)


random_flights(plane1)
random_flights(plane2)


def print_car_specs(car):
    print("-" * 50)
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Year: {car.year}")
    print(f"Weight: {car.weight}")
    print(f"Trips Since Maintenance: {car.trips_since_maintenance}")
    print(f"Needs Maintenance: {car.needs_maintenance}")


def print_plane_specs(plane):
    print("-" * 30)
    print(f"Make: {plane.make}")
    print(f"Model: {plane.model}")
    print(f"Year: {plane.year}")
    print(f"Weight: {plane.weight}")
    print(f"Trips Since Maintenance: {plane.trips_since_maintenance}")
    print(f"Needs Maintenance: {plane.needs_maintenance}")
    if plane.trips_since_maintenance == 0:
        print("Plane currently under maintenance")


print_car_specs(car1)
print_car_specs(car2)
print_car_specs(car3)

print_plane_specs(plane1)
print_plane_specs(plane2)

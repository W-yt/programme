# 用于表示汽车的类

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        #指定默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + ' miles on it!')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        range = 0
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can run approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class EletricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
#
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(500)
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(100)
#
# my_new_car.increment_odometer(50)
# my_new_car.read_odometer()
#
# my_tesla = EletricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()




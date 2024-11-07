class Car:
    """A simple example of a class"""

    def __init__(self, color, make, model, year):
        """Initialize attributes to describe a car"""
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def get_descriptive_name(self):
        """Return a formatted descriptive name for the car"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_mileage(self):
        """Print a statement showing the car's mileage"""
        print("This car has " + str(self.mileage) + " miles on it.")

    def update_mileage(self, mileage):
        """Set the mileage to the given value"""
        self.mileage = mileage

    def increment_mileage(self, miles):
        """Add the given amount to the mileage"""
        self.mileage += miles
    @staticmethod
    def hello():
        print("hello")

        
my_new_car = Car('red', 'audi', 'a4', 2016)


print(my_new_car.get_descriptive_name())
print(my_new_car.mileage)

my_used_car = Car('silver', 'subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

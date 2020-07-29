from klasy.car.car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.descript_name())
my_tesla.descript_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.descript_battery()
my_tesla.battery.get_range()


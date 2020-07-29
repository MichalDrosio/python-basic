class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odmeter_reading = 0
        self.tank = 0

    def descript_name(self):
        return f'{self.year} {self.model.title()} {self.make.title()}'

    def read_odometer(self):
        print(f"Auto {self.make} {self.model} z {self.year} ma przejechane {self.odmeter_reading} km")

    def update_odometer(self, milage):
        if milage >= self.odmeter_reading:
            self.odmeter_reading = milage
        else:
            print('Nie można cofnąć licznika samochodu')

    def incremente_odometer(self, kilometers):
        if kilometers > 0:
            self.odmeter_reading += kilometers
        else:
            print('Nie można cofnąć licznika samochodu')

    def fill_gas_tank(self, gas):
        self.tank += gas
        return f'zatankowano {gas}L paliwa, w zbiorniku znajduje sie obecnie {self.tank}'

class Battery():
    def __init__(self, battery_size=70):
        self.batery_size = battery_size

    def description_batery(self):
        print(f'Auto ma akumulator o pojemnosci {self.batery_size}')

    def get_range(self):
        if self.batery_size == 70:
            range = 240
        elif self.batery_size == 85:
            range = 270
        message = f'Zasieg auta wynosi okolo {range} po pelnym naladowaniu'
        print(message)

    def upgrade_battery(self):
        if self.batery_size != 85:
            self.batery_size = 85




class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def descript_battery(self):
        print(f"Ten samochod {self.make} {self.model} ma akumulator o pojemnosci {self.battery.batery_size} kWh")

    def fill_gas_tank(self, gas):
        print('elektryk, bez tankowania')





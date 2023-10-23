'''Task'''
'''Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", 
наслідувані від "Транспортний засіб". Наповніть класи атрибутами та методами на свій розсуд.
Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель". Виведіть на екран значення атрибутів обʼєктів'''

class Vehicle:
    weight = None                   # масса
    power = None                    # мощность
    appointment = None              # назначение
    cost = None                     # стоимость

    def __init__(self, new_weight, new_power, new_appointment, new_cost):
        self.weight = new_weight
        self.power = new_power
        self.appointment = new_appointment
        self.cost = new_cost

        print(f"Weight: {self.weight}\n"
              f"Power: {self.power}\n"
              f"Appointment: {self.appointment}\n"
              f"Cost: {self.cost}\n")



class Cars(Vehicle):                # автомобили
    brand = None
    model = None

    def __init__(self, new_brand, new_model):
        self.brand = new_brand
        self.model = new_model

    def info_for_vehicle(self):
        print(f"Brand: {self.brand}\n"
              f"Model: {self.model}\n")



class Planes(Vehicle):              # самолёты
    passenger_capacity = None
    flight_altitude = None

    def __init__(self, new_passenger_capacity, new_flight_altitude):
          self.passenger_capacity = new_passenger_capacity
          self.flight_altitude = new_flight_altitude

    def info_for_vehicle(self):
        print(f"Passenger_capacity: {self.passenger_capacity}\n"
              f"Flight_altitude: {self.flight_altitude}\n")



class Ships(Vehicle):               # корабли
    load_capacity = None
    length = None

    def __init__(self, new_load_capacity, new_length):
        self.load_capacity = new_load_capacity
        self.length = new_length

    def info_for_vehicle(self):
        print(f"Load_capacity: {self.load_capacity}\n"
              f"Length: {self.length}\n")




toyota = Vehicle("1900 kg", "180 hp", "Lfe on the land", "9000 $")
toyota = Cars("Toyota", "Camry")
toyota.info_for_vehicle()

mazda = Vehicle("2100 kg",
                "220 hp",
                "Lfe on the land",
                "10500 $")
mazda = Cars("Mazda",
             "CX-5")
mazda.info_for_vehicle()


airbus = Vehicle("456324 kg",
                 "24634 hp",
                 "Moving through the air",
                 "34234000 $")
airbus = Planes("1000 peoples",
                "12527 m")
airbus.info_for_vehicle()


boeing = Vehicle("234652 kg",
                 "35435 hp",
                 "Moving through the air",
                 "25345500 $")
boeing = Planes("1500 peoples",
                "13500 m")
boeing.info_for_vehicle()


oceanco = Vehicle("37000 kg",
                  "4830 hp",
                  "Movement on water",
                  "30000000 $")
oceanco = Ships("20 t",
                "100 m")
oceanco.info_for_vehicle()


feadsfip = Vehicle("29000 kg",
                   "3580 hp",
                   "Movement on water",
                   "25000000 $")
feadsfip = Ships("18 t",
                "85 m")
feadsfip.info_for_vehicle()

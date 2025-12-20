class Vehicle:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self,__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if year > 1900:
            self.__year = year
        else:
            print("Invalid year")
    
    def display_info(self):
        print(f"Brand: {self.__brand}, Model: {self.__model}, Year{self.__year}")


class Car(Vehicle):
    def __init__(self, brand, model, year, doors, fuel_type):
        super().__init__(brand, model, year)
        self.__doors = doors
        self.__fuel_type = fuel_type


    def get_doors(self):
        return self.__doors
    
    def set_doors(self, doors):
        self.__doors = doors

    def get_fuel_type(self):
        return self.__fuel_type
    
    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.__doors}, Fuel Type {self.__fuel_type}")

# 10 demo Car objects
cars = [

    Car("Toyota", "Corolla", 2020, 4, "Petrol"),

    Car("Honda", "Civic", 2019, 4, "Petrol"),

    Car("Ford", "Mustang", 2021, 2, "Petrol"),

    Car("BMW", "X5", 2022, 4, "Diesel"),

    Car("Audi", "A4", 2018, 4, "Diesel"),

    Car("Mercedes", "C-Class", 2020, 4, "Petrol"),

    Car("Hyundai", "Elantra", 2021, 4, "Petrol"),

    Car("Kia", "Seltos", 2019, 4, "Diesel"),

    Car("Nissan", "Altima", 2020, 4, "Petrol"),

    Car("Volkswagen", "Passat", 2021, 4, "Diesel")
]

# Display all demo cars
print("---------------Demo Cars--------------")
for car in cars:
    car.display_info()
    print("")
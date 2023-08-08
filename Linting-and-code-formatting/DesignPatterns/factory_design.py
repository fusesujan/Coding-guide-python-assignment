# # Vehicle interface (Product)
# class Vehicle:
#     def drive(self):
#         pass

# # Concrete classes (Concrete Products)
# class Car(Vehicle):
#     def drive(self):
#         return "Driving a car"

# class Motorcycle(Vehicle):
#     def drive(self):
#         return "Riding a motorcycle"

# class Bicycle(Vehicle):
#     def drive(self):
#         return "Riding a bicycle"

# # Factory class (Creator)
# class VehicleFactory:
#     def create_vehicle(self, vehicle_type):
#         if vehicle_type == "car":
#             return Car()
#         elif vehicle_type == "motorcycle":
#             return Motorcycle()
#         elif vehicle_type == "bicycle":
#             return Bicycle()
#         else:
#             raise ValueError("Invalid vehicle type")

# # Client code
# if __name__ == "__main__":
#     factory = VehicleFactory()

#     vehicle1 = factory.create_vehicle("car")
#     print(vehicle1.drive())  

#     vehicle2 = factory.create_vehicle("motorcycle")
#     print(vehicle2.drive()) 

#     vehicle3 = factory.create_vehicle("bicycle")
#     print(vehicle3.drive()) 

    
#     try:
#         vehicle4 = factory.create_vehicle("train")
#     except ValueError as e:
#         print(e)  

import logging
import datetime

class FileLogger:
    def __init__(self) -> None:
        print("File Logging")

    def logging(self, msg):
        return logging.info(f"File Logging {msg} at {datetime.datetime.now()}")

class ConsoleLogger:
    def __init__(self) -> None:
        print("Console Logging")

    def logging(self, msg):
        return logging.warning(f"Console Logging {msg} at {datetime.datetime.now()}")

class DatabaseLogger:
    def __init__(self) -> None:
        print("Database Logging")

    def logging(self, msg):
        return logging.info(f"Database Logging {msg} at {datetime.datetime.now()}")
    
def FactoryLogger(logger_type: str):
    """Factory Method"""

    loggers = {
        "File": FileLogger,
        "Console": ConsoleLogger,
        "Database": DatabaseLogger
    }
    return loggers[logger_type]()


logging.basicConfig(level=logging.INFO)

message = "secret"
file = FactoryLogger("File")
# console_abc = FactoryLogger("Console")
# database = FactoryLogger("Database")

file.logging(message)
# console_abc.logging(message)
# database.logging(message)
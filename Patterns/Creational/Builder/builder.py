"""
Builder Design Pattern
"""
from abc import ABCMeta, abstractmethod

class Vehicle():
    def __init__(self):
        self.__name      = ''
        self.__bodyType  = ''
        self.__engine    = ''
        self.__fuelType  = ''
        self.__wheels    = 0
        self.__wheelSize = 0

    def setName(self, name):
        ''' set vehicle name '''
        self.__name = name

    def setBodyType(self, bodyType):
        ''' set bodyType '''
        self.__bodyType = bodyType

    def setEngine(self, engine):
        ''' set engine '''
        self.__engine = engine

    def setFuelType(self, fuelType):
        ''' set fuelType '''
        self.__fuelType = fuelType

    def setWheels(self, wheels):
        ''' set wheels '''
        self.__wheels = wheels

    def setWheelSize(self, wheelSize):
        ''' set wheel size '''
        self.__wheelSize = wheelSize

    def __str__(self):
        return f'** Vehicle Specs ** \nName: {self.__name} \nBody Type: {self.__bodyType} \nEngine: {self.__engine} \
            \nFule Type: {self.__fuelType} \nWheels: {self.__wheels} \nWheel Size: {self.__wheelSize}'

class VehicleBuilder( metaclass = ABCMeta ):
    def getVehicle(self):
        ''' returns vehicle '''
        return self.vehicle

    @abstractmethod
    def buildBody(self):
        ''' builds vehicle name and body type '''
        
    @abstractmethod
    def buildEngine(self):
        ''' builds vehicle engine and fuel type '''

    @abstractmethod
    def buildWheels(self):
        ''' builds vehicle wheels '''

class CarBuilder(VehicleBuilder):
    def __init__(self):
        self.vehicle = Vehicle()

    def buildBody(self):
        ''' builds vehicle name and body type '''
        self.vehicle.setName('Car')
        self.vehicle.setBodyType('Hatchback')

    def buildEngine(self):
        ''' builds vehicle engine and fuel type '''
        self.vehicle.setEngine('1000 cc')
        self.vehicle.setFuelType('Diesel')

    def buildWheels(self):
        ''' builds vehicle wheels '''
        self.vehicle.setWheels(4)
        self.vehicle.setWheelSize(16)

class BikeBuilder(VehicleBuilder):
    def __init__(self):
        self.vehicle = Vehicle()

    def buildBody(self):
        ''' builds vehicle name and body type '''
        self.vehicle.setName('Bike')
        self.vehicle.setBodyType('ATV')

    def buildEngine(self):
        ''' builds vehicle engine and fuel type '''
        self.vehicle.setEngine('200 cc')
        self.vehicle.setFuelType('Petrol')

    def buildWheels(self):
        ''' builds vehicle wheels '''
        self.vehicle.setWheels(2)
        self.vehicle.setWheelSize(24)
        
class Supervisor():
    def __init__(self, vehicleBuilder):
        self.vehicleBuilder = vehicleBuilder

    def makeVehicle(self):
        ''' builds vehicle '''
        self.vehicleBuilder.buildBody()
        self.vehicleBuilder.buildEngine()
        self.vehicleBuilder.buildWheels()

        return self.vehicleBuilder.getVehicle()

if __name__ == '__main__':
    # Build Car
    builders = [CarBuilder(), BikeBuilder()]

    for builder in builders:
        supervisor = Supervisor(builder)
        print(supervisor.makeVehicle())
        print('')
        
# Output
# ** Vehicle Specs ** 
# Name: Car 
# Body Type: Hatchback 
# Engine: 1000 cc             
# Fule Type: Diesel 
# Wheels: 4 
# Wheel Size: 16

# ** Vehicle Specs ** 
# Name: Bike 
# Body Type: ATV 
# Engine: 200 cc             
# Fule Type: Petrol 
# Wheels: 2 
# Wheel Size: 24

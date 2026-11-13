
# Car class
class Car:
    def move(self):
        print("The car drives on the road.")


# Boat class
class Boat:
    def move(self):
        print("The boat sails on water.")          #Each Class here is independent of each other, yet all use the same method of 'move'


# Drone class
class Drone:
    def move(self):
        print("The drone flies in the sky.")


# Function that calls the move() method, which means that each class will have a seperate output. 
# This function does not care whether if each class are different, as long as it has the method of 'move' then it is a vehicle
# Which perfectly fits Duck-Typing: "If it can quack and fly, then it is a duck." Since they ignore the class and identify its function
def start_trip(vehicle):
    vehicle.move() #This function specifically requires the move function from the classes, which all have, therefore all are vehicles


# This Create objects, class to variable/object for them to be used with the function below
car1 = Car()
boat1 = Boat()
drone1 = Drone()


# This call's the start_trip() for each object
start_trip(car1)
start_trip(boat1)
start_trip(drone1)                                #He is talking about us.

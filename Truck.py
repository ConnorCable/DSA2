class Truck:
    def __init__(self, location, speed, miles, depatureTime, packages):
        self.location = location
        self.miles = miles
        self.departureTime = depatureTime
        self.packages = packages
        self.speed = speed
        self.currentTime = depatureTime

    def __str__(self):
        return f"location : {self.location}, miles: {self.miles}, departure time: {self.departureTime}, current Time: {self.currentTime} packages: {self.packages}"

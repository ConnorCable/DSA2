class Package:
    def __init__(self, id, address, city,  state, zipcode, deadline, weight):
        self.departure_time = None
        self.delivery_time = None
        self.id = id
        self.address = address
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.deliveryStatus = "At WGUPS Hub"

    def __str__(self) -> str:
        return f"id: {self.id}, address: {self.address}, city: {self.city},  state: {self.state}, zipcode: {self.zipcode}, deadline: {self.deadline}, weight: {self.weight}" 
    
    def returnStatus(self, time):
        if time < self.deadline:
            self.status = "Delivered"
        elif self.departure_time > time:
            self.status = "Delivering"
        else:
            self.status = "At WGUPS Hub"
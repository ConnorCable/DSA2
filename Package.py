class Package:
    def __init__(self, id, address, city,  state, zipcode, deadline, weight , notes ):
        self.departure_time = None
        self.delivery_time = None
        self.id = id
        self.address = address
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.deliveryStatus = " | \033[94m" + "At WGUPS Hub" + "\033[0m"
        self.notes = notes

    def __str__(self) -> str:
        return f"ID: {self.id}, address: {self.address}, city: {self.city}, state: {self.state}, zipcode: {self.zipcode}, deadline: {self.deadline}, weight: {self.weight}, departed: {self.departure_time}, delivered: {self.delivery_time} {self.deliveryStatus}  "
    


    def reportStatus(self,time):
        if time >= self.delivery_time:
            self.deliveryStatus = " | \033[92m" + "Delivered" + "\033[0m"
        elif time >= self.departure_time:
            self.deliveryStatus = " | \033[93m" + "En Route" + "\033[0m"
import datetime
class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, notes):
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
        self.deadStatus = ""

    def __str__(self) -> str:
        return f"ID: {self.id}, address: {self.address}, city: {self.city}, state: {self.state}, zipcode: {self.zipcode}, deadline: {self.deadline}, weight: {self.weight}, departed: {self.departure_time}, delivered: {self.delivery_time} {self.deliveryStatus}{self.deadStatus}"

    def returnString(self):
        if "At WGUPS Hub" in self.deliveryStatus:
            print( f"ID: {self.id}, address: {self.address}, city: {self.city}, state: {self.state}, zipcode: {self.zipcode}, deadline: {self.deadline}, weight: {self.weight}, {self.deliveryStatus}{self.deadStatus}")
        if "Delivered" in self.deliveryStatus:
            print( f"ID: {self.id}, address: {self.address}, city: {self.city}, state: {self.state}, zipcode: {self.zipcode}, deadline: {self.deadline}, weight: {self.weight}, departed: {self.departure_time}, delivered: {self.delivery_time} {self.deliveryStatus}{self.deadStatus}")
        if "En Route" in self.deliveryStatus:
            print( f"ID: {self.id}, address: {self.address}, city: {self.city}, state: {self.state}, zipcode: {self.zipcode}, deadline: {self.deadline}, weight: {self.weight}, departed: {self.departure_time},{self.deliveryStatus}{self.deadStatus}")


    # This is O(1) for a simple comparison of datetime objects
    def reportStatus(self, time):
        if time >= self.delivery_time:
            self.deliveryStatus = " | \033[92m" + "Delivered " + "\033[0m"
            if self.deadline != "EOD":
                self.deadlineStatus()
        elif time >= self.departure_time:
            self.deliveryStatus = " | \033[93m" + "En Route" + "\033[0m |"

    # This is O(1) for a simple comparison of datetime objects
    def deadlineStatus(self):
        hours, minutes = map(int, self.deadline.split(":"))
        deadline = datetime.timedelta(hours=hours, minutes=minutes)
        if self.delivery_time > deadline:
            self.deadStatus = "\033[91mLate\033[0m" + " ID : " + str(self.id)
        else:
            self.deadStatus = "\033[92m" + "Within Deadline" + "\033[0m"




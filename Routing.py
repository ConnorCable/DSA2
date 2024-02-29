import datetime


# This class handles all routing needs, including getting distances, address id's, delivering packages
# and providing information on packages as requested by the user interface
class Routing:

    def __init__(self, distance_table, address_table, hash_table):
        self.distance_table = distance_table
        self.address_table = address_table
        self.hash_table = hash_table

    # O(n) runtime for iterating through a list ( the address table)
    # gets address id from address string
    def getAddress(self, addy):
        for item in self.address_table:
            if addy in item[2]:
                return int(item[0])

    # gets the distance between two address id's
    # O(1) runtime, as dictionary / list lookups are both O(1)
    def getDistance(self, beginning, ending):
        distance = self.distance_table[beginning][ending]
        if distance == "":
            distance = self.distance_table[ending][beginning]
        return float(distance)

    # This algorithm is O(n*m) where n is the number of packages in the truck and m is the amount remaining once one is selected
    def deliverPackages(self, truck):
        to_deliver = []
        priority_to_deliver = []
        # Load the packages from the truck into the algorithm

        for package_id in truck.packages:
            package = self.hash_table.search(package_id)
            # Set the packages departure time to when the truck leaves the hub
            if "EOD" not in package.deadline:
                priority_to_deliver.append(package)
            else:
                to_deliver.append(package)
            package.departure_time = truck.departureTime
        while len(priority_to_deliver) != 0:
            priority_distance = 0
            next_priority_distance = 9999
            next_priority_package = None
            for package in priority_to_deliver:
                priority_current_address = self.getAddress(truck.location)
                # get the package's address number
                priority_package_address = self.getAddress(package.address)
                # get the distance between the truck and the package in question
                priority_distance = self.getDistance(priority_current_address, priority_package_address)
                if priority_distance <= next_priority_distance:
                    next_priority_package = package
            truck.location = next_priority_package.address
            truck.miles += priority_distance
            truck.currentTime += datetime.timedelta(hours=priority_distance / truck.speed)
            # update the packages delivery time
            next_priority_package.delivery_time = truck.currentTime
            priority_to_deliver.remove(next_priority_package)

        while len(to_deliver) != 0:
            # initialize distance between node variable, smallest ( next chosen) distance, and next package
            distance_between = 0
            next_distance = 9999
            next_package = None
            for package in to_deliver:
                # get the truck's address number
                current_address = self.getAddress(truck.location)
                # get the package's address number
                package_address = self.getAddress(package.address)
                # get the distance between the truck and the package in question
                distance_between = self.getDistance(current_address, package_address)

                if distance_between <= next_distance:
                    next_package = package
            # update trucks mileage, address, and current time

            truck.location = next_package.address
            truck.miles += distance_between
            truck.currentTime += datetime.timedelta(hours=distance_between / truck.speed)
            # update the packages delivery time
            next_package.delivery_time = truck.currentTime
            to_deliver.remove(next_package)
    # Delivers packages without prioritization related to deadline O(n * m)
    def deliverPackages_no_priority(self, truck):
        to_deliver = []
        # Load the packages from the truck into the algorithm

        for package_id in truck.packages:
            package = self.hash_table.search(package_id)
            # Set the packages departure time to when the truck leaves the hub

            to_deliver.append(package)
            package.departure_time = truck.departureTime

        while len(to_deliver) != 0:
            # initialize distance between node variable, smallest ( next chosen) distance, and next package
            distance_between = 0
            next_distance = 9999
            next_package = None
            for package in to_deliver:
                # get the truck's address number
                current_address = self.getAddress(truck.location)
                # get the package's address number
                package_address = self.getAddress(package.address)
                # get the distance between the truck and the package in question
                distance_between = self.getDistance(current_address, package_address)
                if distance_between <= next_distance:
                    next_package = package
            # update trucks mileage, address, and current time

            truck.location = next_package.address
            truck.miles += distance_between
            truck.currentTime += datetime.timedelta(hours=distance_between / truck.speed)
            # update the packages delivery time
            next_package.delivery_time = truck.currentTime
            to_deliver.remove(next_package)

    # This algorithm is O(1) as the hash table lookup is O(1)
    def getSinglePackage(self, package_id, time):
        selection = self.hash_table.search(package_id)
        selection.reportStatus(time)
        return selection

    # This algorithm is O(40 * 1) as it only needs to iterate 40 times, but would be O(n)
    # if the hash table continued to expand
    # hash lookup is O(1)
    def getAllPackages(self, time):
        collection = []
        for i in range(1, 41):
            package = self.hash_table.search(i)
            package.reportStatus(time)
            collection.append(package)
        return collection

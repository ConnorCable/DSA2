import csv
import datetime
from hashtable import HashTable
from Package import Package
from Truck import Truck
# load address data
with open("CSV/Address_File.csv") as addressCSV:
    addresses = csv.reader(addressCSV)
    addresses = list(addresses)

with open("CSV/Distance_File.csv") as distanceCSV:
    distances = csv.reader(distanceCSV)
    distances = list(distances)

with open("CSV/Package_File.csv") as packageCSV:
    packages = csv.reader(packageCSV)
    packages = list(packages)


package_hash = HashTable()

def packages_to_hash(table, packages):
        for package in packages:
            Id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            package_zip = package[4]
            deadline = package[5]
            weight = package[6]
            status = "At WGUPS Hub"

            item = Package(Id, address, city, state, package_zip, deadline, weight, status)

            table.insert(Id, item)

packages_to_hash(package_hash, packages_to_hash)

# gets address id from address string
def getAddress(addy, table):
    for item in table:
        if item in table[2]:
            return int(item[0])
    


def getDistance(location_x,location_y):
    distance = distances[location_x][location_y]
    if distance == '':
        distance = distances[location_y][location_x]
    return distance


# location, speed,  miles, depatureTime,  packages

truck1 = Truck("4001 South 700 East", 18, 0, datetime.timedelta(hours=8), [1,2,4,5,7,8,10,11,13,15,17,19,21,22,23,24])
truck2 = Truck("4001 South 700 East", 18, 0, None, [3,9,18,36,38])



def deliverPackages(truck,hash):
    toDeliver = []

    for id in truck.packages:
        package = hash.search(id)
        toDeliver.append(package)

    

    while len(toDeliver) != 0:
        currentAddress = getAddress(truck.location)
        nextAddress = 999
        for package in toDeliver:
            packageAddress = getAddress(package.address)
            if ge




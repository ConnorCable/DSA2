import csv
import datetime
from hashtable import HashTable
from Package import Package
from Truck import Truck
from Routing import Routing

# load address data into a list
with open("CSV/Addresses.csv") as addressCSV:
    addresses = csv.reader(addressCSV)
    addresses = list(addresses)

# load distances and put them into a dictionary
with open("CSV/Distances.csv") as distanceCSV:
    distances = csv.reader(distanceCSV)
    distance_hash = {}
    i = 0
    for entry in list(distances):
        distance_hash[i] = entry
        i += 1
# load package data, later to be put into a chaining hash table
with open("CSV/Packages.csv") as packageCSV:
    packages = csv.reader(packageCSV)
    packages = list(packages)

# instantiate hash table
package_hash = HashTable()


# O(n) runtime complexity, based on the number of packages needing to be inserted into the hash
def packages_to_hash(table, package_list):
    for package in package_list:
        package_id = int(package[0])
        address = package[1]
        city = package[2]
        state = package[3]
        package_zip = package[4]
        deadline = package[5]
        weight = package[6]
        notes = package[7]

        item = Package(package_id, address, city, state, package_zip, deadline, weight, notes)

        table.insert(package_id, item)


packages_to_hash(package_hash, packages)

# location, speed,  miles, depatureTime,  packages
# instantiate the trucks, with their packages loaded
truck_1 = Truck("4001 South 700 East", 18, 0, datetime.timedelta(hours=8),
                [20,3,
                 29, 15, 40, 31, 14, 34, 16, 37, 13, 1, 30, ])
# Truck with packages that have specific requirements ( including package 9, which has its address fixed at exactly 10:20)
truck_2 = Truck("4001 South 700 East", 18, 0, datetime.timedelta(hours=10, minutes=20),
                [9, 5, 12, 17, 21, 19, 18, 22, 23, 24, 26, 27, 35, 36, 38, 39])
# Truck with late packages arriving at 9:05
truck_3 = Truck("4001 South 700 East", 18, 0, datetime.timedelta(hours=9, minutes=5),
                [2, 4, 6, 7, 8, 3, 10, 11, 25, 28, 33, 32])

router = Routing(distance_hash, addresses, package_hash)

router.deliverPackages(truck_1)
router.deliverPackages(truck_2)
router.deliverPackages(truck_3)

# User interface, takes 3 different options for selections
while True:
    selection = input("Please enter 1 to view a single package, 2 to view all, 3 to view truck mileage ")
    if selection not in ["1", "2", "3"]:
        print("Invalid selection")
        continue
    if selection == "3":
        print("truck 1 miles: " + str(truck_1.miles))
        print("truck 2 miles: " + str(truck_2.miles))
        print("truck 3 miles: " + str(truck_3.miles))
        print("combined miles : " + str(truck_1.miles + truck_2.miles + truck_3.miles))
        continue
    time = input("Please enter a time you'd like to see the package(s) at. Format: HH:MM ")
    try:
        (hours, minutes) = time.split(":")
    except ValueError:
        continue
    time = datetime.timedelta(hours=int(hours), minutes=int(minutes))
    match selection:
        case "1":
            id = int(input("Please enter a package ID: "))
            print(str(router.getSinglePackage(id,time)) + "at " + str(time) + " |")
        case "2":
            for package in router.getAllPackages(time):
                print(str(package) + "at " + str(time) + " |")


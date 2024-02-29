# WGU Data Structures and Algorithms 2 C950
# Connor Cable
# Student ID: 011447975


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
    for p in package_list:
        package_id = int(p[0])
        address = p[1]
        city = p[2]
        state = p[3]
        package_zip = p[4]
        deadline = p[5]
        weight = p[6]
        notes = p[7]

        item = Package(package_id, address, city, state, package_zip, deadline, weight, notes)

        table.insert(package_id, item)

# load the package list into the hash table
packages_to_hash(package_hash, packages)

# location, speed,  miles, depatureTime,  packages
# instantiate the trucks, with their packages loaded
truck_1 = Truck("4001 South 700 East", 18, 0, datetime.timedelta(hours=8),
                [16, 34, 37, 40, 19, 13, 1, 20, 14, 15, 10, 11])
truck_2 = Truck("4001 South 700 East", 18, 0, datetime.timedelta(hours=8),
                [6, 18, 25, 27, 33, 35, 36, 38, 39, 30, 31, 29, ])

# load the relevant tables into a Routing object
router = Routing(distance_hash, addresses, package_hash)

# deliver packages for truck 1 and 2
router.deliverPackages(truck_1)
router.deliverPackages(truck_2)
# route the first truck back to the hub so that they can drive the third truck
truck_1.miles += router.getDistance(0, router.getAddress(truck_1.location))
truck_1.location = "4001 South 700 East"
truck_1.currentTime += datetime.timedelta(
    hours=router.getDistance(0, router.getAddress(truck_1.location)) / truck_1.speed)
# put all the EOD package on truck 3 + some others , truck 3 starts when truck 1 reaches the hub
truck_3 = Truck("4001 South 700 East", 18, 0, truck_1.currentTime,
                [3, 2, 4, 5, 7, 8, 9, 12, 17, 21, 22, 23, 24, 26, 28, 32, ])
router.deliverPackages(truck_3)

# User interface, takes 3 different options for selections
while True:
    selection = input("Please enter 1 to view a single package, 2 to view all, 3 to view truck mileage ")
    if selection not in ["1", "2", "3"]:
        print("Invalid selection")
        continue
    # print the truck miles
    if selection == "3":
        print("truck 1 miles: " + str(truck_1.miles))
        print("truck 2 miles: " + str(truck_2.miles))
        print("truck 3 miles: " + str(truck_3.miles))
        print("combined miles : " + str(truck_1.miles + truck_2.miles + truck_3.miles))
        continue
    # get the time of interest for the packages
    time = input("Please enter a time you'd like to see the package(s) at. Format: HH:MM ")
    try:
        (hours, minutes) = time.split(":")
    except ValueError:
        continue
    time = datetime.timedelta(hours=int(hours), minutes=int(minutes))
    match selection:
        # get one package O(1)
        case "1":
            id = int(input("Please enter a package ID: "))
            print(str(router.getSinglePackage(id, time)))
        # get all packages O(n)
        case "2":
            for package in router.getAllPackages(time):
                print(str(package))

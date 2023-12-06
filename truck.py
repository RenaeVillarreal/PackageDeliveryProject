import datetime  # Imports modules
import package
from hashtable import ChainingHashTable
import csv

# Manually loaded the "Trucks" this order meets all deadlines and special notes
packageOne = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
packageTwo = [3, 6, 18, 25, 27, 28, 32, 33, 35, 36, 38, 39]
packageThree = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26]


# Shows the start time for each truck only two trucks can be out at a time. Purpose for different times
startTimeTruck1 = datetime.datetime(2023, 10, 5, 8, 0)
startTimeTruck2 = datetime.datetime(2023, 10, 5, 9, 10)
startTimeTruck3 = datetime.datetime(2023, 10, 5, 10, 30)

# Reads the distance matrix from the 'csv/distance.csv' for distance filled in empty side of csv to read both directions
numpy = []
with open('csv/distance.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        numpy.append(row)
# Reads the addresses from the 'csv/address.csv' file
addressList = list(csv.reader(open('csv/address.csv')))

# Extracts the address inventory from the address file
addressInventory = []
for address in range(len(addressList)):
    addressInventory.append(addressList[address][1])


# Truck class with nearest neighbor algo. Chooses the closest next address from the address matrix looping through
# all addresses until all packages have been delivered/removed.
class Trucks:
    def __init__(self, start_time, truck_number, hash_table):  # Initializes the trucks with attributes
        # print("Initializing Truck")  # Checks if the three trucks have been initialized
        self.mileage = 0
        self.currentAddress = "4001 South 700 East"  # Starts a Wgu Hub
        self.packages = []
        self.time = start_time
        self.deliveryLog = []
        self.truckNumber = truck_number
        self.hash_table = hash_table
        # print("Truck Initialized")  # Checks if the three trucks have been initialized

    # Delivers all packages after execution loops through steps until no more packages remain
    # Also tracks distance back to hub after each truck has been delivered and adds it to the distance without trucks
    # Returning packages deliver at 105 miles with trucks returning 126
    # Prints the delivery logs of each truck at the end of the day with total mileage using the insert funtion and
    # search functions to correctly display package data.

    def loopPackages(self):  # Deliver all packages on the trucks

        # Commented out block shows which packages the trucks are entering the loop with
        """print("Entering loop")
        print("Current packages:", self.packages)"""
        while self.packages:
            #  print("Inside loop, packages:", self.packages)  # Prints which packages are inside loop
            self.nearestNeighbor()
            #  self.checkPackageStatus()  # used to check packages in def checkPackageStatus

        # Commented out block shows the loop exiting and no packages left on trucks
        '''print("Exiting loop")  
        print("Final packages:", self.packages)
        print("Truck", self.truckNumber, "Packages:", [packages.package_id for packages in self.packages])'''

        # Commented out block shows which packages have not been set with Nearest_Neighbor_Status in package.py
    '''def checkPackageStatus(self):  
        for packages in self.packages:
            status = packages.Nearest_Neighbor_Status(self.time)
            delivery_time = packages.delivery_time.strftime("%H:%M") if packages.delivery_time else ""
            print(f"Package {packages.package_id} - Status: {status}, Delivery Time: {delivery_time}")
            self.hash_table.updateStatus(packages.hash_key, status)
            self.hash_table.updateDeliveryTime(packages.hash_key, delivery_time)'''

    def calculateDistanceToHub(self):  # Calculates the distance to return to the hub
        returnToHub = float(numpy[addressInventory.index(self.currentAddress)]
                            [addressInventory.index("4001 South 700 East")])
        self.mileage += returnToHub

    def printDeliveryLog(self):  # Print the delivery log for the three trucks
        for entry in self.deliveryLog:
            print(
                f"Package {entry['package_id']} ({entry['status']}) Address: {entry['address']} City: {entry['city']},"
                f" State: {entry['state']} ZIP Code: {entry['zip_code']} Deadline: {entry['deadline']},"
                f" Weight: {entry['weight']} Notes: {entry['notes']} Delivery Time: {entry['delivery_time']}")

    def set_start_time(self, start_time):
        self.time = start_time

    def truckTime(self, hours, minutes):  # Adds the time of so each package can be tracked with delivery_time
        self.time += datetime.timedelta(hours=hours, minutes=minutes)

    # Main algo finds the nearest Address, repeats until no more packages are left
    # Chooses starting point "Hub", then proceeds to select the closest location
    # Marks this current location as visited, selects this node as the current location
    # Repeats until all locations have been visited returns back to "Hub"
    def nearestNeighbor(self):
        # Commented out block shows entering algorithm loop with current truck packages
        """print("Entering NearestNeighbor")
        print("Current packages: ", self.packages)"""
        nextDistance = float('inf')  # Set to positive infinity to ensure the first distance is always smaller
        currentAddress = self.currentAddress
        nextLocation = ''
        deliveryID = 0
        closestPackage = None

        if self.packages:
            packages = self.packages[0]  # Gets the first package on the truck
            if self.truckNumber == 1:
                truckDepartTime = startTimeTruck1  # checks to see what truck the package is on
            elif self.truckNumber == 2:
                truckDepartTime = startTimeTruck2
            elif self.truckNumber == 3:
                truckDepartTime = startTimeTruck3
            else:
                # Handle cases for other trucks if needed such as wrong input
                truckDepartTime = None
            packages.set_depart_time(truckDepartTime)

        for packages in self.packages:  # Calculates the distance to each package "meat of the algo"
            distance = float(numpy[addressInventory.index(currentAddress)][addressInventory.index(packages.address)])
            if distance < nextDistance:
                nextDistance = distance
                nextLocation = packages.address
                deliveryID = packages.package_id
                closestPackage = packages

        if closestPackage is not None:  # Sets the delivery and departure times for the closest package
            closestPackage.set_delivery_time(self.time)
            # Commented out block shows Algorithm delivering packages
            '''print(f"Found closest package: {closestPackage.package_id}")  
            print(f"Departure Time: {closestPackage.depart_time}, Delivery Time: {closestPackage.delivery_time}")
            print(f"Package {closestPackage.package_id} - Departure Time: {closestPackage.depart_time}, "
                  f"Delivery Time: {closestPackage.delivery_time}")'''
            # Update status and delivery time in the hashtable
            self.hash_table.updateStatus(deliveryID, 'Delivered')
            self.hash_table.updateDeliveryTime(deliveryID, self.time)

            # Remove the delivered package from the list of packages on the truck
            for packages in self.packages:
                if packages.package_id == deliveryID:
                    self.deliveryLog.append(
                        ({'package_id': deliveryID, 'address': packages.address, 'city': packages.city,
                          'state': packages.state, 'zip_code': packages.zip_code,
                          'deadline': packages.deadline, 'weight': packages.weight, 'notes': packages.notes,
                          'status': 'Delivered', 'delivery_time': self.time.strftime("%H:%M"), }))
            self.packages.remove(closestPackage)
        else:
            print("No packages found in the truck.")

        timeAdded = (nextDistance / 18) * 60  # Every second that passed one-minute passes in the program
        hours = timeAdded // 60
        minutes = timeAdded % 60
        self.truckTime(hours, minutes)
        self.currentAddress = nextLocation
        self.mileage += nextDistance

        # Shows loop being exited
        # print("Exiting nearestNeighbor")

# Renae Villarreal StudentID: 010964462
from datetime import datetime as dt  # import modules
# import datetime
from truck import Trucks, packageOne, packageTwo, packageThree, startTimeTruck1, startTimeTruck2, startTimeTruck3
from addpackages import loadPackages


class PackageStatus:
    def __init__(self, package_data, hash_table):
        self.package_data = package_data
        self.hash_table = hash_table

    @staticmethod
    def calculate_status(user_time, package):
        user_time = dt.strptime(user_time, '%H:%M').time()
        depart_time = package.depart_time.time() if package.depart_time else None
        delivery_time = package.delivery_time.time() if package.delivery_time else None

        if depart_time is None:
            return "Departure time not set"

        if user_time < depart_time:
            return "At Hub"
        elif user_time > delivery_time:
            return "Delivered"
        elif depart_time <= user_time <= delivery_time:
            return "En Route"
        return ""

    def add_deliveryTime(self, user_time, package):  # Adds delivery time next to deadline if already delivered
        status = self.calculate_status(user_time, package)
        delivery_time = package.delivery_time.strftime("%H:%M") if package.delivery_time else ""
        delivered_time_label = "Delivered At: "
        deadline_field = (
            f"{package.deadline} - ({delivered_time_label}{delivery_time})"
            if status == "Delivered" else package.deadline
        )

        return {
            "package_id": package.package_id,
            "status": status,
            "address": package.address,
            "city": package.city,
            "state": package.state,
            "zip_code": package.zip_code,
            "deadline": deadline_field,
            "weight": package.weight,
            "notes": package.notes,
        }

    def updates_package_info(self, user_time):  # Adds truck number for option 2 and 3 and updates info on package 9
        package_statuses = []
        for package_id in range(1, 41):  # package IDs go from 1 to 40
            package = self.hash_table.lookup(str(package_id))
            if package:
                truck_number = 0

                if package_id in packageOne:  # Truck 1 assigns truck number
                    truck_number = 1
                elif package_id in packageTwo:  # Truck 2 assigns truck number
                    truck_number = 2
                elif package_id in packageThree:  # Truck 3 assigns truck number
                    truck_number = 3

                if package_id == 9 and user_time >= "10:20":
                    package.address = "410 S State St"
                    package.city = "Salt Lake City"
                    package.state = "UT"
                    package.zip_code = "84111"
                elif package_id == 9 and user_time < "10:20":
                    package.address = "300 State St"
                    package.city = "Salt Lake City"
                    package.state = "UT"
                    package.zip_code = "84103"

                updated_package_info = self.add_deliveryTime(user_time, package)
                updated_package_info["truck_number"] = truck_number
                package_statuses.append(updated_package_info)

        return package_statuses


def main():
    hash_table = loadPackages()

    status_calculator = PackageStatus(hash_table.table, hash_table)

    # Test for visualizing which packages are in which buckets
    '''print("Contents of the Hashtable:")  
    for index, bucket in enumerate(hash_table.table):
        print(f"Bucket {index}:", bucket)'''

    truck1 = Trucks(startTimeTruck1, 1, hash_table)
    truck2 = Trucks(startTimeTruck2, 2, hash_table)
    truck3 = Trucks(startTimeTruck3, 3, hash_table)

    loadPackagesOntoTruck(truck1, packageOne, hash_table, startTimeTruck1)
    loadPackagesOntoTruck(truck2, packageTwo, hash_table, startTimeTruck2)
    loadPackagesOntoTruck(truck3, packageThree, hash_table, startTimeTruck3)

    truck1.loopPackages()
    truck2.loopPackages()
    truck3.loopPackages()

    # Commented out block is a Test for status Calculation
    '''user_time_input = input("Enter the current time (HH:MM Military Time): ")  
    package_statuses = status_calculator.updates_package_info(user_time_input)'''

    # Commented out block is a test with commented out block above user_time_input
    '''for package in package_statuses:
        print(
            f"Package: {package['package_id']:<4} Status: {package['status']:<10}"
            f" Address: {package['address']:<38} City: {package['city']:<16} State: {package['state']:<3}"
            f" ZipCode: {package['zip_code']:<4} Deadline: {package['deadline']:<33}"
            f" Weight: {package['weight']:<4} Notes: {package['notes']} Truck: {package['truck_number']}")

    package_ids_to_check = [1, 2, 3]

    print("Package IDs to Check:", package_ids_to_check)

    for package_id in package_ids_to_check:
        package = hash_table.lookup(str(package_id))
        if package:
            print(f"Package {package_id} - Status: {package.calculate_status(datetime.datetime.now())}, "
                  f"Delivery Time: {package.delivery_time}")
        else:
            print(f"Package {package_id} not found in the hash table.")'''

    truck1.calculateDistanceToHub()
    truck2.calculateDistanceToHub()
    truck3.calculateDistanceToHub()

    while True:
        print("\nWelcome to WGUs Package Delivery Simulator Main Menu")
        print("1. Show Which Packages are on each Truck, Delivery Logs, and Delivery Times/"
              " With Total Mileage For Each Truck/Final Total Mileage")
        print("2. Enter A Time in (HH:MM MilitaryTime) Format and List All Package Info")
        print("3. Enter A Time in (HH:MM MilitaryTime) Format with Package ID to View ONE Packages Info")
        print("0. Exit")

        choice = input("Enter your choice here --> : ")

        if choice == "1":
            print('Truck 1 Delivery Log:')
            truck1.printDeliveryLog()
            print(f'Total Mileage for Truck 1: {round(truck1.mileage, 1)}')

            print('Truck 2 Delivery Log:')
            truck2.printDeliveryLog()
            print(f'Total Mileage for Truck 2: {round(truck2.mileage, 1)}')

            print('Truck 3 Delivery Log:')
            truck3.printDeliveryLog()
            print(f'Total Mileage for Truck 3: {round(truck3.mileage, 1)}')

            total_mileage = round(truck1.mileage + truck2.mileage + truck3.mileage, 1)
            print(f'Final Total Mileage For All Trucks: {total_mileage}')

        elif choice == "2":
            user_time_input = input("Enter a specific time (HH:MM)Military Time: ")
            package_statuses = status_calculator.updates_package_info(user_time_input)
            total_mileage = round(truck1.mileage + truck2.mileage + truck3.mileage, 1)
            print(f'Total Mileage of route: {total_mileage}')
            print(f"Package Status at {user_time_input}")
            print("Package Status Table:")
            for package in package_statuses:
                print(
                    f"Package: {package['package_id']:<4} Status: {package['status']:<10}"
                    f" Address: {package['address']:<38} City: {package['city']:<16} State: {package['state']:<3}"
                    f" ZipCode: {package['zip_code']:<4} Deadline: {package['deadline']:<33}"
                    f" Weight: {package['weight']:<4} Notes: {package['notes']} Truck: {package['truck_number']}")

        elif choice == "3":
            user_time_input = input("Enter a specific time (HH:MM) Military Time: ")
            package_id = input("Enter the Package ID you want to view: ")
            package_statuses = status_calculator.updates_package_info(user_time_input)
            found = False
            for package in package_statuses:
                if str(package["package_id"]) == package_id:
                    print(f"Package Status at {user_time_input}")
                    print(
                        f"Package {package['package_id']} Status: {package['status']} Address: {package['address']}"
                        f" City: {package['city']} State: {package['state']} ZIP Code: {package['zip_code']}"
                        f" Deadline: {package['deadline']} Weight: {package['weight']} Notes: {package['notes']}"
                        f" Truck: {package['truck_number']}")
                    found = True
                    break
            if not found:
                print(f"Package with ID {package_id} not found.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please enter a valid option.")

    print("Goodbye")


def loadPackagesOntoTruck(truck, delivery_list, hash_table, start_time):  # Loads packages onto each truck
    delivery_ids = set(delivery_list)
    all_packages = [package for bucket in hash_table.table for _, package in bucket]
    truck.packages = [package for package in all_packages if int(package.package_id) in delivery_ids]
    for package in truck.packages:
        package.set_depart_time(start_time)


if __name__ == "__main__":
    main()

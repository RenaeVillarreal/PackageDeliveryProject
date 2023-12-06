from hashtable import ChainingHashTable
from package import Package
import csv


def loadPackages():  # Loads packages from csv file
    package_hash_table = ChainingHashTable()

    package_csv_file_path = "csv/packages.csv"
    with open(package_csv_file_path, mode="r") as package_file:
        package_reader = csv.reader(package_file)
        for row in package_reader:
            package_id, address, city, state, zip_code, deadline, weight, notes = row
            package = Package(package_id, address, city, state, zip_code, deadline, int(weight), notes)
            package_hash_table.insert(package_id, package)
            # print(f"Package {package_id} inserted into hash table")  # Shows packages loaded in hashtable

    return package_hash_table


# Create the hash table and load packages
hash_table = loadPackages()

# print("\nSearch:")
# package = package_hash_table.search("1")
# if package:
#  print(package.__dict__)

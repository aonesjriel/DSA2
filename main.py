"""
WGUPS DSA2 Task 2 Implementation Phase
Student ID: 012515260
"""

from file_reader import *
from hash_table import *


#loads all packages from file to available_packages list
available_packages = load_packages_from_csv("package_file.csv")

#loads addresses and their indexes into dictionary of possible addresses
#and creates a 2d list of distances
possible_addresses, distances = load_distances_from_csv("distance_file.csv")

#create hash table that will be used to store packages
#O(n)
package_table = HashTable()
#storing packages in hash table O(n)
for package in available_packages:
    package_table.insert(package)


truck1 = [33, 26]
truck2 = []
truck3 = []



start_index = 0
smallest_distance = 50

for package in truck1:

    current_package = package_table.lookup(package)
    distance = 0

    if current_package is not None:
        address_index = possible_addresses[current_package.address]
        if start_index < address_index:
            distance = distances[address_index][start_index]
        else:
            distance = distances[start_index][address_index]

    if float(distance) < float(smallest_distance):
        smallest_distance = distance

print(smallest_distance)

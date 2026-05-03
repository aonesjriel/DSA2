"""
WGUPS DSA2 Task 2 Implementation Phase
Student ID: 012515260
"""

from file_reader import *
from hash_table import *
from utilities import *


#create hash table that will be used to store packages
#O(n)
package_table = HashTable()

#loads all packages from file and store in hash table
load_packages_from_csv(package_table)

#creates dictionary that stores indexes for address; used to index distances 2d list
available_addresses = load_addresses_from_csv()

#loads distances into a 2d list
distances = load_distances_from_csv()

#creating time object to store time; setting default time as 8:00
time_hour = time(hour=8, minute=0, second=0, microsecond=0)
start_time = datetime.combine(datetime.now(), time_hour)

#manually added packages to the 3 trucks
truck1 = [7,8,10,11, 12] #[1,2,4,5,7,8,10,11,12,13,14,15,16,17,19,20]
truck2 = [3,18,21,22,23,24,25,26,27,29,30,31,33,34,35,36,38]
truck3 = [6,9,25,28,32,37,39,40]




distance_traveled, time_elapsed = package_delivery(truck1, start_time, package_table)
print(time_elapsed)
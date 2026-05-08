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
time_hour_truck1 = time(hour=8, minute=0, second=0, microsecond=0)
start_time_truck1 = datetime.combine(datetime.now(), time_hour_truck1)

#truck 2 cannot leave until delayed packages are back
time_hour_truck2 = time(hour=9, minute=5, second=0, microsecond=0)
start_time_truck2 = datetime.combine(datetime.now(), time_hour_truck2)

#packages for truck 3 are delayed until 9:54 (truck1 comes back at 9:53)
time_hour_truck3 = time(hour=9, minute=54, second=0, microsecond=0)
truck3_start_time = datetime.combine(datetime.now(), time_hour_truck3)

#manually added packages to the 3 trucks
truck1 = [1,13,14,15,16,19,20,29,30,31,34,37,40]
truck2 = [2,3,4,5,6,7,8,11,12,18,25,36,38]
truck3 = [9,10,17,21,22,23,24,26,27,28,32,33,35,39]
trucks = [truck1, truck2, truck3]

truck3distance_traveled, truck3_time_elapsed = package_delivery(truck3, truck3_start_time, package_table)
#print("time after truck finished:", truck3_time_elapsed, "Distance:", truck3distance_traveled)

truck1_distance_traveled, truck1_time_elapsed = package_delivery(truck1, start_time_truck1, package_table)
#print("Time after truck finished deliveries:", truck1_time_elapsed, "Distance:", truck1_distance_traveled)

truck2_distance_traveled, truck2_time_elapsed = package_delivery(truck2, start_time_truck2, package_table)
#print("Time after truck finished deliveries:", truck2_time_elapsed, "Distance:", truck2_distance_traveled)

load_title()
user_input_string = input("Please enter a time (format HH:MM): ")
user_input_datetime = datetime.strptime(user_input_string, "%H:%M")
nine_o_five = time(hour=9, minute=5, second=0, microsecond=0)
ten_twenty = time(hour=10, minute=20, second=0, microsecond=0)

#CLI the user gives a time, and package data displayed based on the time
#O(n)
for package_id in range(1,41):

    this_package = package_table.lookup(package_id)
    this_package.check_status(user_input_datetime.time())

    #tags package with truck number
    if package_id in truck1:
        this_package.truck_number = trucks.index(truck1) + 1
    elif package_id in truck2:
        this_package.truck_number = trucks.index(truck2) + 1
    elif package_id in truck3:
        this_package.truck_number = trucks.index(truck3) + 1
    else:
        this_package.truck_number = None

    if this_package.delivery_time > user_input_datetime.time():
        this_package.delivery_time = None
    if this_package.loading_time > user_input_datetime.time():
        this_package.loading_time = None

    #accomodate special cases:
    is_delayed = False
    if this_package.special_notes == "Delayed on flight---will not arrive to depot until 9:05 am":
        is_delayed = True
    if user_input_datetime.time() < nine_o_five and is_delayed:
        this_package.loading_time = None
        this_package.status = "DELAYED"
        this_package.delivery_time = None
    elif user_input_datetime.time() > ten_twenty and this_package.special_notes == "Wrong address listed":
        this_package.address = "410 S. State St."




    print(this_package)


print("Total distance between three trucks: ", truck1_distance_traveled + truck2_distance_traveled + truck3distance_traveled)
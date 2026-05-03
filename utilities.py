from datetime import *

from file_reader import load_distances_from_csv, load_addresses_from_csv

#Function takes in two addresses and returns the distance between them by referencing the
#address dictionary and the distances 2d list
#O(1)
def get_distance(address_a, address_b):
    distances = load_distances_from_csv()
    addresses = load_addresses_from_csv()


    index_a = addresses[address_a]
    index_b = addresses[address_b]

    if index_a < index_b:
        return distances[index_b][index_a]

    return distances[index_a][index_b]



#Greedy Nearest Neighbor algorithm (method) that takes in list of package ids and the hash table of packages
#Determines the nearest location for a package in the list
#Returns nearest package along with the distance
#O(n)
def find_nearest_package(truck_location, list_of_packages, package_table):

    print(list_of_packages)

    #keep track of smallest distance; set at 100 by default
    current_minimum = 100

    package_to_be_delivered = None

    for package in list_of_packages:
        current_package = package_table.lookup(package)
        current_package_location = current_package.address

        #get distance between package and current truck location
        distance = get_distance(truck_location, current_package_location)

        #check if distance is the shortest
        if float(distance) < float(current_minimum):
            current_minimum = distance
            package_to_be_delivered = current_package
        #if not, keep going

    #once found, return package
    return package_to_be_delivered, float(current_minimum)



#O(n^2)
def package_delivery(packages_list, start_time, package_table):
    speed = 18
    total_distance = 0

    delivery_list = packages_list.copy()

    #starting point of truck/ will update to current location of truck
    current_truck_location = 'HUB'

    for package in packages_list:

        package_to_deliver, distance = find_nearest_package(current_truck_location, delivery_list, package_table)
        total_distance += distance

        #remove package that is being delivered from list of packages
        delivery_list.pop(delivery_list.index(package_to_deliver.id_num))

        #calculate time to move to location time = distance / speed (18 MPH)
        start_time = start_time + timedelta(hours = distance / speed)

        #TODO fix delivery time problem --> only keeping track of individual times not total elapsed time
        #timestamp delivery
        package_to_deliver.delivery_time = start_time
        print("Package ", package_to_deliver.id_num, " delivered at:  ", package_to_deliver.delivery_time.time())


        #TODO fix this problem --> truck location not changing?
        #move truck to current package_to_deliver.address
        current_truck_location = package_to_deliver.address
        print("truck location: ", current_truck_location)

    print("list of packages: ", delivery_list)
    print("truck location: ", current_truck_location)

    return total_distance, start_time.time()
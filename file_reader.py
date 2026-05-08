from package import Package
import csv

#This function reads data from file
#each line is package data for one package
#returns list of package objects
#O(n) time complexity
def load_packages_from_csv(hashtable):

    with open('package_file.csv') as csvfile:
        #create CSV reader object
        csvreader = csv.reader(csvfile, delimiter=',')

        #skips header line
        next(csvreader)

        #looping through lines in file
        for row in csvreader:
            id_num = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zipcode = row[4]
            deadline = row[5]
            weight = row[6]
            #checks if there are any special notes
            if len(row) == 7:
                special_notes = ""
            else:
                special_notes = row[7]

            #create new package with details
            package = Package(id_num, address, city, state, zipcode, deadline, weight, special_notes,"At hub")
            #add package to hash table
            hashtable.insert(package)


#Read CSV file and load distance table to 2d list
#O(n) takes file name as a parameter, returns dictionary of address with corresponding index, and
#list of distances to index distance values
def load_distances_from_csv():
    distances = []
    with open('distance_file.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        for row in csvreader:

            #pop address off
            row.pop(0)
            #Append the rest of distance to list (which creates list of lists)
            distances.append(row)

        return distances

#Read CSV file and load addresses into dictionary
#O(n)
def load_addresses_from_csv():
    distance_dictionary = {}
    dictionary_index = 0

    with open('distance_file.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        for row in csvreader:

            address = row.pop(0)
            distance_dictionary[address] = dictionary_index
            dictionary_index += 1

    return distance_dictionary
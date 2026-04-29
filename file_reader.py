from package import Package
import csv

#This function reads data from file
#each line is package data for one package
#returns list of package objects
#O(n) time complexity
def load_packages_from_csv(filename):

    packages = [] #list that stores packages created from the CSV file

    with open(filename) as csvfile:
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
            package = Package(id_num, address, city, state, zipcode, deadline, weight, special_notes, "None", "None")
            #add package to packages list
            packages.append(package)

    return packages #returns list of package objects

#Read CSV file and load distance data into dictionary
#O(n) takes file name as a parameter, returns dictionary of address with corresponding index, and
#list of distances to index distance values
def load_distances_from_csv(filename):
    distance_dictionary = {}
    dictionary_index = 0
    distances = []
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        for row in csvreader:

            #pop address off
            address = row.pop(0)

            #Insert address into dictionary Key = address, value = index
            distance_dictionary[address] = dictionary_index

            #Append the rest of distance to list (which creates list of lists)
            distances.append(row)


            dictionary_index += 1
            #print(address , ":" , distance_dictionary[address])


        return distance_dictionary, distances



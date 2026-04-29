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

#TODO <read data from distance table csv and >
'''def load_distances_from_csv(filename):
    addresses = []
    with open(filename) as csvfile:'''




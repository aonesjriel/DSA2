from package import Package
from file_reader import *
from hash_table import *




available_packages = load_packages_from_csv("package_file.csv")
learningHash = HashTable()



for package in available_packages:
    learningHash.insert(package)
    #print(learningHash.lookup(package))







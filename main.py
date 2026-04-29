'''
WGUPS DSA2 Task 2 Implementation Phase
Student ID: 012515260
'''

from package import Package
from file_reader import *
from hash_table import *




available_packages = load_packages_from_csv("package_file.csv")
learningHash = HashTable()



for package in available_packages:
    learningHash.insert(package)



for package in available_packages:
    print(learningHash.lookup(package))







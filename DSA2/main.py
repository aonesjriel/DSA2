from package import Package
from file_reader import *




available_packages = load_packages_from_csv("package_file.csv")



for package in available_packages:
    print(package)
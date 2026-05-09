from datetime import time
class Package:

    #Constructor: Complexity: O(1)
    def __init__(self, id_num, address, city, state, zipcode, deadline, weight, special_notes, status):
        self.id_num = id_num
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipcode
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes

        #default time
        self.delivery_time = time(hour=0, minute=0, second=0, microsecond=0)
        self.loading_time = time(hour=0, minute=0, second=0, microsecond=0)
        self.status = status

        #set default to 0 for no truck number
        self.truck_number = 0



    #This method defines how the print() method will operate on an object of Package type; Complexity: O(1)
    def __str__(self):
        return (f"ID: {str(self.id_num)} Address: {self.address} City: {self.city} "
                f"State: {self.state} Zip: {self.zip} "
                f"Deadline: {self.deadline} Weight: {str(self.weight)} "
                f"Special Notes: {self.special_notes} "
                f"Delivery Time: {self.delivery_time} Loading Time: {self.loading_time} "
                f"Status: {self.status} " f"Truck Number: {self.truck_number}")


    #O(1)
    #Checks if status should be updated based on the time user will enter in main
    def check_status(self, user_time):
        if self.delivery_time is None:
            self.status = "DELAYED"

        if self.delivery_time < user_time:
            self.status = "delivered"
        elif self.delivery_time > user_time:
            self.status = "en route"
        if self.loading_time > user_time:
            self.status = "at hub"
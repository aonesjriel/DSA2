class Package:

    #Constructor: Complexity: O(1)
    def __init__(self, id_num, address, city, state, zipcode, deadline, weight, special_notes, delivery_time, loading_time):
        self.id_num = id_num
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipcode
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes

        self.delivery_time = "None"
        self.loading_time = "None"



    #This method defines how the print() method will operate on an object of Package type; Complexity: O(1)
    def __str__(self):
        return (f"ID: {str(self.id_num)} Address: {self.address} City: {self.city} "
                f"State: {self.state} Zip: {self.zip} "
                f"Deadline: {self.deadline} Weight: {str(self.weight)} "
                f"Special Notes: {self.special_notes} "
                f"Delivery Time: {self.delivery_time} Loading Time: {self.loading_time}")

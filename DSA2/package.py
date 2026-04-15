class Package:

    def __init__(self, id_num, address, city, state, zipcode, deadline, weight, special_notes):
        self.id = id_num
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipcode
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes


    def __str__(self):
        return (f"ID: {str(self.id)} Address: {self.address} City: {self.city} "
                f"State: {self.state} Zip: {self.zip} "
                f"Deadline: {self.deadline} Weight: {self.weight} "
                f"Special Notes: {self.special_notes}")

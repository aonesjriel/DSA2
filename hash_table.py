class HashTable:

    #Constructor for HashTable class; Complexity: O(n)
    def __init__(self):
        #list of lists
        #each inner list is a bucket in the table
        self.list = []
        self.size = 10
        for i in range(self.size):
            self.list.append([])


    #inserts key value pair into hash table. uses key and hash function to find bucket index
    #O(1)
    def insert(self, package_object):

        #get bucket index and corresponding list inside using hash function and bucket index
        bucket_index = package_object.id_num % self.size
        bucket_index_list = self.list[bucket_index]

        #update if the key already exists
        for pair in bucket_index_list:
            if pair[0] == package_object.id_num:
                pair[1] = package_object
                return True

        #add key and value "list" to bucket
        bucket_index_list.append([package_object.id_num, package_object])
        return True
        #print("The package with id: " + str(package_object.id_num) + " went in bucket: " + str(bucket_index))



    #Searches hash table if package exists returns package if found, or None
    #O(n)
    def lookup(self, package_object):

        #get bucket index and corresponding list inside using hash function and bucket index
        bucket_index = package_object % self.size
        bucket_index_list = self.list[bucket_index]

        for pair in bucket_index_list:
            if pair[0] == package_object:
                return pair[1]

        return None



    def __str__(self):
        return str(self.list)


# Source: W-1_ChainingHashTable_zyBooks_Key-Value.py
# Source: C950 Webinar-1 - Let's Go Hashing
# This is a self-resizing hash table that built upon lists
# to insert, it hashes the key and uses the modulo of the length in order to find the index of insertion
# if a collision occurs, it will append a new bin to the bin_list
# to update, if a key is found it will update the item at that key
class HashTable:
    def __init__(self, initial_capacity=30):
        # set initial capacity of the table ( the buckets)
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Insert or update an item into the hash table
    # O(1) to insert
    # O(n) to update, based on length of bucket
    def insert(self, key, item):
        
        bin = hash(key) % len(self.table)
        bin_list = self.table[bin]
 
        # update key if it is already in the bin
        for key_value in bin_list:

          if key_value[0] == key:
            key_value[1] = item
            return True
        
        # if not, insert the item to the end of the bin list.
        key_value = [key, item]
        bin_list.append(key_value)
        return True


    # O(1) to search a bucket of length 1
    # O(n) to search a bucket of length > 1
    def search(self, key):
        # get the bin list where this key would be.
        bin = hash(key) % len(self.table)
        bin_list = self.table[bin]
        #print(bucket_list)
 
        # search for the key in the bin list
        for key_value in bin_list:
          #print (key_value)
          if key_value[0] == key:
            return key_value[1] # value
        return None

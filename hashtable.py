
# Source: W-1_ChainingHashTable_zyBooks_Key-Value.py
# Source: C950 Webinar-1 - Let's Go Hashing
class HashTable:
    def __init__(self, initial_capacity=30):
        # set initial capacity of the table ( the buckets)
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Insert or update an item into the hash table
    def insert(self, key, item): 
        
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
 
        # update key if it is already in the bucket
        for kv in bucket_list:
          #print (key_value)
          if kv[0] == key:
            kv[1] = item
            return True
        
        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True
    
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        #print(bucket_list)
 
        # search for the key in the bucket list
        for kv in bucket_list:
          #print (key_value)
          if kv[0] == key:
            return kv[1] # value
        return None
    
def remove(self, key):
    # get the bucket list where this item will be removed from.
    bucket = hash(key) % len(self.table)
    bucket_list = self.table[bucket]

    # remove the item from the bucket list if it is present.
    for kv in bucket_list:
    #print (key_value)
        if kv[0] == key:
            bucket_list.remove([kv[0],kv[1]])
class ChainingHashTable:  # Hashtable class
    def __init__(self, initial_capacity=40):  # Constructor to initialize the hash table with initial capacity
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

# Cited From Zy book WGU Learning Resources SEE Task I for full citation
    def insert(self, key, item):  # Insert a key value pair into the hash table
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:  # Checks if the key already exists in bucket and updates
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]  # Create a key value pair
        bucket_list.append(key_value)  # Add the pair to the bucket list
        return True

# Cited From Zy book WGU Learning Resources SEE Task I for full citation
    def search(self, key):  # Search for a key and returns its value
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):  # Remove a key value pair from the hash table
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    def lookup(self, key):  # Perform a lookup for a key and return value
        index = hash(key) % len(self.table)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def updateStatus(self, key, newStatus):  # Updates the status of a package with key specified
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1].status = newStatus

    def updateDeliveryTime(self, key, newTime):  # Updates delivery time of a package with key specified
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1].delivery_time = newTime

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return str(self)

    def find(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return current

    def insert_or_update_at_head(self, key, value, replace=False):
        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return
            else:
                current = current.next
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_tail(self):
        pass

    def delete(self):
        if self.head.key == key:
            if self.head.next:
                #if head.next exist, move head up
                self.head = self.head.next
                return
            else:
                # if only node is head, delete that node
                self.head = None
                return
        current = self.head
        marker = current
        while current is not None:
            if current.key == key:
                if current.next:
                    marker.next = current.next
                    self.head.next = marker
                else:
                    self.head = None

    def add_to_node(self, node):
        while current is not None:
            if self.key == key:
                return current.value
            else:
                current = current.next
        return current

    # def __str__(self):
    #     return f'{self.key} is {self.value}'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.load = 0

    def __repr__(self):
        return str(self)


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.load / self.capacity


    def fnv1(self, key, seed=0):
        """
        FNV-1 Hash, 64-bit
        """
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        #FNV-1a Hash Function
        hash = offset_basis + seed
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = ((hash << 5) + 5) + ord(x)
        return hash & 0xFFFFFFFF

        # hash = 5381
        # for c in key:
        #     hash = (hash * 33) + ord(c)
        # return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.load += 1
        # check load factor
        if self.get_load_factor() > 0.7:
            # if above 0.7, resize to double capacity
            self.resize(self.capacity * 2)

        index_item = self.hash_index(key)
        if self.storage[index_item] is None:
            self.storage[index_item] = LinkedList()
            self.storage[index_item].insert_or_update_at_head(key, value)
        else:
            self.storage[index_item].insert_or_update_at_head(key, value)




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index_item = self.hash_index(key)

        if self.storage[index_item].head.key == key:
            if self.storage[index_item].head.next:
                #if head.next exist, move head up
                self.storage[index_item].head = self.head.next
                self.load -= 1
            else:
                # if only node is head, delete that node
                self.storage[index_item].head = None
                self.load -= 1
                return
        current = self.storage[index_item].head
        marker = current
        while current is not None:
            if current.key == key:
                if current.next is None:
                    marker.next = current.next
                    self.storage[index_item].head = marker
                    self.load -= 1
                else:
                    self.storage[index_item].head = marker
                    self.load -= 1
            marker = current
            current = current.next
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        item_index = self.hash_index(key)
        if self.storage[item_index] is not None:
            return self.storage[item_index].find(key)
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        self.storage = [None] * self.capacity


if __name__ == "__main__":
    ht = HashTable(8)

    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")

    # ht.delete("key-7")
    # ht.delete("key-6")
    # ht.delete("key-5")
    # ht.delete("key-4")
    # ht.delete("key-3")
    # ht.delete("key-2")
    # ht.delete("key-1")
    ht.delete("key-0")

    # print(ht.get('line_4'))

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
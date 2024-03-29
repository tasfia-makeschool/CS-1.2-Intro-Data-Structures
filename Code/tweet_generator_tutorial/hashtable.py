#!python

from linkedlist import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.count = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    # thanks ben
    def __iter__(self):
        for bucket in self.buckets:
            for item in bucket.items():
                yield item

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def num_buckets(self):
        return len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        Answer: O(n) since it has to gather all the keys inside the hashtable.
        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        Answer: O(n) since it has to gather all the values inside the hashtable.
        """
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?
        Answer: O(n) since it has to gather all the key-value pairs inside 
        the hashtable.
        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?
        Answer: O(n) if a count attribute is not set up, O(b) if it is
        """
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        count = 0
        for bucket in self.buckets:
            # for key, value in bucket.items():
            #     count += 1
            count += bucket.length_fast()
        return count
    
    def length_fast(self):
        return self.count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?
        Answer: Average running time would be O(n) where n is the number of 
        key-value pairs in the hashtable. 
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        bucket = self._bucket_index(key)
        if self.buckets[bucket].is_empty() == False:
            return self.buckets[bucket].find(lambda item: item[0] == key) is not None
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        Answer: O(n/b) = O(l), where n is the number of key-value pairs, b is the
        number of buckets in the hashtable, and l is the load factor (the average 
        number of pairs in each bucket).
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_index = self._bucket_index(key)
        if self.contains(key):
            return self.buckets[bucket_index].find(lambda item: item[0] == key)[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?
        Answer: O(l) since it has to find if the key exists first within
        the specific bucket hash function's return value points to.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        bucket_index = self._bucket_index(key)
        if self.contains(key):
            self.buckets[bucket_index].replace((key, self.get(key)), (key, value))
        else:
            self.buckets[bucket_index].append((key, value))
        self.count += 1

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        Answer: O(l) since it has to find if the key exists first within
        the specific bucket the hash function's return value points to.
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_index = self._bucket_index(key)
        if self.contains(key):
            self.buckets[bucket_index].delete((key, self.get(key)))
            self.count -= 1
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    # print('length: {}'.format(ht length_slow()))
    print('length: {}'.format(ht.length_fast()))    

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        # print('length: {}'.format(ht length_slow()))
        print('length: {}'.format(ht.length_fast()))

def test_hash_table_2():
    ht2 = HashTable(3)
    for key, value in [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]:
        ht2.set(key, value)
    # print('hash table: {}'.format(ht2))
    # print(ht2.keys())
    # for key in ht2.keys():
    #     print(ht2._bucket_index(key), ht2.get(key))
    # print(ht2.length_fast())
    # print(ht2.num_buckets())

    for item in ht2:
        print(item)
        # for node in ll:
        #     print(node)

if __name__ == '__main__':
    pass
    # test_hash_table()
    test_hash_table_2()

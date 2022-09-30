# COLLISION: A problem where two keys have same hash value; 
# For this example, we will use a method called chaining the simplest method
class myHashTable:
    def __init__(self):
        self.capacity = 10 
        self.size = 0
        self.buckets = [None] * self.capacity
        
        
    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            print((idx + len(key)) ** ord(c))
            # hashsum += (idx + len(key)) ** ord(c)
            # hashsum = hashsum % self.capacity
        return hashsum



    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)
        

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
            if node is None:
                return None
            else:
                return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
            if node is None:
                return None
            else:
                self.size -= 1
                result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
        return result


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



        
    


# use cases:
# 1.Write a function to determine whether a string contains repeated characters.
# 2.Given a string of any length, find the most-used character in the string.
# 3.Write a function to determine whether two strings are anagrams.
            
        
        
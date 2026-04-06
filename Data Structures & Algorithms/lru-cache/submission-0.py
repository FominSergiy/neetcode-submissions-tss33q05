class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        # link nodes
        self.left.next = self.right
        self.right.prev = self.left
    

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node: Node) -> None:
        # insert to right
        right_dummy, right_real = self.right, self.right.prev

        # set real pointer
        right_real.next = node
        node.prev = right_real

        # set dummy pointers
        right_dummy.prev = node
        node.next = right_dummy


    def get(self, key: int) -> int:
        # find node, delete it and isert it to the top
        if key in self.cache:
            tmp = self.cache[key]
            self.remove(tmp)
            self.insert(tmp)
            return tmp.val
        return -1

    def put(self, key: int, value: int) -> None:
        #update if exist
        if key in self.cache:
            # remove
            temp = self.cache[key]
            self.remove(temp)

            # add new
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            return

        # add new pair
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        # check for capacity
        if len(self.cache.keys()) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


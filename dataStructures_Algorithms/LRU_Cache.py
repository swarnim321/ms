class dll (object):
    def __init__(self,key,val):
        self.key = key
        self.val=val
        self.prev= None
        self.next= None

class LRUcache(object):
    def __init__(self, capacity):
        self.capacity= capacity
        self.length =0
        self.head=dll(-1,-1)
        self.tail=self.head
        self.hash={}

    def setTail(self,node):
        while node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.next = None
            node.prev = self.tail
            self.tail = node

    def put(self,key,value):
        if key in self.hash:
            node = self.hash[key]
            node.val = value
            self.setTail(node)
        else:
            node = dll(key,value)
            self.hash[key]= node
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.length = self.length +1
            if self.length>self.capacity:
                key = self.head.next.key #check this part
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.hash[key]  #check this part
                self.length = self.length -1

    def get(self,key):
        if key not in self.hash:
            return -1
        node = self.hash[key]
        val = node.val
        self.setTail(node)
        return val





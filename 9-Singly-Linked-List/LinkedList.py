class Item:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def __str__(self):
        if self.head is not None:
            current = self.head
            out = 'LinkedList [\n' + str(current.data) + '\n'
            while current.next is not None:
                current = current.next
                out += str(current.data) + '\n'
            return out + ']' + '\n' + str(self.counter)
        return 'LinkedList []'

    def append(self, number):
        # first we need to create new Item of the List
        new_item = Item(number)
        # if there are no elements in the list, self.head is None
        if self.head is None:
           # so if list is empty new_item will be the 1st element, so...
            self.head = new_item
            self.tail = new_item
            return

        item = self.tail
        item.next = new_item
        self.tail = new_item

    def delete(self, number):
        item = self.head
        prev = None
        while item is not None and item.data is not number:
            prev = item
            item = item.next
        if item is None:
            return
        item = item.next
        if prev is not None:
            prev.next = item
        else:
            self.head = item

    def count(self):
        self.counter = 0
        item = self.head
        while item is not None:
            self.counter += 1
            item = item.next
        return self.counter

    def trim(self, sum):
        if sum <= self.counter:
            item = self.head
            prev = None
            while self.counter is not sum:
                prev = item
                item = item.next
                self.counter -= 1
            if prev is not None:
                item.next = None
                prev.next = None
            else:
                self.head = None
        return


L = List()
L.append(10)
L.append(20)
L.append(30)
L.append(40)
L.append(50)
L.count()
L.trim(5)
print(L)

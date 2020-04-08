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
        if self.head != None:
            current = self.head
            out = 'LinkedList [\n' + str(current.data) + '\n'
            while current.next != None:
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

        # otherwise, if list is not empty we need to go to the last element of it.
        # But everything we know is **self.head**.
        # So how we can do that? **self.head** is type of **Item**, so it has 2 attributes: 1. data 2. next.
        # So, if we know **self.head** it means we know **self.head.data** and **self.head.next**.
        # **self.head.next** is type of **Item** as well.
        # So, , if we know **self.head.next** it means we know **self.head.next.data** and
        # **self.head.next.next** etc.
        # We can move next and next and finally we will come to the end (**element.next** will be **None**)

        item = self.tail
        item.next = new_item
        self.tail = new_item

    def delete(self, number):
        item = self.head
        prev = None
        while item != None and item.data != number:
            prev = item
            item = item.next
        if item == None:
            return
        item = item.next
        if prev != None:
            prev.next = item
        else:
            self.head = item

    def count(self):
        self.counter = 0
        item = self.head
        while item != None:
            self.counter += 1
            item = item.next
        return self.counter

    def trim(self, sum):
        if sum <= self.counter:
            item = self.head
            prev = None
            while self.counter != sum:
                prev = item
                item = item.next
                self.counter -= 1
            if prev != None:
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

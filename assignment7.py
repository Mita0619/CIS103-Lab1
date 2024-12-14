class Array(object):

    def __init__(self, capacity, fillValue=None):
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, newItem):
        self.items[index] = newItem


class ArrayBag(object):

    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self.size

    def __str__(self):
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def add(self, item):
        if self.size == len(self.items):
            self.resize(len(self.items) * 2)
        self.items[self.size] = item
        self.size += 1

    def remove(self, item):
        targetIndex = 0
        while targetIndex < self.size and self.items[targetIndex] != item:
            targetIndex += 1

        if targetIndex == self.size:
            raise ValueError(f"{item} not found in the bag")

        for i in range(targetIndex, self.size - 1):
            self.items[i] = self.items[i + 1]

        self.size -= 1
        self.items[self.size] = None

        if self.size <= len(self.items) // 4:
            self.resize(len(self.items) // 2)

    def resize(self, newSize):
        newItems = Array(newSize)
        for i in range(self.size):
            newItems[i] = self.items[i]
        self.items = newItems


def testArrayBag():
    bag = ArrayBag()

    for i in range(100):
        bag.add(i)

    print("Added 100 items, length of bag =", len(bag))
    print("Expect 160 as length of array =", len(bag.items))
    print(bag)

    for item in range(76):
        bag.remove(item)

    print("Removed 76 items, expect 24 as length of bag:", len(bag))
    print("Expect 80 as length of array =", len(bag.items))

    for item in range(24):
        bag.remove(item + 76)

    print("Removed remaining items, length of bag =", len(bag))
    print("Expect 10 as length of array =", 10 * len(bag.items))


testArrayBag()
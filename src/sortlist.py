import bisect

class sortlist:
    """
    A list that keeps itself sorted.
    From: http://stackoverflow.com/a/12829310
    How to use:
        list = [101, 3, 10, 14, 23, 86, 44, 45, 45, 50, 66, 95, 17, 77, 79, 84, 85, 91, 73]
        s = sortlist(list)
        print(s)
        s.insert(99)
        print(s)
        print(s.search(52))
    """

    def __init__(self, list):
        self.list = []
        for item in list:
            bisect.insort(self.list, item)

    def insert(self, value):
        bisect.insort(self.list, value)

    def remove(self, value):
        self.list.remove(value)

    def to_list(self):
        return self.list[:]

    def index(self, value):
        return self.list.index(value)

    def __str__(self):
        return self.list.__str__()

    def __getitem__(self, i):
        return self.list[i]

    def __len__(self):
        return len(self.list)

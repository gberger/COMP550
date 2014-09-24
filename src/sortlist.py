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

    def __init__(self, list, sort_fn):
        self.list = list
        self.sort()

    def sort(self):
        l = []
        i = 0
        for i in range(len(self.list)):
            bisect.insort(l, self.list[i])
        self.list = l
        self.len = i

    def insert(self, value):
        bisect.insort(self.list, value)
        self.len += 1

    def remove(self, value):
        return self.list.remove(value)

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

    def search(self,value):
        left = bisect.bisect_left(self.list, value)
        if abs(self.list[min([left,self.len-1])] - value) >= abs(self.list[left-1] - value):
            return self.list[left-1]
        else:
            return self.list[left]

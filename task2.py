class CircBuffer1(object):
    def __init__(self, buff_size):
        self.size = buff_size
        self.count = 0
        self.buffer = [None for i in range(buff_size)]
        self.start = self.end = 0

    def put(self, el):
        self.buffer[self.end] = el
        self.end = (self.end + 1) % self.size
        if self.count < self.size:
            self.count += 1
        else:
            self.start = (self.start + 1) % self.size

    def get(self):
        if not self.count:
            return None
        res = self.buffer[self.start]
        self.start = (self.start + 1) % self.size
        self.count -= 1
        return res


class Node(object):
    def __init__(self, element, nxt=None):
        self.element = element
        self.next = nxt


class CircBuffer2(object):
    def __init__(self, buff_size):
        self.size = buff_size
        self.start = self.end = None
        self.count = 0

    def put(self, el):
        if not self.count:
            self.end = self.start = Node(el)
            self.count += 1
        elif self.count < self.size:
            self.end.next = self.end = Node(el)
            self.count += 1
        else:
            self.end.next = self.end = self.start
            self.end.element = el
            self.start = self.start.next

    def get(self):
        if not self.count:
            return None
        else:
            res = self.start.element
            self.start = self.start.next
            self.count -= 1
            return res

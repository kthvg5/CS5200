class Stack(object):
    def __init__(self):
        self.data = []
        self.index = -1

    def push(self, value):
        self.index += 1
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            return None
        tmp = self.data[self.index]
        self.data.pop()
        self.index -= 1
        return tmp

    def top(self):
        if self.is_empty():
            return None
        return self.data[self.index]

    def size(self):
        return self.index+1

    def is_empty(self):
        if self.index == -1:
            return True
        return False

    def print_stack(self):
        print "start[",
        for i in range(0, self.index + 1):
            print self.data[i], ", ",
        print " end"

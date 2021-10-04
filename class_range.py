class Myrange1:
    def __init__(self, start, stop, step = 0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.start = start
        return self
    def __next__(self):
        x = self.start

        while x <= self.stop:
            if self.step == 0 or None:
                print(x)
                x += 1
            else:
                print(x)
                x = x + self.step

primer = Myrange1(2, 25)
print (primer.__next__())
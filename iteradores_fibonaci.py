import time
class FiboIter():
    def __iter__(self):
        self.n0 = 0
        self.n1 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n0
        elif self.counter == 1:
            self.counter += 1
            return self.n1
        else:
            self.aux = self.n0 + self.n1
            #self.n0 = self.n1
            #self.n1 = self.aux
            self.n0, self.n1 = self.n1, self.aux
            return self.aux

def run():
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(1)

if __name__ == '__main__':
    run()
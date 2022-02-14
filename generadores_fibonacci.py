import time

def fibonacci_generator():
    n0 = 0
    n1 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n0
        elif counter == 1:
            counter += 1
            yield n1
        else:
            aux = n0 + n1
            n0, n1 = n1, aux
            counter += 1
            yield aux
def fibonacci_generator(max : int) -> int:
    n0 = 0
    n1 = 1
    counter = 0
    while n0+n1 <= max:
        if counter == 0:
            counter += 1
            yield n0
        elif counter == 1:
            counter += 1
            yield n1
        else:
            aux = n0 + n1
            n0, n1 = n1, aux
            counter += 1
            yield aux

if __name__ == '__main__':
    fibonacci = fibonacci_generator(50)
    for element in fibonacci:
        print(element)
        time.sleep(1)
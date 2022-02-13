#creando un iterador
#ejemplo de lo que hace un ciclo for
def iterar():
    my_list = [1,2,3,4,56,6]
    my_iter = iter(my_list)

    while True:
        try:
            element = next(my_iter)
            print(element)
        except StopIteration:
            break

def run():
    iterar()

if __name__ == '__main__':
    run()
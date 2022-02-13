from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos.")
    return wrapper

@execution_time
def ciclo():
    for _ in range(1, 10000000):
        pass    

@execution_time
def saludo(name="Gsdlkjydnsj"):
    print("Hola " + name)

@execution_time
def suma(a:int, b:int) -> int:
    return a + b

def run():
    ciclo()
    saludo()
    suma(4,5)

if __name__ == '__main__':
    run()
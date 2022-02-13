#Hola 3 -> HolaHolaHola
#Facundo 2 -> FacundoFacundo
#Platzi 4 -> PlatziPlatziPlatziPlatzi
def make_division(n):
    def division(x):
        return x / n
    return division

def run():
    division_3 = make_division(3)
    print(division_3(18))
    division_2 = make_division(2)
    print(division_2(22))
    division_4 = make_division(4)
    print(division_4(100))

if __name__ == '__main__':
    run()
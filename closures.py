#Hola 3 -> HolaHolaHola
#Facundo 2 -> FacundoFacundo
#Platzi 4 -> PlatziPlatziPlatziPlatzi
def make_repeater(n):
    def repeater(string):
        assert type(string) == str, "Solo cadenas"
        return string * n
    return repeater

def run():
    repeat_3 = make_repeater(3)
    print(repeat_3("Hola"))
    repeat_2 = make_repeater(2)
    print(repeat_2("Facundo"))
    repeat_4 = make_repeater(4)
    print(repeat_4("Platzi"))

if __name__ == '__main__':
    run()
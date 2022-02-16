#
def remove_duplicate(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
        else:
            print('removido el numero : ' + str(element))
    return without_duplicates

def run():
    list_number = [1,2,3,4,5,6,7,3,6,7,8,9]
    list_number = remove_duplicate(list_number)
    print(list_number)
    
    #set
    my_set1 = {3,4,5}
    my_set2 = {5,6,7}
    print('#union | ')
    my_set_union = my_set1 | my_set2
    print(my_set_union)
    print('#interseccion & ')
    my_set_interseccion = my_set1 & my_set2
    print(my_set_interseccion)
    print('#diferencia - ')
    my_set_diferencia = my_set1 - my_set2
    print(my_set_diferencia)
    print('#diferencia simetrica ^ ')
    my_set_diferencia_simetrica = my_set1 ^ my_set2
    print(my_set_diferencia_simetrica)



if __name__ == '__main__':
    run()

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

if __name__ == '__main__':
    run()

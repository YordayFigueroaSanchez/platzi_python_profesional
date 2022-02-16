import datetime

def run():
    my_time = datetime.datetime.now()
    print(my_time)
    my_day = datetime.datetime.today()
    print(f'Day : {my_day.day}')
    print(f'Month : {my_day.month}')
    print(f'Year : {my_day.year}')
    print('formateo de fecha')
    my_str = my_time.strftime('%d/%m/%Y')
    print(my_str)

if __name__ == '__main__':
    run()
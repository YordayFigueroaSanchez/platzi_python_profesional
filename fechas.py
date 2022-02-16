from dataclasses import dataclass
import datetime
import pytz

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
    #ZONA HORARIA
    bogota_timezone = pytz.timezone("America/Bogota")
    bogota_date = datetime.datetime.now(bogota_timezone)
    print("Bogota : " + bogota_date.strftime("%d/%m/%Y  %H:%M:%S"))
    mexico_timezone = pytz.timezone("America/Mexico_City")
    mexico_date = datetime.datetime.now(mexico_timezone)
    print("Mexico : " + mexico_date.strftime("%d/%m/%Y  %H:%M:%S"))

if __name__ == '__main__':
    run()
import random
from datetime import datetime
import time
import keyboard


def game_speed():
    simbol_pack = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    tru_speed = 0
    done_time_speed = []
        
    while tru_speed != 10:
        random_simbol = random.randint(0,25)
        simbol = simbol_pack[random_simbol]
        time_start_speed = datetime.now()
        print(f'СИМВОЛ - {simbol}')
        player_chislo_speed = (input(f'Быстро введите символ - '))
        
        random_simbol = random.randint(1,26)
        while player_chislo_speed != simbol:
            player_chislo_speed = (input(f'Быстро введите символ - '))
        if player_chislo_speed == simbol:
            print('Следующая')
            tru_speed = tru_speed + 1
            time_final_speed = datetime.now()
            sum_time_speed = ( time_final_speed - time_start_speed ).seconds
            done_time_speed.append(sum_time_speed)
       
    summa_speed = sum(done_time_speed)
    dlina_speed = len(done_time_speed)
    average_speed = summa_speed / dlina_speed
  
    print(done_time_speed)
    print(f'Ваше среднее время реакции ввода - {average_speed}')


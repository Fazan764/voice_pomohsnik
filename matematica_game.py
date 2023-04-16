import random
from datetime import datetime
import time



def game_speed():
    simbol = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    random_simbol = random.randint(0,25)
    tru_speed = 0
    done_time_speed = []
    player_chislo_speed = (input(f'Быстро введите символ - {simbol[random_simbol]}')).lower
    while tru_speed != 6:
        
        time_start_speed = datetime.now()
        random_simbol = random.randint(1,26)
        
       
        
        try:
            
            while player_chislo_speed == simbol[random_simbol]:

                
                player_chislo_speed = (input(f'Быстро введите символ - {random_simbol}')).lower
            

            if player_chislo_speed == [random_simbol]:
                print('Верно!')
                tru_speed = tru_speed + 1
                time_final_speed = datetime.now()
                sum_time_speed = ( time_final_speed - time_start_speed ).seconds 
                done_time_speed.append(sum_time_speed)

        except ValueError:
            print('ВЫ ВВЕЛИ НЕКОРРЕКТНЫЙ ОТВЕТ')

   
    summa_speed = sum(done_time_speed)
    dlina_speed = len(done_time_speed)
    average_speed = summa_speed / dlina_speed
  
   
    print(f'Ваше среднее время реакции ввода - {average_speed}')
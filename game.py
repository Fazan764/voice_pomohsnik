import random
from datetime import datetime
import time
import pyautogui as pag
import keyboard

def guess_chislo():
    point = 0
    chislo = random.randint(1,5)
    try:
        while True:
            playear = int(input('Введите число от 1 до 5 - '))
            if chislo == playear:
                print('Вы угадали число')
                print(f'число было {chislo}, ляпахов дать игроку - {point}')
                break
            if chislo >= playear:
                print('Загаданое число больше')
            if chislo <= playear:
                print('Загаданое число меньше')
            point = point + 1
            
    except ValueError:
        print('Вводить только числа')
    except RuntimeError:
        print('Вводить только числа')


def matematica_game():
    tru = 0
    done_time = []
    
    while tru != 6:
        time_start = datetime.now()
        one_chislo = random.randint(10,100)
        two_chislo = random.randint(10,100)
        final_chislo = one_chislo + two_chislo
   
        try:
            print(f'{one_chislo} + {two_chislo}')
            player_chislo = int(input('Ответ - '))
            
            
            
         
            while player_chislo != final_chislo:
                if player_chislo != final_chislo:
                    tru = tru - 1
                print(f'{one_chislo} + {two_chislo}')
                player_chislo = int(input('Ответ - '))
            

            if player_chislo == final_chislo:
                print('Правильно!')
                tru = tru + 1
                time_final = datetime.now()
                sum_time = (time_final - time_start ).seconds 
                done_time.append(sum_time)
            
            
        except ValueError:
            print('ВЫ ВВЕЛИ НЕКОРРЕКТНЫЙ ОТВЕТ')
            tru = tru - 1
           

   
    summa = sum(done_time)
    dlina = len(done_time)
    min_moment = min(done_time)
    max_moment = max(done_time)
    average = summa / dlina
    print(f'Самое долгое время решения - {max_moment}')
    print(f'Самое быстрое время решения - {min_moment}')
    print(f'Ваше среднее время решения - {average}')


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
def macros():
    

        kol_vo = 0
        keyboard.wait("m")
        while kol_vo != 8:
        
            keyboard.write("GG!WP")
            keyboard.press("enter")
            kol_vo = kol_vo + 1




   


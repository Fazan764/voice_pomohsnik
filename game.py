import random



def guess_chislo():
    point = 0
    chislo = random.randint(1,5)
    while True:
        playear = int(input('Введите число от 1 до 5 - '))
        if chislo == playear:
            print('Вы угадали число')
            break
        if chislo >= playear:
            print('Загаданое число больше')
        if chislo <= playear:
            print('Загаданое число меньше')
        point = point + 1
    print(f'число было {chislo}, ляпахов дать игроку - {point}')
   
    
guess_chislo()

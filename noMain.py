from game import *
import pyautogui as pag


from tkinter import *
window = Tk(className='Text helper')
window.configure(bg='grey22')
window.geometry('690x458')


    

def ygadai_chislo():
    pag.moveTo(850,980)
    pag.click(850,980,2,1,'left')
    guess_chislo()
    pag.click(1360, 1040, 1, 1, 'left')
def react_speed():
    pag.moveTo(850,980)
    pag.click(850,980,2,1,'left')
    game_speed()
    pag.click(1360, 1040, 1, 1, 'left')
def ymnay_game():
    pag.moveTo(850,980)
    pag.click(850,980,2,1,'left')
    matematica_game()
    pag.click(1360, 1040, 1, 1, 'left')
def macros_func():
    macros()

    








txtmacros = Label(
    text='МАКРОС - [m]',
    width = 20,
    height = 5,
    font='arial,30',
    bg='grey22',
    fg ='white'
)
txt = Label(
    text='Выберите действие',
    width = 20,
    height = 5,
    font='arial,30',
    bg='grey22',
    fg ='white'
)
void1 = Label(
    text=' ',
    width = 1,
    height = 10,
    bg='grey22'
)
void2 = Label(
    text=' ',
    width = 30 ,
    height = 10,
    bg='grey22'
)
void3 = Label(
    text=' ',
    width = 30 ,
    height = 10,
    bg='grey22'
)
void4 = Label(
    text=' ',
    width = 30 ,
    height = 10,
    bg='grey22'
)
void5 = Label(
    text=' ',
    width = 30 ,
    height = 10,
    bg='grey22'
)
btn1 = Button( 
    text = 'игра - "Угадай число"',
    width = 20 ,
    height = 5,
    bg='grey26',
    font='arial,16',
    command=ygadai_chislo
    )
btn2 = Button( 
    text = 'Игра на реакцию',
    width = 20 ,
    height = 5,
    bg='grey26',
    font='arial,16',
    command=react_speed
    )
btn3 = Button( 
    text = 'Математическая игра',
    width = 20 ,
    height = 5,
    bg='grey26',
    font='arial,16',
    command=ymnay_game
    )
btn4 = Button( 
    text = 'Макрос / use - [m]',
    width = 20 ,
    height = 5,
    bg='grey26',
    font='arial,16',
    command=macros_func,
    )
btn5 = Button( 
    text = 'СКОРО',
    width = 20 ,
    height = 5,
    bg='grey26',
    font='arial,16',
    )



void1.grid(column=0,row=0)
txt.grid(column=1,row=0)
btn1.grid(column=0,row=1)
btn2.grid(column=1,row=1)
btn3.grid(column=2,row=1)
btn4.grid(column=0,row=2)










window.mainloop()
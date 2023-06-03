import turtle

# Definicja rysunków etapów
hangman = [
    '''
       +---+
           |
           |
           |
           |
           |
    =======''',
    '''
       +---+
       |   |
           |
           |
           |
           |
    =======''',
    '''
       +---+
       |   |
       O   |
           |
           |
           |
    =======''',
    '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =======''',
    '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =======''',
    '''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =======''',
    '''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =======''',
    '''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    ======='''
]


def draw_hanged_man(number):
    # Ustawienie koloru
    if number == 7 :
        turtle.color('red')
    else:
        turtle.color('black')
    # Rysowanie etapu
    turtle.clear
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    turtle.write(hangman[number], font=('Arial', 16))




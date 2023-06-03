import random

##konwersja słowa na listę

def create_list(word):
    return list(word)


##konwersja wybranego słowa na podkreślenia
def convert_word(word):
    a = list('X' * len(word))
    return a


##wyświetlanie prawidłowe
def display(word_list):
    return ' '.join(word_list)


##wybór słowa z listy słów
def select_word(word_list):
    result = random.choice(word_list)
    return result


def used_letters(user_input, used_letters):
    used_letters.append(user_input)
    used_letters = list(set(used_letters))
    print(used_letters)
    return used_letters


## user input
def user_input(bot_world):
    while True:
        a = input("Podaj literę: ")
        if len(a) == 1 and a.isalpha():
            break
        elif a.upper() == bot_world.upper():
            break
        else:
            print('Błąd typu. Podaj literę.')
    return a.upper()
##sprawdzenie czy litera jest w słowie


def check_input(UserInput, word_list, used_letters):
    indexes = []
    while True:
        if UserInput in used_letters:
            print("Ta litera była wykorzystana, wprowadź inną!.")
            UserInput = user_input(word_list)
        else:
            break
    for i in range(len(word_list)):
        if word_list[i] == UserInput:
            indexes.append(i)
    return indexes


##podmienienie znaku w liście
def change_char(guess_list, indeks, user_input):
    guess_list[indeks] = user_input


def check_results(list1, list2):  ##sprawdzenie czy lista ze słowem zgadywanym jest taka sama jak lista ze słowem od usera
    if list1 == list2:
        return True
    else:
        return False
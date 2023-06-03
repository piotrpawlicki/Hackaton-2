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


def used_letters(user_input, used):
    used = set(used)
    used.add(user_input)
    return used


## user input
def user_input(bot_word):
    while True:
        a = input("Podaj literę: ")
        if len(a) == 1 and a.isalpha():
            break
        elif a.upper() == bot_word.upper():
            break
        else:
            print('Błąd typu. Podaj literę.')
    return a.upper()
##sprawdzenie czy litera jest w słowie


def check_input(UserInput, word_list):  ##zwraca indeksy na których znajduje się odgardnięta litera w słowie
    indexes = []
    for i in range(len(word_list)):
        if word_list[i] == UserInput:
            indexes.append(i)
    return indexes


##podmienienie znaku w liście
def change_char(guess_list, indeks, user_input):
    guess_list[indeks] = user_input


def display_set(set_word):
    return ' '.join(set_word)


def check_results(list1, list2):  ##sprawdzenie czy lista ze słowem zgadywanym jest taka sama jak lista ze słowem od usera
    if list1 == list2:
        return True
    else:
        return False

##sprawdzenie czy litera była wykorzystana
def was_used(user_input, used_letters):
    if user_input in used_letters:
        return True
    else:
        return False

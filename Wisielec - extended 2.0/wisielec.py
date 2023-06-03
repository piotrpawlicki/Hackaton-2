import openpyxl
from operation_on_strings import *
from cat_oper import *
from print_hangman import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from colorama import Fore
#from hangman_turtle import *


def main():
    # wczytanie pliku
    Tk().withdraw()
    file = askopenfilename(filetypes=[("Pliki excelowe", "*.xlsx")])
    worksheets = openpyxl.load_workbook(file)
    worksheets_names = worksheets.sheetnames
    guessing_words = guess_words(worksheets, worksheets_names)
    guess_number = 0
    guess_word = select_word(guessing_words).upper()
    guess_word_list = create_list(guess_word)
    hidden_word_list = convert_word(guess_word)
    letters_used = []

    while not check_results(guess_word_list, hidden_word_list):
        #draw_hanged_man(guess_number)
        print(hangman(guess_number))

        if guess_number == 7:
            #draw_hanged_man(guess_number)
            print(Fore.RED + hangman[7])
            break
        else:
            draw_hanged_man(guess_number)
            ##print(f'Wykorzystales nastepujące litery: {letters_used}')
            print(f'Wykorzystano litery : {display_set(letters_used)}')
            user_char = user_input(guess_word)
            result = check_input(user_char, guess_word_list)
            if user_char != guess_word :
                if result:
                     for i in result:
                        change_char(hidden_word_list, i , user_char)
                        letters_used = used_letters(user_char, letters_used)
                else:
                    if user_char in letters_used:
                        print('JuŻ wykorzystałeś tą literę, wybierz inną')
                        print(f'To była Twoja próba numer {guess_number}')
                        letters_used = used_letters(user_char, letters_used)
                    else:
                        print('Spróbuj jeszcze raz')
                        guess_number += 1
                        print(f'To była Twoja próba numrer {guess_number}')
                        letters_used = used_letters(user_char, letters_used)
            elif user_char == guess_word: ##wprowadzenie możliwości podania całego hasła
                guess_word_list = hidden_word_list
                break
        print(display(hidden_word_list))

    if check_results(guess_word_list, hidden_word_list):
        print('Gratuluję, wygrałeś!')
    else:
        print(f'Wisisz, koleżko. Miałeś odgadnąć słowo {guess_word}')


main()
# File: Wordle.py

"""
To-Do:
-Make buttons in fixed position
-Delete button
-Enter error

"""

from tkinter import *
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import (
    WordleGWindow,
    N_COLS,
    N_ROWS,
    CORRECT_COLOR,
    PRESENT_COLOR,
    MISSING_COLOR,
    KEY_LABELS
)

modNum = '2'
cSaver = CORRECT_COLOR
pSaver = PRESENT_COLOR
mSaver = MISSING_COLOR
CORRECT_COLOR_OPTION = "#ADD8E6" # Light blue for correct letters
PRESENT_COLOR_OPTION = "#FFCCCB" # Red for letters that don't appear
MISSING_COLOR_OPTION = "#FFD580" # Light orange for misplaced letters

# Selects random word
randomWord = random.choice(FIVE_LETTER_WORDS)

print(randomWord)

# Milestone 1:
    # Breaks word up
    # for index, letter in enumerate(randomWord):
    #     nextLetter.append(letter)
    #     gw.set_square_letter(N_COLS - 5, index, letter)

def wordle():

    def changeColor():

        global CORRECT_COLOR
        global PRESENT_COLOR
        global MISSING_COLOR
        global cSaver
        global pSaver
        global mSaver

        if CORRECT_COLOR == cSaver:
            print('first')
            for k in range(N_ROWS):
                for y in range(N_COLS):
                    if gw.get_square_color(k,y) == CORRECT_COLOR:
                        gw.set_square_color(k, y, CORRECT_COLOR_OPTION)
                    elif gw.get_square_color(k,y) == PRESENT_COLOR:
                        gw.set_square_color(k, y, PRESENT_COLOR_OPTION)
                    elif gw.get_square_color(k,y) == MISSING_COLOR:
                        gw.set_square_color(k, y, MISSING_COLOR_OPTION)

            for l in KEY_LABELS:
                for letter in l:
                    if gw.get_key_color(letter) == CORRECT_COLOR:
                        gw.set_key_color(letter, CORRECT_COLOR_OPTION)
                    elif gw.get_key_color(letter) == PRESENT_COLOR:
                        gw.set_key_color(letter, PRESENT_COLOR_OPTION)
                    elif gw.get_key_color(letter) == MISSING_COLOR:
                        gw.set_key_color(letter, MISSING_COLOR_OPTION)

            CORRECT_COLOR = CORRECT_COLOR_OPTION
            PRESENT_COLOR = PRESENT_COLOR_OPTION
            MISSING_COLOR = MISSING_COLOR_OPTION

        else:

            print('second')
            print(PRESENT_COLOR_OPTION)
            for k in range(N_ROWS):
                for y in range(N_COLS):
                    print(gw.get_square_color(k,y))
                    if gw.get_square_color(k,y) == CORRECT_COLOR_OPTION:
                        gw.set_square_color(k, y, cSaver)
                    elif gw.get_square_color(k, y) == PRESENT_COLOR_OPTION:
                        gw.set_square_color(k, y, pSaver)
                        print(pSaver)
                    elif gw.get_square_color(k,y) == MISSING_COLOR_OPTION:
                        gw.set_square_color(k, y, mSaver)

            for l in KEY_LABELS:
                for letter in l:
                    if gw.get_key_color(letter) == CORRECT_COLOR_OPTION:
                        gw.set_key_color(letter, cSaver)
                    elif gw.get_key_color(letter) == PRESENT_COLOR_OPTION:
                        gw.set_key_color(letter, pSaver)
                    elif gw.get_key_color(letter) == MISSING_COLOR_OPTION:
                        gw.set_key_color(letter, mSaver)

            CORRECT_COLOR = cSaver
            PRESENT_COLOR = pSaver
            MISSING_COLOR = mSaver

    def Shared():
        
        print('share')
        
        for k in range(N_ROWS):
            for y in range(N_COLS):
                gw.set_square_letter(k,y," ")

        for l in KEY_LABELS:
            for letter in l:

                print(letter)
                gw.set_key_color(letter, MISSING_COLOR)
            

    def enter_action(s):
        if s.lower() in FIVE_LETTER_WORDS:
            nextLetter = []
            chosenLetter = []
            for index, letter in enumerate(randomWord):
                nextLetter.append(letter.upper())

            for index, l in enumerate(s):
                chosenLetter.append(l.upper())
                
            print(chosenLetter)
            print(nextLetter)

            x = 0
            
            tempList = nextLetter
            chosenTemp = chosenLetter

            for index, anyLetter in enumerate(chosenLetter):

                if chosenLetter[index] not in nextLetter:
                    gw.set_key_color(chosenLetter[index], MISSING_COLOR)
                print("gray")
                gw.set_square_color(gw.get_current_row(), index, MISSING_COLOR)
        
            for index, anyLetter in enumerate(nextLetter):

                if anyLetter == chosenLetter[index]:
                    print("green")
                    gw.set_square_color(gw.get_current_row(), index, CORRECT_COLOR)
                    gw.set_key_color(chosenLetter[index], CORRECT_COLOR)
                    tempList[index] = '_'
                    chosenTemp[index] = '='

            for index, tempLetter in enumerate(chosenTemp):
                    
                for dex, cTempletter in enumerate(tempList):
                    print(tempLetter)
                    print(chosenTemp[index])
                    if chosenTemp[index] == tempList[dex]:
                        tempList[dex] = '-'
                        print('yellow')
                        gw.set_key_color(chosenLetter[index], PRESENT_COLOR)
                        gw.set_square_color(gw.get_current_row(), index, PRESENT_COLOR)
                        
                        print('entered')
                        break
                    
                print(tempList)

            gw.set_current_row(gw.get_current_row() + 1)

            for index, finished in enumerate(tempList):
                if tempList[index] == '_':
                    x += 1             

            if x == 5:
                gw.show_message("Congrats you have guessed the word in " + str(gw.get_current_row() ) + " tries!")
                gw.set_current_row(gw.get_current_row() + 6)
        else:
            gw.show_message("Not in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    btn = Button(gw._root, text = 'Share', bd = '5',
                          command = Shared)
    btn.place(x=185, y=480)

    btnOne = Button(gw._root, text = 'Change Color Scheme', bd = '5',
                          command = changeColor)
    btnOne.place(x=30, y=480)

# Startup code
if __name__ == "__main__":
    wordle()

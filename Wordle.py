# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import tkinter
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import (
    WordleGWindow,
    N_COLS,
    N_ROWS,
    CORRECT_COLOR,
    PRESENT_COLOR,
    MISSING_COLOR,
    KEY_LABELS,
    WordleKey,
)

from tkinter import *


CORRECT_COLOR_OPTION = "#ADD8E6" # Light blue for correct letters
PRESENT_COLOR_OPTION = "#ffcccb" # Red for letters that don't appear
MISSING_COLOR_OPTION = "#FFD580" # Light orange for misplaced letters

# Selects random word
randomWord = random.choice(FIVE_LETTER_WORDS)

print(randomWord)


def wordle():

    def changeColor():
        for k in range(N_ROWS):
            for y in range(N_COLS):
                if gw.get_square_color(k,y) == CORRECT_COLOR:
                    gw.set_square_color(k, y, CORRECT_COLOR_OPTION)
                elif gw.get_square_color(k,y) == PRESENT_COLOR:
                    gw.set_square_color(k, y, PRESENT_COLOR_OPTION)
                elif gw.get_square_color(k,y) == MISSING_COLOR:
                    gw.set_square_color(k, y, MISSING_COLOR_OPTION)


    def Shared():
        # if isinstance(tke, str):
        
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
                # gw.set_square_letter(N_COLS - 5, index, letter)

            for index, l in enumerate(s):
                chosenLetter.append(l.upper())
                # gw.set_square_letter(N_COLS - 5, index, l)
            print(chosenLetter)
            print(nextLetter)

            x = 0
            
            tempList = nextLetter
            chosenTemp = chosenLetter

            for index, anyLetter in enumerate(chosenLetter):
                # if chosenLetter[index] in nextLetter:
                #     print("yellow")
                #     gw.set_square_color(gw.get_current_row(), index, PRESENT_COLOR)

                if chosenLetter[index] not in nextLetter:
                    gw.set_key_color(chosenLetter[index], MISSING_COLOR)
                print("gray")
                gw.set_square_color(gw.get_current_row(), index, MISSING_COLOR)
        
            for index, anyLetter in enumerate(nextLetter):
                # if chosenLetter[index] in nextLetter:
                #     print("yellow")
                #     gw.set_square_color(gw.get_current_row(), index, PRESENT_COLOR)

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
                        # if letterCount > 1:
                        #     chosenTemp[index] = '-'
                    
                print(tempList)
                # if chosenTemp[index] in tempList:
            # for index, grey in enumerate(tempList):



            gw.set_current_row(gw.get_current_row() + 1)

            for index, finished in enumerate(tempList):
                if tempList[index] == '_':
                    x += 1
                

            if x == 5:
                gw.show_message("Congrats you have guessed the word in " + str(gw.get_current_row() ) + " tries!")
                gw.set_current_row(gw.get_current_row() + 6)
        else:
            gw.show_message("Not in word list")

    # root = tkinter.tk()

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    btn = Button(gw._root, text = 'Share', bd = '5',
                          command = Shared)
    btn.place(x=352, y=465)

    btnOne = Button(gw._root, text = 'Change Color Scheme', bd = '5',
                          command = changeColor)
    btnOne.place(x=30, y=480)

    # btn.pack()
    
    # gw._root.bind("<Key>", gw.key_action)
    # gw._root.bind("<ButtonPress-1>", gw.press_action)
    # gw._root.bind("<ButtonRelease-1>", gw.release_action)
    # gw.add_enter_listener(shareAction)

    # root = tkinter.Tk()

    # root.bind("<Key>", gw.key_action)
    # root.bind("<ButtonPress-1>", gw.press_action)
    # root.bind("<ButtonRelease-1>", gw.release_action)
    
    # shareResults = WordleKey(gw._canvas, 352, 465, 122, 50, "Share Results")

    # Shared(shareResults)
    
    # Marcus' Button Tests
    # window = Tk()
    # button = Button(window, text="Hola")
    # button.pack()

    # kl = KEY_LABELS()
    # kl.append("Change Color Scheme")

    # wk = WordleKey(Canvas, X, Y, 25, 25, "Change Color Scheme")
    # colorSchemeBtn = Button(wk, text="Change Color Scheme")
    # colorSchemeBtn.pack()

    # Milestone 1:
    # Breaks word up
    # for index, letter in enumerate(randomWord):
    #     nextLetter.append(letter)
    #     gw.set_square_letter(N_COLS - 5, index, letter)


# Startup code
if __name__ == "__main__":
    wordle()

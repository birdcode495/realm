import tkinter as tk

from tkinter import *   # --- Graphical User Interface (GUI) Construction with the Tkinter library

from BirdGuess_Images import *

from BirdGuess_Info import BirdGuess_sci

from BirdGuess_Info import BirdGuess_Spanish

from BirdGuess_Info import BirdGuess_english

from BirdGuess_Info import BirdGuess_french

from BirdGuess_Info import BirdGuess_german

from BirdGuess_Info import BirdGuess_chinese

from BirdGuess_Info import BirdGuess_pinyin

import time 

import random


BirdGuess_list_k = BirdGuess_list

BirdGuess_sci_k = BirdGuess_sci

BirdGuess_Spanish_k = BirdGuess_Spanish

BirdGuess_english_k = BirdGuess_english

BirdGuess_french_k = BirdGuess_french

BirdGuess_german_k = BirdGuess_german

BirdGuess_chinese_k = BirdGuess_chinese

BirdGuess_pinyin_k = BirdGuess_pinyin



index = 890
y = [0, 5, 19]
z = 0



def IndexCreation():

	global index
	global y 
	global z

	if z < len(y):
		index = y[z]
		#z = z + 1
		del y[z]

	else:
		print('fin')

	 


	



	#index = random.randint(0, len(BirdGuess_list_k) - 1)

	#index = random.randint(0, 5)
	


	


IndexCreation()


def GUI_Creation():

	raiz = Tk()

	raiz.title(BirdGuess_english_k[index])

	raiz.iconbitmap()

	miFrame = Frame(raiz)

	miFrame.pack()

	miImagen = PhotoImage(file = BirdGuess_list_k[index][0])

	Label(miFrame, image=miImagen).pack()

	Button = tk.Button(raiz, text = "Close Window", command = raiz.destroy)
	Button.config(fg = "#fa7704")
	Button.place(x = 20, y = 20)

	raiz.mainloop()


GUI_Creation()



BirdGue = BirdGuess_chinese_k[index]


x = 0

hits = 0

diamonds = 0

coins = 0 

lifes = 5

End = False



def Juego():

	global x 
	global hits

	while x <= len(BirdGue) - 1:

		answer = input('Enter birds chinese character: ')

		if answer == BirdGue[x]:

			print('Hit!!')
			hits = hits + 1

		else:

			print('Wrong!')

		x = x + 1

print(BirdGue)
print(BirdGuess_pinyin[index])

Juego()


while End == False or lifes > 0:

	if hits == len(BirdGue):

		print('Congratulations!!!!')
		time.sleep(5)

		del BirdGuess_list_k[index]
		del BirdGuess_english_k[index]
		del BirdGuess_chinese_k[index]
		diamonds = diamonds + 1
		coins = coins + 1
		IndexCreation()
		GUI_Creation()
		time.sleep(2)
		x = 0
		hits = 0
		Juego()


	elif hits >= len(BirdGue) / 2 and hits < len(BirdGue):

		print('Pasa')
		coins = coins + 1
		IndexCreation()
		GUI_Creation()
		time.sleep(2)
		x = 0
		hits = 0
		Juego()


	elif hits < len(BirdGue) / 2:
		print('No')
		lifes = lifes - 1
		IndexCreation()
		GUI_Creation()
		time.sleep(2)
		x = 0
		hits = 0
		Juego()

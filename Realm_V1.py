print()
print()
print()
print()

print(' ------------------------------------------------  WELCOME TO REALM VERSION 1 ------------------------------------------------------------------')





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

from playsound import playsound  # --- Audio reproduction in Python


BirdGuess_list_k = BirdGuess_list

BirdGuess_sci_k = BirdGuess_sci

BirdGuess_Spanish_k = BirdGuess_Spanish

BirdGuess_english_k = BirdGuess_english

BirdGuess_french_k = BirdGuess_french

BirdGuess_german_k = BirdGuess_german

BirdGuess_chinese_k = BirdGuess_chinese

BirdGuess_pinyin_k = BirdGuess_pinyin

print()
print()
print()


print('                                                           WELCOME TO REALM              ')
print()
print('                                 A SERIOUS GAME TO GUESS THE COLOMBIAN BIRDS NAMES IN MANDARIN CHINESE')
print()               
print('                                                     	CHARACTER BY CHARACTER ')
print()
print()
print()
print('                                                         So, lets give it a try ')

print()
print()
print()
print('    -----------------------------------------------------------------------------------------------------------------------------------------------')







time.sleep(2)

welcome = 'Welcome.mp3'

caracara = 'Caracara chimachima.wav'

playsound(caracara)

time.sleep(5)

playsound(welcome)

index = 890
y = [0, 18, 84, 85]
z = 0



def IndexCreation():

	global index
	global y 
	global z

	if z < len(y):
		index = y[z]
		#z = z + 1
		del y[z]

	elif z == len(y):
		print('fin')

	 
	#index = random.randint(0, len(BirdGuess_list_k) - 1)

	#index = random.randint(0, 5)
	

IndexCreation()


def GUI_Creation():

	global y 

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

hit_sound = 'Hit.wav'
wrong_sound = 'wrong.mp3'
congratulations_message = 'Congratulations.mp3'
diamond_message = 'Diamond.mp3'

def Juego():

	global x 
	global hits
	global BirdGue

	BirdGue = BirdGuess_chinese_k[index]



	while x <= len(BirdGue) - 1:

		print()
		answer = input('Enter birds chinese character: ')

		if answer == BirdGue[x]:

			print()
			playsound(hit_sound)

			print('Hit!!')
			hits = hits + 1

		else:

			print()
			playsound(wrong_sound)
			print('Wrong!')

		x = x + 1

print()
print()

print(BirdGue)
print(BirdGuess_pinyin[index])

Juego()


# ---------------------------------------- Badges --------------------------------------------------------------


def diamond():

	def Close():

		root_diamond.destroy()



	root_diamond = tk.Tk()

	root_diamond.title("Badge: Diamond")

	root_diamond.geometry("600x400")

	root_diamond.iconbitmap()

	miFrame_diamond = Frame(root_diamond)

	miFrame_diamond.pack()

	miImage_diamond = PhotoImage(file = "Diamond_image_v4.png")

	Label(miFrame_diamond, image = miImage_diamond).pack()

	

	CloseWindow = tk.Button(root_diamond, text = "Understood", font = ("Comic Sans MS", 13), command = lambda:Close())
	CloseWindow.config(fg = "#0f10be")
	CloseWindow.place(x = 450, y = 300)
		
	root_diamond.mainloop()



while End == False and lifes > 0:

	if len(y) == 0:

		print()
		print('End of the game')
		End == True
		break

	elif hits == len(BirdGue):

		print()
		print('Congratulations. You have won a Diamond !!!!')
		print()
		print()
		time.sleep(2)
		playsound(congratulations_message)
		time.sleep(1)
		playsound(diamond_message)
		time.sleep(2)
		diamond()

		del BirdGuess_list_k[index]
		del BirdGuess_english_k[index]
		del BirdGuess_chinese_k[index]
		del BirdGuess_pinyin_k[index]
		diamonds = diamonds + 1
		coins = coins + 1
		IndexCreation()
		GUI_Creation()
		#time.sleep(2)
		x = 0
		hits = 0
		Juego()


	elif hits >= len(BirdGue) / 2 and hits < len(BirdGue):

		print()
		print('You have won a coin !!!!!!')
		print()
		del BirdGuess_list_k[index]
		del BirdGuess_english_k[index]
		del BirdGuess_chinese_k[index]
		del BirdGuess_pinyin_k[index]
		coins = coins + 1
		time.sleep(4)
		IndexCreation()
		GUI_Creation()
		#time.sleep(2)
		x = 0
		hits = 0
		Juego()


	elif hits < len(BirdGue) / 2:

		print()
		print('You have lost one life')
		print()
		del BirdGuess_list_k[index]
		del BirdGuess_english_k[index]
		del BirdGuess_chinese_k[index]
		del BirdGuess_pinyin_k[index]
		lifes = lifes - 1
		time.sleep(4)
		IndexCreation()
		GUI_Creation()
		#time.sleep(2)
		x = 0
		hits = 0
		Juego()

	

	



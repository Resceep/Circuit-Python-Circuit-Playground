import time
import board
import neopixel
from random import randint

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.fill((0,0,0))

user_input = input("Enter a number from 1- 10\n")

try:
    user_input = int(user_input) 
    if 1 <= user_input <= 10:
        print("This is definitely a number")
    else:
        print("You entered a number too high or too low\nPlease run the program again")
        quit()
except:
    print("You did not follow instructions\nPlease run the program again")
    

pixels[user_input - 1] = (0,255,0)
print("Your neopixel is highlighted in green, at neopixel",user_input,"\nYou think I can capture your neopixel?")
user_input = user_input - 1
time.sleep(2)




time.sleep(1)
print("Starting Game")
time.sleep(1)

loop_count = 0
while loop_count <= 4:
    random_number = randint(1,10)
    if random_number == user_input:
        print("Capturing neopixel ",random_number)
        print("I captured your neopixel")
        time.sleep(0.5)
        pixels[user_input] = (0,0,255)
        time.sleep(0.5)
        break
    else:
        print("Capturing neopixel ",random_number)
        time.sleep(0.5)
        pixels[random_number - 1] = (255,0,0)
        time.sleep(0.5)
        loop_count += 1
if loop_count < 5:
    print("The computer emerges victorious")
else:
    print("The user emerges victorious")
        
        

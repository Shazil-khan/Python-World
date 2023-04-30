# random numbers generate
# dynamically drawing patterns using loops
# draw pattern 
# make dice function
# making patterns
import random
import os
import time

def roll_dice():
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    if dice_one==1:
        print('\t _________')
        print('\t|         |')  
        print('\t|    O    |') 
        print('\t|_________|')
               
    elif dice_one==2:
        print('\t _________')
        print('\t|         |')  
        print('\t|  O   O  |') 
        print('\t|_________|') 
               
    elif dice_one==3:
        print('\t _________')
        print('\t|  O   O  |') 
        print('\t|         |') 
        print('\t|    O    |') 
        print('\t|_________|')
               
    elif dice_one==4:
        print('\t _________')
        print('\t|  O   O  |') 
        print('\t|         |')   
        print('\t|  O   O  |') 
        print('\t|_________|')
                
    elif dice_one==5:
        print('\t _________')
        print('\t| O     O |')  
        print('\t|    O    |') 
        print('\t| O     O |')
        print('\t|_________|')
                
    elif dice_one==6:
        print('\t _________')
        print('\t| O     O |')  
        print('\t| O     O |') 
        print('\t| O     O |')
        print('\t|_________|')
    if dice_two==1:
        print('\t _________')
        print('\t|         |')  
        print('\t|    O    |') 
        print('\t|_________|')
               
    elif dice_two==2:
        print('\t _________')
        print('\t|         |')  
        print('\t|  O   O  |') 
        print('\t|_________|') 
               
    elif dice_two==3:
        print('\t _________')
        print('\t|  O   O  |') 
        print('\t|         |') 
        print('\t|    O    |') 
        print('\t|_________|')
               
    elif dice_two==4:
        print('\t _________')
        print('\t|  O   O  |') 
        print('\t|         |')   
        print('\t|  O   O  |') 
        print('\t|_________|')
                
    elif dice_two==5:
        print('\t _________')
        print('\t| O     O |')  
        print('\t|    O    |') 
        print('\t| O     O |')
        print('\t|_________|')
                
    elif dice_two==6:
        print('\t _________')
        print('\t| O     O |')  
        print('\t| O     O |') 
        print('\t| O     O |')
        print('\t|_________|')
         
    print(dice_one,dice_two)
    
# simulating the dice dynamically
def dice_simulate():
    count=0
    i=0
    flag = 0
    os.system('cls')
    while True:
            if i==0:
                print(' _________')
                print('|         |')  
                print('|    O    |') 
                print('|_________|')
                time.sleep(0.08)
                count+=1
                os.system('cls')
            if i==1:
                print(' _________')
                print('|         |')  
                print('|  O   O  |') 
                print('|_________|') 
                time.sleep(0.08)
                count+=1
                os.system('cls')
            if i==2:
                print(' _________')
                print('|  O   O  |') 
                print('|         |') 
                print('|    O    |') 
                print('|_________|')
                time.sleep(0.08)
                count+=1
                os.system('cls')
            if i==3:
                print(' _________')
                print('|  O   O  |') 
                print('|         |')   
                print('|  O   O  |') 
                print('|_________|')
                time.sleep(0.08)
                count+=1
                os.system('cls')
            if i==4:
                print(' _________')
                print('| O     O |')  
                print('|    O    |') 
                print('| O     O |')
                print('|_________|')
                time.sleep(0.08)
                count+=1
                os.system('cls')
            if i==5:
                print(' _________')
                print('| O     O |')  
                print('| O     O |') 
                print('| O     O |')
                print('|_________|')
                time.sleep(0.08)
                count+=1
                os.system('cls')
                i=-1
            if count==36:
                break
            i+=1
            
dice_simulate()
roll_dice()
# -*- coding: utf-8 -*-

"""
Created on Apr 20 2020

@authors: Julia Gruber, Max Schlicher, Caroline Steiner, Jelena Zimmermann
"""

# importing survey questions to answer
import csv
import read_data

def initialize_survey():
    
    v_which_canton = read_data.which_cantons()
    v_age = input("Please enter your age: ")
    
    #Which survey do you want to take?
    while True:
        inp_survey = input("Which survey do you want to take? (A = Consumption B = Activity Level and Recovery):  ")
        if inp_survey == 'A' or inp_survey == 'B':
            break;
        else:
            print('This survey does not exist. Please enter A or B.')
    return v_which_canton, v_age, inp_survey

def take_survey(p_survey):
    v_count = 0
    v_points = 0
    #read the former chosen survey
    with open('Survey_' + p_survey + '.csv') as f:
        csv_reader = csv.reader(f)
        print('Please enter one of the following: 0 = never, 1 = rarely, 2 = sometimes, 3 = often, 4 = always')
        #skip the header row
        next(f)
        for line in csv_reader:
            v_count += 1            
            v_points += int(input('Question No. ' + str(v_count) + ': ' + line[0] + ' YOU: '))
    return v_points

def final_result(p_points,p_canton):
    print(p_points)
    if p_points>16:
        print("            ____O         __O                    ")
        print("            _`___\-'      / /\_,               | ")
        print("           (')\/(`)     ___/\                  | ")
        print("                            /_                 | ")
        print("         --------------------------------------  ")
        print("")
        print("You're doing a great job. Keep going!")
    else:
        print("+---------------------------------------------------------+")
        print("|                                                         |")
        print("|  o   \ o /  _ o         __+    \ /     +__        o _   |")
        print("| /+\    +     /\   ___\o   \o    +    o/    o/__   /\    |")
        print("| / \   / \   + \  /)  +    ( \  /o\  / )    +  (\  / +   |")
        print("|                                                         |")
        print("+---------------------------------------------------------+")
        print("")
        print("A doctor might be a good choice. Here are some recommendations for you: ")
        #oh oh, not good. Therefore show doctors from this canton
        print(read_data.get_doctors(p_canton))
    return

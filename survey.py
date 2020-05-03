# importing survey questions to answer
import csv
import read_data

def initialize_survey():
    v_age = 0
    v_which_canton = read_data.which_cantons()
    while True:
        try:
            v_age = input("Please enter your age: ")
            if int(v_age) > 0:
                break;
            else:
                print('This does not seem to be a reasonable age')
        except:
            print("Please enter a valid age!")    
            
    #Which survey do you want to take?
    while True:
        inp_survey = input("Which survey do you want to take? (A = Consumption B = Activity Level and Recovery):  ").upper()
        if inp_survey == 'A' or inp_survey == 'B':
            break;
        else:
            print("This survey does not exist. Please enter A or B.")
    return v_which_canton, v_age, inp_survey

def take_survey(p_survey):
    v_count = 0
    v_points = 0
    #read the former chosen survey
    with open('Survey_' + p_survey + '.csv') as f:
        csv_reader = csv.reader(f)
        print("")
        print("Please enter one of the following: 0 = never, 1 = rarely, 2 = sometimes, 3 = often, 4 = always")
        print("")
        #skip the header row
        next(f)
        for line in csv_reader:
            v_count += 1
            while True:
                try:
                    v_chosen_points = int(input('Question No. ' + str(v_count) + ': ' + line[0] + ' YOU: '))
                    if int(v_chosen_points) in range(0, 5):
                        v_points += v_chosen_points
                        break;
                    else:
                        print('Please try again. Enter a number between 0-4')
                except:
                    print("You did not enter a number. Please enter 0-4")   
    return v_points

def final_result(p_points,p_canton):
    print("")
    print("")
    print("Your overall points are: " + str(p_points))
    print("")
    print("")
    if p_points>30:
        print("")
        print("           ___________                ")
        print("          '._==_==_=_.'               ")
        print("          .-\:      /-.               ")
        print("         | (|:.     |) |              ")
        print("          '-|:.     |-'               ")
        print("            \::.    /                 ")
        print("             '::. .'                  ")
        print("               ) (                    ")
        print("             _.'_'._                  ")
        print("")
        print("")
        print("Excellent! Your're well on your way to the next Olympic Games!")
    elif p_points>24:
        print("")
        print("            ____O         __O                    ")
        print("            _`___\-'      / /\_,               | ")
        print("           (')\/(`)     ___/\                  | ")
        print("                            /_                 | ")
        print("         --------------------------------------  ")
        print("")
        print("")
        print("You're doing a great job. Keep going and stay healthy!")
    elif p_points>16:
        print("")
        print("+---------------------------------------------------------+")
        print("|                                                         |")
        print("|  o   \ o /  _ o         __+    \ /     +__        o _   |")
        print("| /+\    +     /\   ___\o   \o    +    o/    o/__   /\    |")
        print("| / \   / \   + \  /)  +    ( \  /o\  / )    +  (\  / +   |")
        print("|                                                         |")
        print("+---------------------------------------------------------+")
        print("")
        print("")
        print("You laid the fundations. Now you can really get started!")
        print("")
        print("Keep pushing and further improve your fitness with regular exercises!")
    else:
        print("")       
        print("       ,'--.             ")
        print("       )  ,|             ")
        print("      /  /,'-.           ")
        print("     /  //  /.`.         ")
        print("   ,'  //  /  `.`.       ")
        print("  (    )--.`.   //|      ")
        print("  |`--'|   `.`.// |      ")
        print("   `--'      `./ /       ")
        print("     |_________|/        ")
        print("")
        print("")
        print("Your results show potential for improvement.")
        print("")
        print("We recommend that you have a medical checkup and develop a suitable training plan with a doctor.")
        print("")
        print("Here are some recommendations for you: ")
        print("")
        #oh oh, not good. Therefore show doctors from this canton
        print(read_data.get_doctors(p_canton))
    return

#importing survey questions to answer
import csv
import read_data

def initialize_survey():
    #initialize variables
    v_age = 0
    #call another function to print a list of cantons
    v_which_canton = read_data.which_cantons()
    #break on purpose, stay in the loop until a valid age has been entered
    while True:
        try:
            v_age = input("Please enter your age: ")
            #people with the age of zero shouldn't participate
            if int(v_age) > 5:
                break;
            else:
                print("This does not seem to be a reasonable age.")
        except:
            print("Please enter a valid age!")  
    #enter a gender
    #user can type in upper or lower case
    while True:
        v_gender = input("Please enter your gender. \nM = Male | F = Female:  ").upper()
        if v_gender == 'M' or v_gender == 'F':
            break;
        else:
            print("This gender is not defined. Please enter M or F.")          
    
    #lets user decide which survey he wants to take
    #user can type in upper or lower case
    while True:
        inp_survey = input("Which survey do you want to take? \nA = Consumption | B = Activity Level and Recovery:  ").upper()
        if inp_survey == 'A' or inp_survey == 'B':
            break;
        else:
            print("This survey does not exist. Please enter A or B.")
    return v_which_canton, v_age, v_gender, inp_survey

def take_survey(p_survey):
    v_count = 0
    v_points = 0
    #read the previously chosen survey
    with open('Survey_' + p_survey + '.csv') as f:
        csv_reader = csv.reader(f)
        print("")
        print("Please enter one of the following: \n0 = never | 1 = rarely | 2 = sometimes | 3 = often | 4 = always")
        print("")
        #skip the header row
        next(f)
        for line in csv_reader:
            #question one should be called "1", instead of 0. python starts counting with 0 normally
            v_count += 1
            while True:
                try:
                    v_chosen_points = int(input("Question No. " + str(v_count) + ": " + line[0] + " \n -->  "))
                    #we are looking for answers with either 1,2,3,4
                    if int(v_chosen_points) in range(0, 5):
                        v_points += v_chosen_points
                        break;
                    else:
                        print("Please try again. Enter a number between 0-4.")
                except:
                    print("You did not enter a number. Please enter 0-4.")   
    return v_points

def final_result(p_points,p_canton):
    print("")
    print("")
    print("Your overall points are: " + str(p_points))
    print("")
    print("")
    #everything looks fine, healthy
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
    #still ok in terms of health
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
    #you should practise more
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
        print("You laid the foundations. Now you can really get started!")
        print("")
        print("Keep pushing and further improve your fitness with regular exercises!")
    #not healthy at all, call a doctor
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


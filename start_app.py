#for installing missing modules
import import_modules

#calls to survey.py due to: initialization, survey taking, 
#   evaluation of results 
import survey

#contains a tuple, consisting of (v_which_canton, v_age, inp_survey)
global inp_survey

# (0) install potential missing modules
import_modules.auto_install()


# (1) Welcome to Sporty-Healthy Checker
#   http://asciiflow.com/ has been used to create the ascii-pics

print("")
print("")
print("")
print("         Welcome to the Health Check App")
print("           Get healthy, STAY HEALTHY")
print("")
print("                   ,++./,+.")
print("                  / #      \ ")
print("                 +          +")
print("                  \        /")
print("                   `._,._,'")
print("")
print("")
print("+------------------------------------------------------+")
print("| EXPLANATION                                          |")
print("| * You will be able to choose from different surveys  |")
print("| * We just need your age and the canton you live in   |")
print("|                                                      |")
print("| --> Based on the result you will be given advice <-- |")
print("|                                                      |")
print("+------------------------------------------------------+")
print("")      
input("Let us start the survey. Hit any key. ")


# (2) Initialize the survey with details about the participant as well
#   as the choice of survey
inp_survey = survey.initialize_survey()

# (3) Perform the actual survey. Question by question.
#   Parameter "inp_survey[2]" stands for the survey which has been chosen
write_points = survey.take_survey(inp_survey[2])

# (4) Show the grade, healthy or suggestion for medical support.
#   In case the health result is poor, doctor suggestions from the appropriate
#   canton are being shown.
#   Parameter "inp_survey[0]" stands for the participants' canton
survey.final_result(write_points,inp_survey[0])


# (5) Survey results are being written persistantly into a file
#   calls to results.py due to: writing the results into a file, 
#   creating diagrams for the participants
import results
#   Parameter "inp_survey[0]" = canton, "inp_survey[1]" = age of 
#   the participant, "inp_survey[2]" = Survey taken
#   write_point = amount of points accumulated in this survey
results.write_survey_results(inp_survey[0],inp_survey[1],inp_survey[2],write_points)

# (6) Plot statistical results via diagrams
results.create_diagrams()

# HSG_Health-Check

With this program, a user can check her health score in two different surveys. 
Depending on the survey chosen, the inputs are then categorized and the user gets an answer-based result.
Besides collecting information for further analysis, the personal feedback also creates valuable insight for the user and based on her final score, she will receive a list of doctors in the canton she lives in.   
The diagrams shown at the end gives the user a quick insight into the survey and provides her with an overview about the most relevant statistics.

Roadmap:
 1. __start_app.py:__ general code that imports the functionalities written in other files
 2. import_modules.py: squarify is being installed automatically, if it does not yet exist - 
    (squarify is necessary for creating a treemap diagram)
 3. read_data.py: reads the data from external website + internal csv file
 4. survey.py: performs the survey + gives the final score
 5. results.py: stores the final score to a csv + creates diagrams

Technical functionality:
 - Automatic installation of necessary "squarify" package
 - Make use of different python packages (pandas, matplotlib)
 - Read data from an external website (cantons) - read html table data and format via panda dataframes
 - Data selection via panda
 - Write results into an external csv file
 - Diagrams based on results file via panda
 - Read data from csv file and selection criteria (based on cantons)
 - Exception handling
 - Use ascii visualization
 - Separated code into more files for independent working and developing of features (functionality based)

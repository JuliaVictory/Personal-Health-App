# pandas is being used for dataframes (loading all data from survey results)
import pandas

# matplotlib is neccesary for creating statistical diagrams based on former surveys
import matplotlib.pyplot as plt

# squarify is necessary for creating a treemap diagram
import squarify as sq

def write_survey_results(p_canton, p_age, p_gender, p_survey, p_points):
    #Write results of a taken survey
    df_write = pandas.DataFrame({'\n\nSurvey': [p_survey],
                       'Canton': [p_canton],
                       'Age': [p_age],
                       'Gender': [p_gender],
                       'Points': [p_points]})
    df_write.to_csv('survey_results.csv', mode='a', header=False,index=False)
    return

def create_diagrams():
    survey_results = pandas.read_csv('survey_results.csv')
    
    print("")
    print("")
    print("Additionally, you'll find some diagrams about the survey you've just participated in.")
    print("")
    
# (1) Create a histogram of the age of all the users that have taken the survey so far
    plt.hist(
    
        # using age
        survey_results['Age'],     
        # plotting it by age ranges
        bins=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100),     
        # with width
        rwidth=0.9,     
        # with color
        color='blue')

    # Set labels
    plt.ylabel('Number of People')
    plt.xlabel('Age')
    plt.title('Age Distribution')

    # View the plot
    plt.show()
        

# (2) Create a treemap to show distribution based on the cantons the users live in
    # Showing distribution of cantons
    # sum the instances of cantons
    survey_results_grouped = survey_results.groupby("Canton", as_index=False)["Points"].sum()
    sq.plot(sizes=survey_results_grouped['Points'], label=survey_results_grouped['Canton'], alpha=.8 )
    # Hiding axis
    plt.axis('off')
    # Set labels
    plt.title("Cantons points gained")
    # View the plot
    plt.show()


    
    return

# pandas is being used for dataframes (loading all data from survey results)
import pandas

# matplotlib is neccesary for creating statistical diagrams based on former surveys
import matplotlib.pyplot as plt

# squarify is necessary for creating a treemap diagram
import squarify as sq

def write_survey_results(p_canton, p_age, p_survey, p_points):
    #Write results of a taken survey
    df_write = pandas.DataFrame({'\n\nSurvey': [p_survey],
                       'Canton': [p_canton],
                       'Age': [p_age],
                       'Points': [p_points]})
    df_write.to_csv('survey_results.csv', mode='a', header=False,index=False)
    return

def create_diagrams():
    survey_results = pandas.read_csv('survey_results.csv')
    
    print("")
    print("")
    print("Additionally, you'll find some diagrams about the survey you've just participated in.")
    print("")
    
# part 1 - Create histogram 
    plt.hist(
    
        #using Age
        survey_results['Age'],     
        #plotting it by age ranges
        bins=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100),     
        #with width
        rwidth=0.9,     
        #with color
        color='blue')

    #Set labels
    plt.ylabel('Number of People')
    plt.xlabel('Age')
    plt.title('Age Distribution')

    #View the plot
    plt.show()
        

# part 2 - Creating a treemap to show distribution 
    # Showing distribution of cantons
    # sum the instances of cantons
    survey_results_grouped = survey_results.groupby("Canton", as_index=False)["Points"].sum()
    sq.plot(sizes=survey_results_grouped['Points'], label=survey_results_grouped['Canton'], alpha=.8 )
    # Hiding axis
    plt.axis('off')
    # Set labels
    plt.title("Cantons points gained")
    #View the plot
    plt.show()

# part 3 - piechart 
    #grouped by surveys, build the sum
    results_by_survey = survey_results.groupby("Survey", as_index=False)["Points"].sum()
    # sum the instances of A (position 0) and B (position 1)
    A_results = results_by_survey.loc[0,"Points"]
    B_results = results_by_survey.loc[1,"Points"]
    # put them into a list called proportions
    proportions = [A_results, B_results]    

    plt.pie(
        # using proportions
        proportions,

        # with the labels being names
        labels = ['Survey A', 'Survey B'],

        # with no shadows
        shadow = False,

        # with colors
        colors = ['blue','red'],

        # with one slide exploded out
        explode = (0.15 , 0),

        # with the start angle at 90%
        startangle = 90,

        # with the percent listed as a fraction
        autopct = '%1.1f%%'
        )

    # View the plot drop above
    plt.axis('equal')
    # Set labels
    plt.title("Points achieved in both surveys")
    # View the plot
    plt.tight_layout()
    plt.show()
    
    return
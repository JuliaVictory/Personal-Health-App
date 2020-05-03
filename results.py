# pandas is being used for dataframes (loading all data from survey results)
import pandas

# matplotlib is neccesary for creating statistical diagrams based on former surveys
import matplotlib.pyplot as plt

# squarify is necessary for creating a treemap diagram
import squarify as sq

def write_survey_results(p_canton, p_age, p_survey, p_points):
    #Write results of a taken survey
    df_write = pandas.DataFrame({'\n\nSurvey': [p_survey],
                       'Kanton': [p_canton],
                       'Age': [p_age],
                       'Points': [p_points]})
    df_write.to_csv('survey_results.csv', mode='a', header=False,index=False)
    return

def create_diagrams():
    survey_results = pandas.read_csv('survey_results.csv')
    # sum the instances of A and B
    A_results = (survey_results['Survey'] == 'A').sum()
    B_results = (survey_results['Survey'] == 'B').sum()
    # put them into a list called proportions
    proportions = [A_results, B_results]

    print("")
    print("")
    print("Below you'll find some background information about the survey you've just participated in.")
    print("")
    
        #Create histogram 
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
    
    print("")
    print("")
    print("")

    # Showing distribution of cantons
    # Reading the csv file
    survey_results = pandas.read_csv('survey_results.csv')
    # sum the instances of cantons
    AG_results = (survey_results['Kanton'] == 'AG').sum()
    AI_results = (survey_results['Kanton'] == 'AI').sum()
    AR_results = (survey_results['Kanton'] == 'AR').sum()
    BL_results = (survey_results['Kanton'] == 'BL').sum()
    BS_results = (survey_results['Kanton'] == 'BS').sum()
    BE_results = (survey_results['Kanton'] == 'BE').sum()
    FR_results = (survey_results['Kanton'] == 'FR').sum()
    GE_results = (survey_results['Kanton'] == 'GE').sum()
    GL_results = (survey_results['Kanton'] == 'GL').sum()
    GR_results = (survey_results['Kanton'] == 'GR').sum()
    JU_results = (survey_results['Kanton'] == 'JU').sum()
    LU_results = (survey_results['Kanton'] == 'LU').sum()
    NE_results = (survey_results['Kanton'] == 'NE').sum()
    NW_results = (survey_results['Kanton'] == 'NW').sum()
    OW_results = (survey_results['Kanton'] == 'OW').sum()
    SG_results = (survey_results['Kanton'] == 'SG').sum()
    SH_results = (survey_results['Kanton'] == 'SH').sum()
    SO_results = (survey_results['Kanton'] == 'SO').sum()
    SZ_results = (survey_results['Kanton'] == 'SZ').sum()
    TG_results = (survey_results['Kanton'] == 'TG').sum()
    TI_results = (survey_results['Kanton'] == 'TI').sum()
    UR_results = (survey_results['Kanton'] == 'UR').sum()
    VD_results = (survey_results['Kanton'] == 'VD').sum()
    VS_results = (survey_results['Kanton'] == 'VS').sum()
    ZG_results = (survey_results['Kanton'] == 'ZH').sum()
    ZH_results = (survey_results['Kanton'] == 'ZG').sum()
    # put them into a list called cantons
    cantons_results = [['AG', AG_results],['AI', AI_results],['AR', AR_results],['BL', BL_results],['BS', BS_results], ['BE', BE_results], ['FR', FR_results], ['GE', GE_results], ['GL', GL_results], ['GR', GR_results], ['JU', JU_results], ['LU', LU_results], ['NE', NE_results], ['NW', NW_results], ['OW', OW_results], ['SG', SG_results], ['SH', SH_results], ['SO', SO_results], ['SZ', SZ_results], ['TG', TG_results], ['TI', TI_results], ['UR', UR_results], ['VD', VD_results], ['VS', VS_results], ['ZG', ZG_results], ['ZH', ZH_results]]

    # Creating a new dataframe cantons_table
    cantons_table = pandas.DataFrame(cantons_results, columns = ['Canton', 'Instances'])

    # Creating dataframe with cantons instances > 0
    cantons_data = cantons_table[cantons_table["Instances"]>0]

    # Creating a treemap to show distribution 
    sq.plot(sizes=cantons_data['Instances'], label=cantons_data['Canton'], alpha=.7)
    # Hiding axis
    plt.axis('off')
    # Set labels
    plt.title("Cantons participated")
    #View the plot
    plt.show()

    print("")
    print("")
    print("")
    
            # Create a pie chart
    plt.pie(
        # using proportions
        proportions,

        # with the labels being officer names
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
    
    
    # Plotting the age distribution
    # Read the data from csv file
    survey_results = pandas.read_csv('survey_results.csv', sep=',')
    
    return
 

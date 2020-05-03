def which_cantons():
    #needed for showing the list of cantons
    import pandas as pd
    #short sign for canton will be used throughout the program
    v_abk_canton = ""
    
    #get all cantons online. You never know when they will change ;-)
    #read_html > reads html tables and puts it in a variable
    tables = pd.read_html("http://kantone-staedte.infos-schweiz.ch/")

    #for formatting purposes we convert the canton-list into a panda
    #   dataframe
    df = tables[2]
    #only canton short sign and the canton name are being needed
    df = df.drop(df.columns[[0,3,4,5,6,7,8]], axis=1)

    #Start index counting at 1 to let participants choose an appropriate number
    df.index += 1 
    #show all cantons from the online list (except the last line,
    #  it will show the sum of all cantons)
    print(df.head(int(len(df)-1)))
    while True:
        try:
            inp_canton = input("Which canton are you from? Please enter a number from the list: ")
            #we choose "len(df)-1" to dynamically increase the number
            #in case there will be more cantons in future
            if int(inp_canton) in range(0, len(df)):
                #short name canton will be returned
                v_abk_canton = df.loc[int(inp_canton),"Abk"]
                break;
            else:
                print('This canton does not exist')
        except:
            #we choose "len(df)-1" as the maximum amount of cantons,
            #in case the number of cantons will change in future
            print("Please enter a canton no. between 1-"+str(len(df)-1))    
    return v_abk_canton

def get_doctors(p_canton):
    import pandas as pd
    return_value = ''
    survey_results = pd.read_csv('doctors_list.csv')
    return_value = survey_results.loc[survey_results['Canton'] == p_canton].to_string(index=False)
    if survey_results.loc[survey_results['Canton'] == p_canton].empty == True:
        return_value = 'There does not seem to be any doctor in your canton!'
    return return_value

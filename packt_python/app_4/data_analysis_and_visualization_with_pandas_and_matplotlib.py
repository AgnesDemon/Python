#For Jupyter notebook, type Ctrl + Enter to execute code on Windows.
#This will execute code without creating a new box.
#Shift + Enter will execute code and create a new box.
#Note: had to install matplotlib by using pip install.
#In Jupyter Notebook, sometimes you have to run all of the cells (the boxes) again for it to work.
#You can do this quickly by clicking Run and selecting Run All Cells.
#You can create a new cell above all of the other cells by pressing A and then pressing M - just make sure you don't have any of the cells selected.
#This should allow you to create a title if you type in 2 #s in the cell.
#If you type 3 #s, then the font will be smaller.
#You can also create a markdown cell by making sure nothing is selected and pressing M.
#This should create a markdown cell, and you can do the same thing as you did with the title.
#NOTE: BE SURE TO PUT A SPACE BETWEEN THE #S WHEN YOU CREATE A MARKDOWN CELL, OTHERWISE IT WILL NOT CREATE A TITLE.
#Series represent single columns.
#Dataframes represent more than one column.
#To undo, type Ctrl + Z.


#data["Day"] = data["Timestamp"].dt.date
#data.head()
#day_average = data.groupby(["Timestamp"])
#day_average.head()
#Prints out chart, but groupby seems to mess up on printing only the head

#data['Day'] = data['Timestamp'].dt.date
#day_avg = data.groupby(["Course Name"]).mean()
#day_avg
#Constantly has an error due to groupby, no matter which column name I put

#data["Day"] = data["Timestamp"].dt.date creates a new column that shows the date in this format: Y-M-D
#You can also create a Month and Year column with the same code.
#Just switch "Day" with "Week" or "Month".
#Also, switch .date for .strftime("%-%").
#For Week, put either ("%Y-%U") or ("%m-%U") - the first one is for more data, while the second one is for less data.
#For Month, put ("%Y-%m").

#To make the rest of the code work, the columns Course Name, Comment, and Timestamp need to be removed, or "dropped".
#This will not only allow the code to work, but it will create a chart with just Rating and Day, just like the instructor's.
#Therefore, in order for day_average = data.groupby(["Day"]).mean() to work, the other columns need to be dropped.
#The Timestamp column can work as well, but the instructor only wanted the Rating and Day columns.
#You can drop more than one column by doing this: data.drop(["Column A", "Column B"], axis=1)


#132 is the line I left off of in reviews.csv

#I AM TYRPING THIS DOWN HERE BECAUSE I KNOW THAT IT WILL NOT WORK IN JUPYTER NOTEBOOK
#I WILL TRY TO MIMIC IT IN MY OWN WAY, EVEN IF IT TAKES LONGER
#What day are people the happiest?
    #data - SHOWS DATA FROM reviews.csv
    #data["Weekday"] = data["Timestamp"].dt.strftime("%A") - CREATES A NEW COLUMN WITH THE DAYS OF THE WEEK (SUN-SAT)
    #data["Daynumber"] = data["Timestamp"].dt.strftime("%w") - CREATES A NEW COLUMN WITH THE DAYS OF THE WEEK AS NUMNERS (MON = 1, TUE = 2, ETC)
    #data - SHOWS THE UPDATED DATA WITH NEW COLUMN
    #weekday_average = data.groupby(["Weekday"]).mean() - GROUPS THE RATING AND WEEKDAY COLUMNS TOGETHER AND THEIR AVERAGE
    #HOWEVER, THERE IS A PROBLEM WITH THIS LINE - IT PRINTS THE DAYS OF THE WEEK IN ALPHABETICAL ORDER, SO LIKE THIS: FRI, MON, SAT, SUN, THURS, TUES, WED
    #weekday_average = weekday_average.sort_values("Weekday") - SUPPOSED TO ORGANIZE THE WEEKDAYS IN THEIR ORIGINAL ORDER, BUT STILL IN ALPHABETICAL ORDER
    #TO FIX THIS, USE THIS CODE:
        #weekday_average = data.groupby(["Weekday", "Daynumber"]).mean()
        #weekday_average = weekday_average.sort_values("Daynumber")
    #plt.figure(figsize = [15, 3]) - SETS THE SIZE OF THE GRAPH
    #plt.plot(weekday_average.index, weekday_average["Rating"]) - CREATES A GRAPH WITH THE DAYS OF THE WEEK AS THE X-AXIS AND THE RATING AS THE Y-AXIS
    #HOWEVER, ANOTHER ERROR OCCURS BECAUSE A TUPLE IS GIVEN INSTEAD OF A STRING OR BYTE
    #TO FIX THIS, USE THIS CODE INSTEAD FOR THE GRAPH:
        #plt.plot(weekday_average.index.get_level_values(0), weekday_average["Rating"])
        #.get_level_values(0) ONLY USES THE WEEKDAY COLUMN, THAT WAY THERE IS NO TUPLE TO CONFUSE THE GRAPH
    #TO ACCESS DIFFERENT TYPES OF GRAPHS, TYPE dir(plt), WHICH SHOULD SHOW YOU THE OTHER GRAPHS THAT YOU CAN USE FOR YOUR DATA
    #NOTE: NOT ALL GRAPHS OR CHARTS ARE APPROPRIATE FOR SPECIFIC TYPES OF DATA, SO AT TIMES YOU MAY GET AN ERROR
    #TO LEARN A BIT MORE ABOUT THE GRAPH OR CHART THAT YOU ARE USING, TYPE help(plt.plot) OR WHATEVER GRAPH/CHART METHOD YOU ARE USING


#Need to test this out:
#share = data.groupby(["Course Name"])["Rating"].count()
#share
#plt.pie(share, labels = share.index)



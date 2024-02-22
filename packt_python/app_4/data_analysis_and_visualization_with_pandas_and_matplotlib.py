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


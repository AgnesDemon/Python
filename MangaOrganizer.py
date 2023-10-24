#Should be able to log in
#Should be able to create folders for different manga series
#Should be able to add and store new manga into files
#Should organize manga in order by volume
#Should be able to see the files
#Maybe delete files or manga
#Make sure I cannot make duplicates. This means that the manga can have the same name, but not the same volume number

import os

#This just reads the file
'''manga_file = open("all_manga.txt")
print(manga_file.read())
print("\n")'''

#This opens, appends, resets the cursor, closes, and prints the text file
with open("all_manga.txt", "a+") as manga_file:
    manga_file.write("\nAttack On Titan")
    manga_file.seek(0)
    content = manga_file.read()
    
print(content)


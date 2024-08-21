#Web Scraping with Python and Beautiful Soup
#on a webpage, if you right click and select "Inspect", you can see the html code
#pythonhow.com
#"jupyter notebook" to open Jupyter in terminal
    #Alt + Enter to run code and go to next line

#webpage used for this assignment no longer exists, but here's some notes to get an idea of what everything does:
    #"request = requests.get("link_here")" gets the link that you are going to use for this assignment
    #"content = request.content" shows what is in the webpage. You can also see what is in a webpage by using "Inspect"
    #"type(content)" tells you what the content is. In my case, it was bytes
    #"soup = BeautifulSoup(content, "html.parser")" specifies the parser that you want to use for parsing the data, which is usually html.parser
    #"print(soup.prettify())" works similarly to "Inspect", so you usually don't have to use this
    #"all = soup.find_all("div", {"class" : "name of class(vector?)"})" finds the html code related to the specified div class and prints it as a list
    #"all2 = soup.find("div", {"class" : "name of class(vector?)"})" finds the code but does not print it as a list
    #"all[0]" you can use list indexing to find code
    #if you only want the h2 tags (using his webpage), you would type "all[0].find_all("h2")"
    #"all[0].find_all("h2")[0]" prints the h2 tags but without the brackets
    #"all[0].find_all("h2")[0].text" prints the name in the h2 tags
    #to extract the other headers:
        #"for item in all:"
            #"print(item.find_all("h2")[0].text)"
        #this will extract the other headers without the h2 tags or brackets


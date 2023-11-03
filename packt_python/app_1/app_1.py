#APP 1: WEB MAPPING WITH PYTHON: INTERACTIVE MAPPING OF POPULATION AND VOLCANOES

#SAVING MAP AS AN HTML FILE
#Latitude: goes from -90 to 90
#Longitude: goes from -180 to 180
#To run folium in the Python interactive shell, be sure to import it first
#'dir(folium) shows you all of the available functions in the folium library
#You can get out of help by pressing q (quit)
#'map = folium.Map(location=[80, -100])' sets coordinates on a map
#Be sure to save this with 'map.save("Map1.html")'
#A file should be created as a result of saving and running the map.save called 'Map1.html'
#To access the map on this computer, go to files, go to This PC, go into OS, go into the Coding folder, go to Python and open the Map
#You can override the map with the same code but different coordinates
#You can use Google Maps to find coordinates of specific places
#You can also zoom in the map with 'map = folium.Map(location=[80, -100], zoom_start=6)'
#Save with 'map.save("Map1.html")' and open the map again
#You can also just reload the web page instead of opening a new one
#Either way, you should get a zoomed in map

#ADDING A MARKER/POINT TO A MAP
import folium
import pandas

data = pandas.read_csv("volcanoes.csv")
print(data)
print("\n")
#print(data["STATE"])
#print("\n")

lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])
#name = list(data["NAME"])
elev = list(data["HEIGHT"])

def color_producer(elevation):
    #return 'red'
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="OpenStreetMap")

fg = folium.FeatureGroup(name="My Map")
'''fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Location1", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[38.7, 99.1], popup="Location2", icon=folium.Icon(color='green')))'''
#You can write this expression multiple times, just with different coordinates, to have multiple markers

#You can create a for loop to make multiple markers without having to constantly type them down
'''for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Location", icon=folium.Icon(color='green')))'''

#You can use a txt or csv file that holds the data of lat and lon to make locations on the map
for lt, ln, el in zip(lat, lon, elev):
    #both examples work
    #folium.Marker example (upside down teardrops)
    #fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+"m", icon=folium.Icon(color=color_producer(int(el)))))
    #folium.CircleMarker example (shows locations of volcanoes as circles instead of upside down teardrops)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+"m", fill_color = color_producer(el), color = 'grey', fill_opacity=0.7))
#If your popup=(parameter) is an integer, type str(parameter) to fix the error

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))
#Polygons should be displayed on the map
#I think when he says 'polygons,' I think he means the lines traced along the countries

map.add_child(fg)
#or map.add_child(folium.Marker(location=[38.2, -99.1], popup="Location1", icon=folium.Icon(color='green')))

map.save("Map1.html")




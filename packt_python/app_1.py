#APP 1: WEB MAPPING WITH PYTHON: INTERACTIVE MAPPING OF POPULATION AND VOLCANOES

#*Problem may be occuring due to lack of Leaflet, a JavaScript library to see the map
#May end up just taking notes instead of coding

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
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Location1", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[38.7, 99.1], popup="Location2", icon=folium.Icon(color='green')))
#You can write this expression multiple times, just with different coordinates, to have multiple markers

#You can create a for loop to make multiple markers without having to constantly type them down
'''for coordinates in [[38.2, -99.1], [39.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Location", icon=folium.Icon(color='green')))'''

map.add_child(fg)
#or map.add_child(folium.Marker(location=[38.2, -99.1], popup="Location1", icon=folium.Icon(color='green')))

map.save("Map1.html")



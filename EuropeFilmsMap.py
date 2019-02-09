import folium


# Basic
myMap = folium.Map(location=[48.210033, 16.363449], zoom_start=5)
dirInfo = "filminfo.txt"
mainLst = []
# Filling main array
with open(dirInfo, "r") as f:
    for line in f:
        line = line.split(",")
        temp = line[0][1:-1], float(line[1]), float(line[2]), int(line[3])
        mainLst.append(temp)
# Adding markers
fg_Markers = folium.FeatureGroup(name="Country Name and Exact num of films")
for part in mainLst:
    fg_Markers.add_child(folium.Marker(location=[part[1], part[2]],
            popup="Country: " + str(part[0]) + " | " + "Number of films: " +
                    str(part[3]), icon=folium.Icon()))
# Filling map with colored Europe Countries
fg_MapColor = folium.FeatureGroup(name="Colored num of films")
fg_MapColor.add_child(folium.GeoJson(data=open("worldEurope.json", 'r',
        encoding='utf-8-sig').read(), style_function=
                lambda x: {'fillColor': '#000000'
                    if x['properties']['FILMS'] < 20
                    else '#c300ff' if 21 <= x['properties']['FILMS'] < 100
                    else '#ff0000' if 101 <= x['properties']['FILMS'] < 1000
                    else '#eeff00' if 1001 <= x['properties']['FILMS'] < 5000
                    else '#00b211'}))
# Adding layers on a map
myMap.add_child(fg_Markers)
myMap.add_child(fg_MapColor)
myMap.add_child(folium.LayerControl())
myMap.save('EuropeFilmsMap.html')

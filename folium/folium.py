import folium
import numpy as np
from naverMapApi.reversegeocoding_naverapi import reverse_geocoding 

def create_maposm(xs, ys):
    x_c = np.median(xs)
    y_c = np.median(ys)
    map_osm = folium.Map(location=[y_c,x_c])
    return map_osm
def make_marker(map_osm, x, y):
    data = []
    for i in range(len(x)):
        data.append([str(x[i])+ ", "+str(y[i])])
        print(data)
    geoname = reverse_geocoding(data)
    for i in range(len(x)):
        folium.Marker([y[i],x[i]], tooltip=geoname[i]).add_to(map_osm)
    return map_osm

def draw_line(map_osm, point1, point2):
    location = [point1, point2]
    folium.PolyLine(locations=location, tooltip='Polyline').add_to(map_osm)
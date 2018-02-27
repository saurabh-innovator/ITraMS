import googlemaps
from datetime import datetime
import json


gmaps = googlemaps.Client(key='AIzaSyBPH6Eej16ErJTF7TLs-WC5sI9Vm9gd1VY')
print ("Enter Co-ordinates(latitude,longitude): ")
cor=input()
reverse_geocode_result = gmaps.reverse_geocode((cor))
a=reverse_geocode_result[0]
b=a['formatted_address']
print (b)

import googlemaps
from datetime import datetime
import json


gmaps = googlemaps.Client(key='AIzaSyBPH6Eej16ErJTF7TLs-WC5sI9Vm9gd1VY')

# Geocoding an address
print ("Enter Location: ")
location=input()
geocode_result = gmaps.geocode(location)
alist=geocode_result[0]
adict=alist['geometry']
bdict=adict['location']
cdict=bdict['lng']
ddict=bdict['lat']
print("longitude",cdict)
print("latitude",ddict)

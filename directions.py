import googlemaps
from datetime import datetime
import json


gmaps = googlemaps.Client(key='AIzaSyBPH6Eej16ErJTF7TLs-WC5sI9Vm9gd1VY')
print ("For directions Enter Source: ")
source=input()
print ("For directions Enter Destination: ")
dest=input()
print ("What mode of transport, like driving, walking, cycle, transit? : ")
Mode=input()
now = datetime.now()
directions_result = gmaps.directions(source,dest, mode=Mode, departure_time=now)
alist=directions_result[0]
bdict=alist['legs']
clist=bdict[0]
ddict=clist['start_address']
edict=clist['end_address']
fdict=clist['distance']
gdict=clist['duration']
print ("Starting point: ",ddict)
print ("Destination point: ",edict)
print ("Distance: ",fdict['text'])
print ("Duration: ",gdict['text'])



# importing the requests library
import requests
 
# api-endpoint
URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=28.6758058,
            77.5000373&radius=1000&type=hospital&key=AIzaSyBPH6Eej16ErJTF7TLs-WC5sI9Vm9gd1VY"
 
# location given here
#location = "delhi technological university"
 
# defining a params dict for the parameters to be sent to the API
#PARAMS = {'address':location}
 
# sending get request and saving the response as response object
r = requests.get(url = URL)
 
# extracting data in json format
data = r.json()
results=data["results"]
alist=results[0]
adict=alist["name"]
bdict=alist["vicinity"]

print ("Name: ",adict,"Adress: ",bdict)

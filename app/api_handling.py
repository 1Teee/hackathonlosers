import requests, random
from PIL import Image

us_states = [
    "alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", 
    "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", 
    "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan", 
    "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "newhampshire", 
    "newjersey", "newmexico", "newyork", "northcarolina", "northdakota", "ohio", "oklahoma", 
    "oregon", "pennsylvania", "rhodeisland", "southcarolina", "southdakota", "tennessee", 
    "texas", "utah", "vermont", "virginia", "washington", "westvirginia", "wisconsin", "wyoming"
]

def image():
    loc = getLoc()
    url = f'https://maps.googleapis.com/maps/api/streetview?size=600x300&location={loc[0]},{loc[1]}&key={getKey()}'
    response = requests.get(url)
    if response.status_code == 200:
        with open('streetview_image.jpg', 'wb') as file:
            file.write(response.content)
        print("Image successfully downloaded.")
    else:
        print(f"Error: {response.status_code}")
    image = Image.open('streetview_image.jpg')
    image.show()
    return getLoc()

def getLoc():
    locations = ['restaurant', 'park']
    loc = locations[random.randint(0, 1)]
    print(loc)
    stateCoord = getState()
    print(stateCoord)
    api = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={stateCoord[0]},{stateCoord[1]}&radius=500000&type={loc}&key={getKey()}'
    
    response = requests.get(api).json()

    if response['status'] == 'OK':
        rand_num = random.randint(0, len(response['results'])-1)
        print(response['results'][rand_num])
        lat = response['results'][rand_num]['geometry']['location']['lat']
        lng = response['results'][rand_num]['geometry']['location']['lng']
        return [lat, lng]
    else:
        print("Error fetching location details")

def getState():
    state = us_states[random.randint(0, len(us_states)-1)]
    print(state)
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={state}&key={getKey()}"

    response = requests.get(geocode_url).json()

    if response['status'] == 'OK':
        lat = response['results'][0]['geometry']['location']['lat']
        lng = response['results'][0]['geometry']['location']['lng']
        return [lat, lng]
    else:
        print("Error fetching location details")
    

def getKey():
    try:
        with open('../apikey.txt', 'r') as file:
            key = file.read()
    except:
        print('error')
    return key

image()
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import requests, random, os, shutil
from datetime import datetime

app = Flask(__name__)

key = "AIzaSyAlhdlfM5OklUfOHAK8gdgksuYbOwH3d7o"

us_states = [
    "alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", 
    "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", 
    "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan", 
    "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "newhampshire", 
    "newjersey", "newmexico", "newyork", "northcarolina", "northdakota", "ohio", "oklahoma", 
    "oregon", "pennsylvania", "rhodeisland", "southcarolina", "southdakota", "tennessee", 
    "texas", "utah", "vermont", "virginia", "washington", "westvirginia", "wisconsin", "wyoming"
]



@app.route('/', methods=['GET', 'POST'])
def home():
    print("we're home!")

    # jay lukose can u add the image link and make it randomly generate please
    #JLUKOSE ADD CITY INFORMATION
    # city = CITYNAME
    # location
    # all that stuff
    image()
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    print("running result page!")

    if request.method == "POST":
        guess = request.form["input"]
        answer = ""
        re = (answer == guess) #JAYLUKOSE ADD THE CITY NAME FROM THE API HERE PLEASE
        if re: r = "correct" 
        else: r = "incorrect"
        print("result method")
        return render_template('result.html', c=guess, res=r, a = answer)
    if request.method == "GET":
        print("going back home...")
        return redirect(url_for("home"))
    
    return render_template('result.html')

def image():
    loc = getLoc()
    url = f'https://maps.googleapis.com/maps/api/streetview?size=600x300&location={loc[0]},{loc[1]}&key={key}'
    response = requests.get(url)
    if response.status_code == 200:
        with open('streetview_image.jpg', 'wb') as file:
            file.write(response.content)
        print("Image successfully downloaded.")
    else:
        print(f"Error: {response.status_code}")
    source_path = "C:/Users/angry/Documents/CS/hackathonlosers/streetview_image.jpg"
    dest = "C:/Users/angry/Documents/CS/hackathonlosers/app/static"
    des_path = os.path.join(dest, os.path.basename(source_path))
    shutil.move(source_path, des_path)
    return getLoc()

def getLoc():
    locations = ['restaurant', 'park']
    loc = locations[random.randint(0, 1)]
    print(loc)
    stateCoord = getState()
    print(stateCoord)
    api = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={stateCoord[0]},{stateCoord[1]}&radius=500000&type={loc}&key={key}'
    
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
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={state}&key={key}"

    response = requests.get(geocode_url).json()

    if response['status'] == 'OK':
        lat = response['results'][0]['geometry']['location']['lat']
        lng = response['results'][0]['geometry']['location']['lng']
        return [lat, lng]
    else:
        print("Error fetching location details")

@app.route('/<filename>')
def serve_image(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == "__main__":
    app.debug = True
    app.run()
from flask import Flask, render_template, request, redirect, url_for
import calendar, os
from datetime import datetime

app = Flask(__name__)

key = "AIzaSyAlhdlfM5OklUfOHAK8gdgksuYbOwH3d7o"

@app.route('/', methods=['GET', 'POST'])
def home():
    print("we're home!")

    il = "" # jay lukose can u add the image link and make it randomly generate please
    #JLUKOSE ADD CITY INFORMATION
    # city = CITYNAME
    # location
    # all that stuff


    if request.method == "POST":
        guess = request.form["input"]
        r = "CORRECT" #(city == guess)
        print("result method")
        return render_template('result.html', c = guess, res = r)

    return render_template('index.html', image_link = il)

@app.route('/result', methods=['GET', 'POST'])
def result():
    print("running result page!")

    if request.method == "GET":
        "going back home..."
        return redirect(url_for("home"))
    
    return render_template('result.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
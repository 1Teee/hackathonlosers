from flask import Flask, render_template, request, redirect, url_for
import calendar, os
from datetime import datetime

app = Flask(__name__)

key = "AIzaSyAlhdlfM5OklUfOHAK8gdgksuYbOwH3d7o"

@app.route('/', methods=['GET', 'POST'])
def home():
    print("we're home!")

    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
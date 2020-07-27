# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import requests
from datetime import datetime
import os
from model import makeCategoriesList
from model import makeCuisineList
from model import makeCuisineIDList
from model import getLocation
from model import getLocationID
from model import getLocationType

# -- Initialization section --
app = Flask(__name__)
app.config['ZOMATO_KEY'] = os.getenv('ZOMATO_KEY')
global_city_id = 0
global_list_of_cuisines_id = []
global_list_of_cuisines = []
global_location_query = ""

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    # Load API_KEY
    ZOMATO_API_KEY = "496de5020f4fb0a70da1e71b5f5f7ddb"
    # API Endpoint
    version = 'v2.1'
    API_AUTH = {'user-key': ZOMATO_API_KEY}
    return render_template("index.html", time=datetime.now())
    
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    ZOMATO_API_KEY = "496de5020f4fb0a70da1e71b5f5f7ddb"
    API_AUTH = {'user-key': ZOMATO_API_KEY}
    version = 'v2.1'
    location_query = request.form["location_choice"]
    global global_location_query
    global_location_query += location_query
    endpoint1 = f"https://developers.zomato.com/api/v2.1/locations?query={location_query}"
    location = requests.get(endpoint1, headers=API_AUTH).json()
    city_id = getLocation(location)
    global global_city_id
    global_city_id += city_id
    endpoint2 = f"https://developers.zomato.com/api/{version}/categories"
    endpoint3 = f"https://developers.zomato.com/api/{version}/cuisines?city_id={city_id}"
    # The documentation for this API says to include the authentication key in the headers.
    # To do that, we make a dictionary and use the headers keyword
    categories = requests.get(endpoint2, headers=API_AUTH).json()
    cuisines = requests.get(endpoint3, headers=API_AUTH).json()
    # We get the data from the request using .json()
    list_of_categories = makeCategoriesList(categories)
    list_of_cuisines = makeCuisineList(cuisines)
    list_of_cuisines_id = makeCuisineIDList(cuisines)

    # Call on global variables and store the values
    global global_list_of_cuisines
    global_list_of_cuisines = list_of_cuisines
    global global_list_of_cuisines_id
    global_list_of_cuisines_id = list_of_cuisines_id

    return render_template("submit.html", time=datetime.now(), list_of_categories = list_of_categories, list_of_cuisines = list_of_cuisines, city_id = city_id, location_query = location_query)

@app.route('/results', methods=["GET", "POST"])
def results():
    ZOMATO_API_KEY = "496de5020f4fb0a70da1e71b5f5f7ddb"
    category_query = request.form["categories"]
    cuisine_query = request.form["cuisines"]
    version = 'v2.1'
    endpoint1 = f"https://developers.zomato.com/api/{version}/categories"
    API_AUTH = {'user-key': ZOMATO_API_KEY}
    categories = requests.get(endpoint1, headers=API_AUTH).json()
    list_of_categories = makeCategoriesList(categories)
    index_of_cuisines = global_list_of_cuisines.index(cuisine_query)
    cuisine_id = global_list_of_cuisines_id[index_of_cuisines]
    category_id = list_of_categories.index(category_query) + 1
    endpoint2 = f"https://developers.zomato.com/api/v2.1/search?entity_id=280&cuisines=2&category={category_id}"
    endpoint3 = f"https://developers.zomato.com/api/v2.1/locations?query={global_location_query}"
    location = requests.get(endpoint3, headers=API_AUTH).json()
    location_id = getLocationID(location)
    location_type = getLocationType(location)
    return render_template("results.html", time=datetime.now(), category_id = category_id, cuisine_id = cuisine_id, location_id = location_id, location_type= location_type)
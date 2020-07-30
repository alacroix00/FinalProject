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
from model import getLocationTitle
from model import getLocationID
from model import getLocationType
from model import RestaurantName
from model import RestaurantHighlights
from model import RestaurantTiming
from model import RestaurantCurrency
from model import RestaurantAverageCost
from model import RestaurantRating
from model import RestaurantURL
from model import RestaurantCuisine
from model import RestaurantAddress

# -- Initialization section --
app = Flask(__name__)
app.config['ZOMATO_KEY'] = os.getenv('ZOMATO_KEY')
global_city_id = 0
global_list_of_cuisines_id = []
global_list_of_cuisines = []
global_location_query = ""
global_loc_title = ""
global_loc_id = 0
global_loc_type = ""
global_category_id = 0
global_cuisine_id = 0


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
    loc_title = getLocationTitle(location)
    global global_loc_title
    global_loc_title = loc_title
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
    global global_category_id
    global_category_id = category_id
    global global_cuisine_id
    global_cuisine_id = cuisine_id
    endpoint2 = f"https://developers.zomato.com/api/v2.1/search?entity_id=280&cuisines=2&category={category_id}"
    endpoint3 = f"https://developers.zomato.com/api/v2.1/locations?query={global_location_query}"
    location = requests.get(endpoint3, headers=API_AUTH).json()
    location_id = getLocationID(location)
    global global_loc_id
    global_loc_id = location_id
    location_type = getLocationType(location)
    global global_loc_type
    global_loc_type = location_type
    endpoint4 = f"https://developers.zomato.com/api/v2.1/search?entity_id={location_id}&entity_type={location_type}&cuisines={cuisine_id}&category={category_id}"
    search_results = requests.get(endpoint4, headers=API_AUTH).json()
    restaurant_name = RestaurantName(search_results)
    restaurant_highlights = RestaurantHighlights(search_results)
    restaurant_average_cost = RestaurantAverageCost(search_results)
    restaurant_currency = RestaurantCurrency(search_results)
    restaurant_timing = RestaurantTiming(search_results)
    restaurant_rating = RestaurantRating(search_results)
    restaurant_address = RestaurantAddress(search_results)
    restaurant_url = RestaurantURL(search_results)
    restaurant_cuisine = RestaurantCuisine(search_results)
    return render_template("results.html", time=datetime.now(), global_loc_title = global_loc_title, restaurant_url= restaurant_url, restaurant_cuisine= restaurant_cuisine, restaurant_rating = restaurant_rating, restaurant_timing=restaurant_timing, restaurant_currency=restaurant_currency, restaurant_average_cost=restaurant_average_cost, restaurant_highlights=restaurant_highlights, restaurant_address = restaurant_address, restaurant_name=restaurant_name)

@app.route('/finalresults', methods=['GET','POST'])
def finalresults():
    ZOMATO_API_KEY = "496de5020f4fb0a70da1e71b5f5f7ddb"
    version = 'v2.1'
    API_AUTH = {'user-key': ZOMATO_API_KEY}
    sort_choice = request.form["sort_choice"]
    order_choice = request.form["order_choice"]
    endpoint5 = f"https://developers.zomato.com/api/v2.1/search?entity_id={global_city_id}&entity_type={global_loc_type}&cuisines={global_cuisine_id}&category={global_category_id}&sort={sort_choice}&order={order_choice}"
    final_results = requests.get(endpoint5, headers=API_AUTH).json()
    restaurant_name = RestaurantName(final_results)
    restaurant_highlights = RestaurantHighlights(final_results)
    restaurant_average_cost = RestaurantAverageCost(final_results)
    restaurant_currency = RestaurantCurrency(final_results)
    restaurant_timing = RestaurantTiming(final_results)
    restaurant_rating = RestaurantRating(final_results)
    restaurant_address = RestaurantAddress(final_results)
    restaurant_url = RestaurantURL(final_results)
    restaurant_cuisine = RestaurantCuisine(final_results)
    return render_template("finalresults.html", time=datetime.now(), global_loc_title = global_loc_title, restaurant_url= restaurant_url, restaurant_cuisine= restaurant_cuisine, restaurant_rating = restaurant_rating, restaurant_timing=restaurant_timing, restaurant_currency=restaurant_currency, restaurant_average_cost=restaurant_average_cost, restaurant_highlights=restaurant_highlights, restaurant_address = restaurant_address, restaurant_name=restaurant_name)
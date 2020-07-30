def makeCategoriesList(categories):
    list_of_categories = []
    for num in range(0,len(categories["categories"])):
        list_of_categories.append(categories["categories"][num]["categories"]["name"])
    return list_of_categories

def makeCuisineList(cuisines):
    list_of_cuisines = []
    for num in range(0,len(cuisines["cuisines"])):
        list_of_cuisines.append(cuisines["cuisines"][num]["cuisine"]["cuisine_name"])
    return list_of_cuisines

def makeCuisineIDList(cuisines):
    list_of_cuisines_id = []
    for num in range(0,len(cuisines["cuisines"])):
        list_of_cuisines_id.append(cuisines["cuisines"][num]["cuisine"]["cuisine_id"])
    return list_of_cuisines_id

def getLocation(location):
    return location["location_suggestions"][0]["city_id"]

def getLocationTitle(location):
    return location["location_suggestions"][0]["title"]

def getLocationID(location):
    location_id = location["location_suggestions"][0]["entity_id"]
    return location_id

def getLocationType(location):
    location_type = location["location_suggestions"][0]["entity_type"]
    return location_type

def RestaurantName(search_results):
    restaurant_name = []
    for num in range(0, search_results["results_shown"]):
        restaurant_name.append(search_results["restaurants"][num]["restaurant"]["name"])
    return restaurant_name

def RestaurantHighlights(search_results):
    restaurant_highlights =[]
    for num in range(0, search_results["results_shown"]):
        restaurant_highlights.append(search_results["restaurants"][num]["restaurant"]["highlights"])
    return restaurant_highlights

def RestaurantAverageCost(search_results):
    restaurant_average_cost = []
    for num in range(0, search_results["results_shown"]):
        restaurant_average_cost.append(search_results["restaurants"][num]["restaurant"]["average_cost_for_two"])
    return restaurant_average_cost

def RestaurantCurrency(search_results):
    restaurant_currency = []
    for num in range(0, search_results["results_shown"]):
        restaurant_currency.append(search_results["restaurants"][num]["restaurant"]["currency"])
    return restaurant_currency

def RestaurantTiming(search_results):
    restaurant_timing = []
    for num in range(0, search_results["results_shown"]):
        restaurant_timing.append(search_results["restaurants"][num]["restaurant"]["timings"])
    return restaurant_timing

def RestaurantAddress(search_results):
    restaurant_address = []
    for num in range(0, search_results["results_shown"]):
        restaurant_address.append(search_results["restaurants"][num]["restaurant"]["location"]["address"])
    return restaurant_address

def RestaurantRating(search_results):
    restaurant_rating = []
    for num in range(0, search_results["results_shown"]):
        restaurant_rating.append(search_results["restaurants"][num]["restaurant"]["user_rating"]["aggregate_rating"])
    return restaurant_rating

def RestaurantURL(search_results):
    restaurant_url = []
    for num in range(0, search_results["results_shown"]):
        restaurant_url.append(search_results["restaurants"][num]["restaurant"]["url"])
    return restaurant_url

def RestaurantCuisine(search_results):
    restaurant_cuisine = []
    for num in range(0, search_results["results_shown"]):
        restaurant_cuisine.append(search_results["restaurants"][num]["restaurant"]["cuisines"])
    return restaurant_cuisine

# def RestaurantImage(search_results):
#     restaurant_image = []
#     for num in range(0, search_results["results_shown"]):
#         restaurant_image.append(search_results["restaurants"][num]["featur"]["cuisines"])
#     return restaurant_image
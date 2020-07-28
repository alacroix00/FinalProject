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

def getLocationID(location):
    location_id = location["location_suggestions"][0]["entity_id"]
    return location_id

def getLocationType(location):
    location_type = location["location_suggestions"][0]["entity_type"]
    return location_type

def search(search_results):
    restaurant_name = []
    restaurant_address = []
    restaurant_url = []
    restaurant_rating = []
    restaurant_cuisine = []
    restaurant_highlights =[]
    restaurant_average_cost = []
    restaurant_currency = []
    restaurant_timing = []
    counter = 0
    for num in range(0, search_results["results_shown"]):
        restaurant_name.append(search_results["restaurants"][num]["restaurant"]["name"])
    return restaurant_name
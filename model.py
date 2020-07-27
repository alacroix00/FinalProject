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
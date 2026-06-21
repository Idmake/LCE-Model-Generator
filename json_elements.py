from json_data import contains_key

def get_element_count(json_data):
    elements = json_data.get("elements")
    if elements != None:
        return len(elements)
    
    print("The specified JSON data doesn't have \"elements\".")
    return -1

def get_custom_element_key(element, key):
    if contains_key(element, key):
        return element[key]
    
def get_name(element):
    if contains_key(element, "name"):
        return element["name"]
    
    return "cube" # Fall back to default name

def get_box_uv(element):    return get_custom_element_key(element, "box_uv")
def get_from(element):      return get_custom_element_key(element, "from")
def get_to(element):        return get_custom_element_key(element, "to")
def get_autouv(element):    return get_custom_element_key(element, "autouv")
def get_color(element):     return get_custom_element_key(element, "color")
def get_origin(element):    return get_custom_element_key(element, "origin")
def get_faces(element):     return get_custom_element_key(element, "faces")
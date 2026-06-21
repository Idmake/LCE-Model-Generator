import json

def get_json_data(filepath):
    try:
        with open(filepath) as file:
            json_data = file.read()
            json_data = json.loads(json_data)
            return json_data
        
    except UnicodeDecodeError:
        print("Trying to read this file caused a UnicodeDecodeError, is", filepath, "the correct file?")
        return ""
    except json.JSONDecodeError:
        print("Trying to read this file caused a JSONDecodeError, is", filepath, "the correct file?")
        return ""
    except ValueError:
        print("Trying to read this file caused an unknown error, is", filepath, "the correct file?")
        return ""
    
def get_json_element_count(json_data):
    elements = json_data.get("elements")
    if elements != None:
        return len(elements)
    
    print("The specified JSON data doesn't have \"elements\".")
    return -1

def contains_key(element, key):
    key = key
    return str(element).find(key) != -1 

def get_json_element_from(element):
    return element["from"]

def get_json_element_to(element):
    return element["to"]

def get_json_element_rotation(element):
    if contains_key(element, "rotation"):
        return element["rotation"]

def get_json_element_color(element):
    return element["color"]

def get_json_element_faces(element):
    return element["faces"]

def get_json_element_name(element):
    if contains_key(element, "name"):
        return element["name"]
    
    return "cube" # Fall back to default name

def get_custom_json_element(element, key):
    if contains_key(element, key):
        return element[key]
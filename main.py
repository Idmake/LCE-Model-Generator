import json
import tkinter.filedialog
import os.path

def get_ask_filename(title, type_name, type_extension):
    return tkinter.filedialog.askopenfilename(title=title, filetypes=[(type_name, type_extension)])

def get_json_data(filepath):
    try:
        with open(filepath) as file:
            json_data = file.read()
            json_data = json.loads(json_data)
            return json_data
        
    except UnicodeDecodeError:
        print("Trying to read this file caused a UnicodeDecodeError, is", filepath, "the correct file?")
        return None
    except json.JSONDecodeError:
        print("Trying to read this file caused a JSONDecodeError, is", filepath, "the correct file?")
        return None
    except ValueError:
        print("Trying to read this file caused an unknown error, is", filepath, "the correct file?")
        return None
    
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

def get_custom_json_element(element, key):
    if contains_key(element, key):
        return element[key]
    
def convert_to_whd(from_, to_):
    # Convert to width, height, depth because it's what LCE uses
    w = to_[0] - from_[0]
    h = to_[1] - from_[1]
    d = to_[2] - from_[2]

    return [w, h, d]

def convert_to_xyz(from_):
    x =     from_[0]
    y = 0 - from_[1] # Invert because of different coordinate systems
    z =     from_[2]

    return [x, y, z]


json_file = get_ask_filename(title="Select your exported JSON file", type_name="JSON File", type_extension="*.json")
json_data = ""
json_element_count = -1

if os.path.exists(json_file): 
    json_data = get_json_data(json_file)
    json_element_count = get_json_element_count(json_data)
    
if json_element_count != -1:
    for index, element in enumerate(json_data["elements"]):
        from_ =         get_json_element_from(element)
        to_ =           get_json_element_to(element)
        rotation_ =     get_json_element_rotation(element)
        color_ =        get_json_element_color(element)
        faces_ =        get_json_element_faces(element)

        print("")
        print("-- ELEMENT", index, "--")
        print("from:", from_)
        print("to:", to_)
        print("rotation:", rotation_)
        print("color:", color_)
        print("faces:", faces_)

        whd = convert_to_whd(from_=from_, to_=to_)
        xyz = convert_to_xyz(from_=from_)
        print(xyz)
        print(whd)

        
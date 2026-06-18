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

def get_json_element_name(element):
    if contains_key(element, "name"):
        return element["name"]
    
    return "cube" # Fall back to default name

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

def format_code(code):
    new_code = ""
    lines = code.splitlines()
    line_count = len(lines)

    # In multi-line strings the preceding whitespaces are kept, remove them here
    for index, line in enumerate(lines):
        new_code += line.strip()

        # Only add a new line if its not the last one
        if index != line_count - 1:
            new_code += "\n"

    return new_code

def contains_value(list, value):
    for item in list:
        if item == value:
            return True
        
    return False

def generate_snippet(json_data):
    snippet = ""
    snippet += f"float width, height, depth;\n"
    snippet += "\n"

    for index, element in enumerate(json_data["elements"]):
        name_ =         get_json_element_name(element)
        from_ =         get_json_element_from(element)
        to_ =           get_json_element_to(element)
        rotation_ =     get_json_element_rotation(element)
        color_ =        get_json_element_color(element)
        faces_ =        get_json_element_faces(element)

        print("")
        print("-- ELEMENT", index, "--")
        print("name:", name_)
        print("from:", from_)
        print("to:", to_)
        print("rotation:", rotation_)
        print("color:", color_)
        print("faces:", faces_)

        whd = convert_to_whd(from_=from_, to_=to_)
        xyz = convert_to_xyz(from_=from_)

        width = whd[0]
        height = whd[1]
        depth = whd[2]
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]

        # Don't reinitialize already used element / ModelPart!
        if contains_value(used_element_names, name_) == False:

            # Add spacing after each new part but not on the first line
            if index != 0: snippet += f"\n"
            snippet += f"{name_} = (new ModelPart(this, 0, 0))->setTexSize(0, 0);"

        snippet += f"""
            width = {width};
            height = {height};
            depth = {depth};
            {name_}->addBox({x}, {y}, {z}, width, height, depth);"""


        snippet = format_code(snippet)
        used_element_names.append(name_)

    return snippet



json_file = get_ask_filename(title="Select your exported JSON file", type_name="JSON File", type_extension="*.json")
json_data = ""
json_element_count = -1
output_snippet = ""
used_element_names = [] # Keep track of used element names, so we don't reinitialize them in the game

if os.path.exists(json_file): 
    json_data = get_json_data(json_file)
    json_element_count = get_json_element_count(json_data)
    output_snippet = generate_snippet(json_data)

    with open("output.txt", "w") as file:
        file.write(output_snippet)

        
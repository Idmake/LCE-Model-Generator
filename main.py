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
    
def get_json_element_data(json_data, index):
    elements = json_data.get("elements")
    if index < len(elements):
        return elements[index]
    
    print("Specified element index is", index, "even though there are only", len(elements), "elements.")

def get_json_element_count(json_data):
    elements = json_data.get("elements")
    if elements != None:
        return len(elements)
    
    print("The specified JSON data doesn't have \"elements\".")
    return None


json_file = get_ask_filename(title="Select your exported JSON file", type_name="JSON File", type_extension="*.json")
if os.path.exists(json_file): 

    json_data = get_json_data(json_file)

    if json_data != None:
        json_element_count = get_json_element_count(json_data)
        
        if json_element_count != None:
            for element in json_data["elements"]:
                print(str(element) + "\n\n")
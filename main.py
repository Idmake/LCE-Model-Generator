import json
import tkinter.filedialog

def get_file_prompt(title, type_name, type_extension):
    return tkinter.filedialog.askopenfilename(title=title, filetypes=[(type_name, type_extension)])

def get_json_data(filepath):
    with open(filepath) as file:
        json_data = file.read()
        json_data = json.loads(json_data)
        return json_data
    
def get_json_element_data(json_data, index):
    elements = json_data.get("elements")
    if index < len(elements):
        return elements[index]
    
    print("Specified element index is", index, "even though there are only", len(elements), "elements.")

def get_json_element_count(json_data):
    elements = json_data.get("elements")
    return len(elements)


json_file = get_file_prompt(title="Select your exported JSON file", type_name="JSON File", type_extension="*.json")
if json_file != "":
    json_data = get_json_data(json_file)
    json_element_count = get_json_element_count(json_data)

    for element in json_data["elements"]:
        print(str(element) + "\n\n")
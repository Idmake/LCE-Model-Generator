from ask_filename import get_ask_filename
from json_data import get_json_data, get_json_element_count
from snippet import generate_snippet
import shared_variables
    

json_file = get_ask_filename(title="Select your exported JSON file", filetypes=[("JSON File", "*.json"), ("All Files", "*.*")])

if json_file != "":
    json_data = ""
    json_element_count = -1
    output_snippet = ""
    shared_variables.used_element_names = [] # Keep track of used element names, so we don't reinitialize them in the game
    json_data = get_json_data(json_file)

    if json_data != "" and get_json_element_count(json_data) != -1:
        output_snippet = generate_snippet(json_data)
        with open("output.txt", "w") as file:
            file.write(output_snippet)
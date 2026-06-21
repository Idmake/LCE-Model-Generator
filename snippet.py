from json_elements import get_json_element_color, get_json_element_count, get_json_element_faces, get_json_element_from, get_json_element_name, get_json_element_rotation, get_json_element_to
from LCE_convert import convert_to_scale
from contains_value import contains_value
import shared_variables

def format_code(code: str):
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

def generate_snippet(json_data):
    snippet = ""
    snippet += f"double width, height, depth;\n"
    snippet += f"double x, y, z;\n"
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

        whd = convert_to_scale(from_=from_, to_=to_)
        width = whd[0]
        height = whd[1]
        depth = whd[2]
        x = from_[0]
        y = -from_[1]
        z = from_[2]

        # Don't reinitialize already used element / ModelPart!
        if contains_value(shared_variables.used_element_names, name_) == False:

            # Add spacing before each new part but not on the first line
            if index != 0: snippet += "\n"
            snippet += f"{name_} = (new ModelPart(this, 0, 0))->setTexSize(0, 0);"

        # This "snippet" part is hard to manage, and also doesn't look that good.
        # If anyone reading this has a better idea for this then you're welcome to share it.
        snippet += f"""
            width = {width};
            height = {height};
            depth = {depth};
            x = {x};
            y = {y};
            z = {z};
            {name_}->addBox(x, y - height - (16 / 2), z, width, height, depth);
            {name_}->y += (32.5);""" # // Yes, this seems to be a magic value, i literally couldn't find any variable for it. May not be perfect.
    
        
        # Not the last line, add a new one
        if index != get_json_element_count(json_data) - 1:
            snippet += "\n"

        shared_variables.used_element_names.append(name_)

    # End of the snippet, remove indentation created by multi-line strings
    snippet = format_code(snippet)
    return snippet
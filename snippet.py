from LCE_convert import convert_to_scale
from contains_value import contains_value
import shared_variables
import json_elements
import json_textures
import json_element_faces

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

    for index, texture in enumerate(json_data["textures"]):
        id_ =           json_textures.get_id(texture)
        width_ =        json_textures.get_width(texture)
        height_ =       json_textures.get_height(texture)
        uv_width =      json_textures.get_uv_width(texture)
        uv_height =     json_textures.get_uv_height(texture)

        print("")
        print("-- TEXTURE", index, "--")
        print("id:", id_)
        print("width:", width_)
        print("height:", height_)
        print("uv_width:", uv_width)
        print("uv_height:", uv_height)

    for index, element in enumerate(json_data["elements"]):
        name_ =         json_elements.get_name(element)
        from_ =         json_elements.get_from(element)
        to_ =           json_elements.get_to(element)
        color_ =        json_elements.get_color(element)
        faces_ =        json_elements.get_faces(element)
        texture_id_ =   json_element_faces.get_texture_id(element)
        uv_offset_ =    json_element_faces.get_uv_offset(element)

        print("")
        print("-- ELEMENT", index, "--")
        print("name:", name_)
        print("from:", from_)
        print("to:", to_)
        print("color:", color_)
        print("faces:", faces_)
        print("texture_id:", texture_id_)
        print("uv_offset:", uv_offset_)

        whd = convert_to_scale(from_=from_, to_=to_)
        width = whd[0]
        height = whd[1]
        depth = whd[2]
        x = from_[0]
        y = -from_[1]
        z = from_[2]
        u_offset = uv_offset_[0]
        v_offset = uv_offset_[1]

        if texture_id_ < json_textures.get_texture_count(json_data):
            uv_width = json_textures.get_uv_width(texture)
            uv_height = json_textures.get_uv_height(texture)
        else:
            uv_width = 0
            uv_height = 0
            
            print("Failed to get UV size as the given texture id (index) is",
                    texture_id_, ", even though there are only", json_textures.get_texture_count(json_data), "textures available.")

        # Don't reinitialize already used element / ModelPart!
        if contains_value(shared_variables.used_element_names, name_) == False:

            # Add spacing before each new part but not on the first line
            if index != 0: snippet += "\n"
            snippet += f"{name_} = (new ModelPart(this, {u_offset}, {v_offset}))->setTexSize({uv_width}, {uv_height});"

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
        if index != json_elements.get_element_count(json_data) - 1:
            snippet += "\n"

        shared_variables.used_element_names.append(name_)

    # End of the snippet, remove indentation created by multi-line strings
    snippet = format_code(snippet)
    return snippet
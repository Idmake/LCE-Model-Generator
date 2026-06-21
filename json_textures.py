from json_data import contains_key

def get_texture_count(json_data):
    textures = json_data.get("textures")
    if textures != None:
        return len(textures)
    
    print("The specified JSON data doesn't have \"textures\".")
    return -1

def get_custom_texture_key(texture, key):
    if contains_key(texture, key):
        return texture[key]
    
def get_id(texture):            return get_custom_texture_key(texture, "id")
def get_width(texture):         return get_custom_texture_key(texture, "width")
def get_height(texture):        return get_custom_texture_key(texture, "height")
def get_uv_width(texture):      return get_custom_texture_key(texture, "uv_width")
def get_uv_height(texture):     return get_custom_texture_key(texture, "uv_height")
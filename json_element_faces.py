from json_elements import get_faces

def get_face_north(face):                           return face["north"]
def get_face_east(face):                            return face["east"]
def get_face_south(face):                           return face["south"]
def get_face_west(face):                            return face["west"]
def get_face_up(face):                              return face["up"]
def get_face_down(face):                            return face["down"]
def get_face_direction_uv(face_direction):          return face_direction["uv"]
def get_face_direction_texture(face_direction):     return face_direction["texture"]
def get_uv_offset(element):
    # Each element (part) has their own set of uv coordinates, which are offsets on the texture.
    # To calculate the offset on the texture, we can just use the x coordinate of the east face (u-offset)
    # and the y coordinate of the down face (v-offset) as they give us the most top-left position.
    all_faces = get_faces(element)
    face_east = get_face_direction_uv(all_faces["east"])
    face_down = get_face_direction_uv(all_faces["down"])
    u_texture_offset = face_east[0]
    v_texture_offset = face_down[1]

    return [u_texture_offset, v_texture_offset]

def get_texture_id(element):
    # Suppose each face (side) of the element (part) uses the same texture:
    all_faces = get_faces(element)
    texture_id = get_face_direction_texture(all_faces["east"])

    return texture_id
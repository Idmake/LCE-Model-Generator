def convert_to_scale(from_, to_):
    # Convert to width, height, depth because it's what LCE uses
    w = to_[0] - from_[0]
    h = to_[1] - from_[1]
    d = to_[2] - from_[2]

    return [w, h, d]

def convert_to_xyz(from_, whd):
    # Blockbench and LCE use different coordinate systems so we have to convert the positions
    x =     from_[0]
    y =    -from_[1] - whd[1] - (16 / 2)
    z =     from_[2]

    return [x, y, z]
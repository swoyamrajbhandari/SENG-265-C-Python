#!/usr/bin/env python

import random

class PyArtConfig:
    """PyArtConfig class"""

    # Default ranges for different parameters
    SHA_RANGE = (0, 3)
    X_RANGE = (0, 800)  # Assuming viewport size is 800x600
    Y_RANGE = (0, 600)
    RAD_RANGE = (0, 100)
    RX_RANGE = (10, 30)
    RY_RANGE = (10, 30)
    W_RANGE = (10, 100)
    H_RANGE = (10, 100)
    R_RANGE = (0, 255)
    G_RANGE = (0, 255)
    B_RANGE = (0, 255)
    OP_RANGE = (0.0, 1.0)

    def __init__(self, cnt: int, sha_range: tuple = SHA_RANGE, x_range: tuple = X_RANGE, y_range: tuple = Y_RANGE, rad_range: tuple = RAD_RANGE, rx_range: tuple = RX_RANGE,
                 ry_range: tuple = RY_RANGE, w_range: tuple = W_RANGE, h_range: tuple = H_RANGE, r_range: tuple = R_RANGE, g_range: tuple = G_RANGE, b_range: tuple = B_RANGE,
                 op_range: tuple = OP_RANGE) -> None:
        """__init__() method"""

        self.cnt = cnt
        self.sha_range = sha_range
        self.x_range = x_range
        self.y_range = y_range
        self.rad_range = rad_range
        self.rx_range = rx_range
        self.ry_range = ry_range
        self.w_range = w_range
        self.h_range = h_range
        self.r_range = r_range
        self.g_range = g_range
        self.b_range = b_range
        self.op_range = op_range

    def generate_random_number(self, range_tuple: tuple) -> float:
        """generate_random_number() method"""
        return random.uniform(range_tuple[0], range_tuple[1])

    def generate_random_shape(self) -> tuple:
        """generate_random_shape() method"""

        cnt = self.cnt
        sha = int(self.generate_random_number(self.sha_range))
        x = int(self.generate_random_number(self.x_range))
        y = int(self.generate_random_number(self.y_range))
        rad = int(self.generate_random_number(self.rad_range))
        rx = int(self.generate_random_number(self.rx_range))
        ry = int(self.generate_random_number(self.ry_range))
        w = int(self.generate_random_number(self.w_range))
        h = int(self.generate_random_number(self.h_range))
        r = int(self.generate_random_number(self.r_range))
        g = int(self.generate_random_number(self.g_range))
        b = int(self.generate_random_number(self.b_range))
        op = round(self.generate_random_number(self.op_range), 1)

        return cnt, sha, x, y, rad, rx, ry, w, h, r, g, b, op

class RandomShape:
    """RandomShape class"""

    def __init__(self, art_config: PyArtConfig) -> None:
        """__init__() method"""
        self.art_config = art_config

    def __str__(self) -> str:
        """__str__() method"""
        shape_data: tuple = self.art_config.generate_random_shape()
        return (f"CNT: {shape_data[0]}\n"
                f"SHA: {shape_data[1]}\n"
                f"X:   {shape_data[2]}\n"
                f"Y:   {shape_data[3]}\n"
                f"RAD: {shape_data[4]}\n"
                f"RX:  {shape_data[5]}\n"
                f"RY:  {shape_data[6]}\n"
                f"W:   {shape_data[7]}\n"
                f"H:   {shape_data[8]}\n"
                f"R:   {shape_data[9]}\n"
                f"G:   {shape_data[10]}\n"
                f"B:   {shape_data[11]}\n"
                f"OP:  {shape_data[12]}")

    def as_Part2_line(self) -> str:
        """as_Part2_line() method"""
        shape_data: tuple = self.art_config.generate_random_shape()
        return f"{self.art_config.cnt:>3} {shape_data[1]:>3} {shape_data[2]:>3} {shape_data[3]:>3} {shape_data[4]:>3} {shape_data[5]:>2} {shape_data[6]:>2} {shape_data[7]:>2} {shape_data[8]:>2} {shape_data[9]:>3} {shape_data[10]:>3} {shape_data[11]:>3} {shape_data[12]:>3}"

    def as_svg(self) -> str:
        """as_svg() method"""
        shape_data: tuple = self.art_config.generate_random_shape()
        if shape_data[1] == 0:  # Circle
            return f"<circle cx='{shape_data[2]}' cy='{shape_data[3]}' r='{shape_data[4]}' fill='rgb({shape_data[9]}, {shape_data[10]}, {shape_data[11]})' opacity='{shape_data[12]}' />"
        elif shape_data[1] == 1:  # Rectangle
            return f"<rect x='{shape_data[2]}' y='{shape_data[3]}' width='{shape_data[7]}' height='{shape_data[8]}' fill='rgb({shape_data[9]}, {shape_data[10]}, {shape_data[11]})' opacity='{shape_data[12]}' />"
        else:  # Ellipse
            return f"<ellipse cx='{shape_data[2]}' cy='{shape_data[3]}' rx='{shape_data[5]}' ry='{shape_data[6]}' fill='rgb({shape_data[9]}, {shape_data[10]}, {shape_data[11]})' opacity='{shape_data[12]}' />"

def main() -> None:
    """main() method"""

    shapes: list = [] # Create an empty list to store the RandomShape objects.

    for cnt in range(10):
        default_config: PyArtConfig = PyArtConfig(cnt)
        shape: RandomShape = RandomShape(default_config)  # Create a RandomShape object using the default configuration.
        shapes.append(shape)

    # Print the generated shapes in given format
    print("CNT SHA   X   Y RAD RX RY  W  H   R   G   B  OP")
    for shape in shapes:
        print(shape.as_Part2_line())

if __name__ == "__main__":
    main()
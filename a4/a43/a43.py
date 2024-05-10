#!/usr/bin/env python

from typing import IO, List
from collections import namedtuple
import random

# Define namedtuple for Circle, Rectangle, and Ellipse.
Circle= namedtuple("Circle", ["cx", "cy", "r", "fill", "fill_opacity"])
Rectangle = namedtuple("Rectangle", ["x", "y", "width", "height", "fill", "fill_opacity"])
Ellipse = namedtuple("Ellipse", ["cx", "cy", "rx", "ry", "fill", "fill_opacity"])

class HtmlComponent:
    """HtmlComponent class"""
    def __init__(self) -> None:
        """__init__() method"""
        pass

    def render(self, f: IO[str], indent: int = 0) -> None:
        """render() method"""
        pass

class CircleShape(HtmlComponent):
    """CircleShape class"""
    def __init__(self, cx: int, cy: int, r: int, fill: str, fill_opacity: float) -> None:
        """__init__() method"""
        super().__init__()
        self.circle = Circle(cx, cy, r, fill, fill_opacity)

    def render(self, f: IO[str], indent: int = 0) -> None:
        """render() method"""
        ts: str = "   " * indent
        f.write(f'{ts}<circle cx="{self.circle.cx}" cy="{self.circle.cy}" r="{self.circle.r}" '
                f'fill="{self.circle.fill}" fill-opacity="{self.circle.fill_opacity}"></circle>\n')

class RectangleShape(HtmlComponent):
    """RectangleShape class"""
    def __init__(self, x: int, y: int, width: int, height: int, fill: str, fill_opacity: float) -> None:
        """__init__() method"""
        super().__init__()
        self.rect = Rectangle(x, y, width, height, fill, fill_opacity)

    def render(self, f: IO[str], indent: int = 0) -> None:
        """render() method"""
        ts: str = "   " * indent
        f.write(f'{ts}<rect x="{self.rect.x}" y="{self.rect.y}" width="{self.rect.width}" height="{self.rect.height}" '
                f'fill="{self.rect.fill}" fill-opacity="{self.rect.fill_opacity}"></rect>\n')

class EllipseShape(HtmlComponent):
    """EllipseShape class"""
    def __init__(self, cx: int, cy: int, rx: int, ry: int, fill: str, fill_opacity: float) -> None:
        """__init__() method"""
        super().__init__()
        self.ellipse = Ellipse(cx, cy, rx, ry, fill, fill_opacity)

    def render(self, f: IO[str], indent: int = 0) -> None:
        """render() method"""
        ts: str = "   " * indent
        f.write(f'{ts}<ellipse cx="{self.ellipse.cx}" cy="{self.ellipse.cy}" rx="{self.ellipse.rx}" ry="{self.ellipse.ry}" '
                f'fill="{self.ellipse.fill}" fill-opacity="{self.ellipse.fill_opacity}"></ellipse>\n')

class SvgCanvas(HtmlComponent):
    """SvgCanvas class"""
    def __init__(self, width: int, height: int) -> None:
        """__init__() method"""
        super().__init__()
        self.width = width
        self.height = height
        self.shapes: list = []

    def add_shape(self, shape: HtmlComponent) -> None:
        """add_shape() method"""
        self.shapes.append(shape)

    def render(self, f: IO[str], indent: int = 0) -> None:
        """render() method"""
        ts: str = "   " * indent
        f.write(f'{ts}<!--Define SVG drawing box-->\n')
        f.write(f'{ts}<svg width="{self.width}" height="{self.height}">\n')
        for shape in self.shapes:
            shape.render(f, indent + 1)
        f.write(f'{ts}</svg>\n')

class HtmlDocument(HtmlComponent):
    """HtmlDocument class"""
    def __init__(self, title: str):
        """__init__() method"""
        super().__init__()
        self.title = title
        self.body: list = []

    def add_component(self, component: HtmlComponent) -> None:
        """add_component() method"""
        self.body.append(component)

    def render(self, filename: str, indent: int = 0) -> None:
        """render() method"""
        with open(filename, "w") as f:
            ts: str = "   " * indent
            f.write("<html>\n")
            f.write("<head>\n")
            f.write(f"<title>{self.title}</title>\n")
            f.write("</head>\n")
            f.write("<body>\n")
            for component in self.body:
                component.render(f, indent=1)
            f.write("</body>\n")
            f.write("</html>\n")

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

    def __init__(self, cnt: int, sha_range: tuple = SHA_RANGE, x_range: tuple = X_RANGE, y_range: tuple = Y_RANGE,
                 rad_range: tuple = RAD_RANGE, rx_range: tuple = RX_RANGE, ry_range: tuple = RY_RANGE, w_range: tuple = W_RANGE, h_range: tuple = H_RANGE,
                 r_range: tuple = R_RANGE, g_range: tuple = G_RANGE, b_range: tuple = B_RANGE, op_range: tuple = OP_RANGE) -> None:
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
        self.shape_data: tuple = self.art_config.generate_random_shape()

    def as_shape(self) -> HtmlComponent:
        """as_shape() method"""
        if self.shape_data[1] == 0:  # Circle
            return CircleShape(self.shape_data[2], self.shape_data[3], self.shape_data[4], f'rgb({self.shape_data[9]}, {self.shape_data[10]}, {self.shape_data[11]})', self.shape_data[12])
        elif self.shape_data[1] == 1:  # Rectangle
            return RectangleShape(self.shape_data[2], self.shape_data[3], self.shape_data[7], self.shape_data[8], f'rgb({self.shape_data[9]}, {self.shape_data[10]}, {self.shape_data[11]})', self.shape_data[12])
        else:  # Ellipse
            return EllipseShape(self.shape_data[2], self.shape_data[3], self.shape_data[5], self.shape_data[6], f'rgb({self.shape_data[9]}, {self.shape_data[10]}, {self.shape_data[11]})', self.shape_data[12])

class GreetingCard:
    """GreetingCard class"""
    def __init__(self) -> None:
        """__init__() method"""
        self.canvas: SvgCanvas = SvgCanvas(800,600)
        self.configs: list = []

    def add_config(self, config) -> None:
        """add_config() method"""
        self.configs.append(config)

    def generate_greeting_card(self, filename: str) -> None:
        """generate_greeting_card() method"""
        for config in self.configs:
            random_shape = RandomShape(config)
            self.canvas.add_shape(random_shape.as_shape())

        doc: HtmlDocument = HtmlDocument("Greeting Card")
        doc.add_component(self.canvas)
        doc.render(filename)

def main() -> None:
    """main() method"""

    # Create three instances of GreetingCardGenerator
    greeting_card1: GreetingCard = GreetingCard()
    greeting_card2: GreetingCard = GreetingCard()
    greeting_card3: GreetingCard= GreetingCard()

    # Add random shape configurations to each generator
    num_shapes_canvas1: int = 300
    num_shapes_canvas2: int = 400
    num_shapes_canvas3: int = 500

    for _ in range(num_shapes_canvas1):
        config = PyArtConfig(cnt=1)
        greeting_card1.add_config(config)

    for _ in range(num_shapes_canvas2):
        config = PyArtConfig(cnt=1)
        greeting_card2.add_config(config)

    for _ in range(num_shapes_canvas3):
        config = PyArtConfig(cnt=1)
        greeting_card3.add_config(config)

    # Generate the three greeting cards
    greeting_card1.generate_greeting_card("a431.html")
    greeting_card2.generate_greeting_card("a432.html")
    greeting_card3.generate_greeting_card("a433.html")


if __name__ == "__main__":
    main()
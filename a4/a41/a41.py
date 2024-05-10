#!/usr/bin/env python

from typing import IO
from collections import namedtuple

# Define namedtuple for Circle, Rectangle and Ellipse.
Circle = namedtuple("Circle", ["cx", "cy", "r", "fill", "fill_opacity"])
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

    def gen_art(self) -> None:
        """gen_art() method"""
        self.add_shape(CircleShape(50, 50, 50, "rgb(255, 0, 0)", 1.0))
        self.add_shape(CircleShape(150, 50, 50, "rgb(255, 0, 0)", 1.0))
        self.add_shape(CircleShape(250, 50, 50, "rgb(255, 0, 0)", 1.0))
        self.add_shape(CircleShape(350, 50, 50, "rgb(255, 0, 0)", 1.0))
        self.add_shape(CircleShape(450, 50, 50, "rgb(255, 0, 0)", 1.0))
        self.add_shape(CircleShape(50, 250, 50, "rgb(0, 0, 255)", 1.0))
        self.add_shape(CircleShape(150, 250, 50, "rgb(0, 0, 255)", 1.0))
        self.add_shape(CircleShape(250, 250, 50, "rgb(0, 0, 255)", 1.0))
        self.add_shape(CircleShape(350, 250, 50, "rgb(0, 0, 255)", 1.0))
        self.add_shape(CircleShape(450, 250, 50, "rgb(0, 0, 255)", 1.0))

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
    def __init__(self, title: str) -> None:
        """__init__() method"""
        super().__init__()
        self.title = title
        self.body: list = []

    def add_component(self, component: HtmlComponent) -> None:
        """add_component() method"""
        self.body.append(component)

    def gen_art(self) -> None:
        """gen_art() method"""
        svg_canvas: SvgCanvas = SvgCanvas(500, 300)
        svg_canvas.gen_art()
        self.add_component(svg_canvas)

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

def main():
    """main() method"""
    doc: HtmlDocument = HtmlDocument("My Art")
    doc.gen_art()
    doc.render("a41.html")

if __name__ == "__main__":
    main()
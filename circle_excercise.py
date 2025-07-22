from PIL import Image, ImageDraw
import random

class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes

    def draw(self, draw_context):
        x, y = self.attributes["position"]
        r = self.attributes["radius"]
        color = self.attributes["color"]
        draw_context.ellipse([(x - r, y - r), (x + r, y + r)], fill=color)

    
class Canvas:
    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.elements = []
        self.image = Image.new("RGB", (width, height), background_color)

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        draw = ImageDraw.Draw(self.image)
        for element in self.elements:
            element.draw(draw)
        self.image.show()
        self.image.save("output.png")


def main():
    canvas = Canvas(500, 500, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    for _ in range(40):
        attrs = {
            "position": (random.randint(0, 500), random.randint(0, 500)),
            "radius": random.randint(10, 100),
            "color": (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        }
        circle = ArtElement(attrs)
        canvas.add_element(circle)
    canvas.render()


main()
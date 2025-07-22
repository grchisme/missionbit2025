from PIL import Image, ImageDraw
import random

class ArtElement:
    def __init__(self, attributes):
        self.attributes = attributes

    def draw(self, draw_context):
        x, y = self.attributes["Position"]
        r = self.attributes["Radius"]
        color = self.attributes["Color"]
        shape = self.attributes["Shape"]

        if shape == 1:
            draw_context.ellipse([(x - r, y - r), (x + r, y + r)], fill=color)
        elif shape == 2:
            linex = random.randint(0, 500)
            liney = random.randint(0, 500)
            draw_context.line([(x, y), (linex, liney)], fill=color, width = 5)
        elif shape == 3:
            sizex = random.randint(0, 500)
            sizey = random.randint(0, 500)
            draw_context.rectangle((x, y, x + sizex, y + sizey), fill=color)
        elif shape == 4:
            arcx = random.randint(0, 500)
            arcy = random.randint(0, 500)
            start_angle = random.randint(0, 180)
            end_angle = random.randint(181, 360)
            draw_context.arc([min(x, arcx), min(y, arcy), max(x, arcx), max(y, arcy)], start_angle, end_angle, fill=color, width = 3)

    def __str__(self):
        return '\n'.join(f"{k}: {v}" for k, v in self.attributes.items())



    
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
    for _ in range(65):
        shape_type = random.randint(1, 4)
        attrs = {
            "Position": (random.randint(0, 500), random.randint(0, 500)),
            "Radius": random.randint(10, 100),
            "Color": (random.randint(0,255), random.randint(0,255), random.randint(0,255)),
            "Shape" : shape_type
        }
        shape = ArtElement(attrs)
        canvas.add_element(shape)
    canvas.render()
    # for __str__ to show
    print(shape)

main()

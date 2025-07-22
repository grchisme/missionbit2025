from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

image = Image.open('conan.jpg')
#image.show()

resized_image = image.resize((100, 100))

rotated_image = image.rotate(90)

grayscale_image = image.convert('L')

blur = image.filter(ImageFilter.BoxBlur(3))
blur.save("blurred_image.jpg")

edge = image.filter(ImageFilter.EDGE_ENHANCE_MORE)

sharpen = image.filter(ImageFilter.SHARPEN)

contrast = ImageEnhance.Contrast(image)
factor = 1.8  # Example: Increase contrast by 50%
contrast_img = contrast.enhance(factor)
contrast_img.save("enhanced_contrast_image.jpg")
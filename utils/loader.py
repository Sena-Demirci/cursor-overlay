from PIL import Image

def load_image(path, size):
    img = Image.open(path).convert("RGBA")
    return img.resize((size, size))
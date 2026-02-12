from PIL import Image, ImageDraw

def create_icon(size, filename):
    img = Image.new('RGBA', (size, size), color=(255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    # Draw a blue circle
    d.ellipse([0, 0, size, size], fill=(52, 152, 219))
    # Draw a white P
    font_size = int(size * 0.6)
    # Since we might not have a font, we'll just draw a smaller white circle for simplicity
    d.ellipse([size*0.25, size*0.25, size*0.75, size*0.75], fill=(255, 255, 255))
    
    img.save(filename)
    print(f"Created {filename}")

if __name__ == "__main__":
    create_icon(16, "icons/icon16.png")
    create_icon(48, "icons/icon48.png")
    create_icon(128, "icons/icon128.png")

from PIL import Image, ImageOps, ImageDraw

class ImageManager:
    
    LIGHT_SEARCH_IMAGE = Image.open('images/light_search_icon.png')
    DARK_SEARCH_IMAGE = Image.open('images/dark_search_icon.png')
    MP3_IMAGE = Image.open('images/mp3_icon.png')
    MP4_IMAGE = Image.open('images/mp4_icon.png')
    
    def circle_mask(img: Image.Image):

        # Open the image from bytes
        width, height = img.size

        # Create a new transparent image of the same size as the original image
        circle_mask = Image.new('RGBA', (width, height), (0, 0, 0, 0))

        # Create a draw object to draw a white circle on the new image
        draw = ImageDraw.Draw(circle_mask)
        draw.ellipse((0, 0, width, height), fill=(255, 255, 255, 255))

        # Crop the original image using the new image as a mask
        output = ImageOps.fit(img, (width, height), centering=(0.5, 0.5))

        # Apply the circular mask to the cropped image
        output.putalpha(circle_mask.getchannel('A'))
                 
        return output
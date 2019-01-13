import pytesseract
from PIL import Image
from PIL import ImageFilter



def process_image(path):
    image = Image.open(path)
#    image.filter(ImageFilter.SHARPEN)

    # Uncomment the line below to provide path to tesseract manually
    # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

    # Define config parameters.
    # '-l eng'  for using the English language
    # '--oem 1' for using LSTM OCR Engine
    config = ('-l eng --oem 1 --psm 3')

    # Read image from disk

    # Run tesseract OCR on image
    text = pytesseract.image_to_string(image, config=config)

    return text
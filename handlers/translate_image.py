# adds image processing capabilities
from PIL import Image

# will convert the image to text string
import pytesseract

# translates into preferred language
from googletrans import Translator



# pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR/tesseract.exe'

def translate_image(lan):
    img = Image.open('/home/ergashfx2/mandatbot/handlers/images/image.png')
    result = pytesseract.image_to_string(img)
    p = Translator()
    k = p.translate(result, dest=lan)
    translated = str(k.text)
    print(translated)
    return translated

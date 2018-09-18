import pyscreenshot as ImageGrab
import PIL
fileName = "resources/ad.png"
im  = ImageGrab.grab( bbox =(15,100,1060,700))
# im.save(fileName)

import pytesseract

text = pytesseract.image_to_string(im)
print(text)
# im.show()
# # PIL.Image.save(im, "~/1.png")

# position of mouse click - (93,707)


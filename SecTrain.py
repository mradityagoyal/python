try:
    import Image
except ImportError:
    from PIL import Image
#
#
# # If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
#
# # Simple image to string
# print(pytesseract.image_to_string(Image.open('test.png')))
import pyscreenshot as ImageGrab

im=ImageGrab.grab(bbox=(10,100,1100,700)) # X1,Y1,X2,Y2
>>> im.show()

import pyautogui
import pyscreenshot
import pytesseract
import os
import pyautogui
import time

NUM_SLIDES = 10
screenshot_bbox = (15,100,1060,700)
COURSE_NAME = 'TEST1_'
#Location where will click for next
CLICK_LOC = (93,707)
#sleep interval
WAIT_TIME = 2
FIRST_SLIDE = 7

img_dir = 'resources/captures'
text_dir = 'resources/text'
for i in range(FIRST_SLIDE,FIRST_SLIDE+NUM_SLIDES):
    #take screenshot and save.
    im  = pyscreenshot.grab(bbox =screenshot_bbox)
    #image captured.. can click ahead.
    pyautogui.click(CLICK_LOC)

    #save capture
    captureFile = "%s/%s%s.png" % (img_dir, COURSE_NAME, i)
    im.save(captureFile)
    print("Screenshot #%s taken and saved at %s" %(i, captureFile))

    #use teserract to extract text.
    text = pytesseract.image_to_string(im)
    #remote blank lines
    text = os.linesep.join([s.tolower() for s in text.splitlines() if s])
    #create file name
    textFile = "%s/%s%s.txt" %(text_dir, COURSE_NAME, i)
    #write to file
    tf = open(textFile, "w")
    tf.write(text)
    tf.close()

    #sleep for some time
    time.sleep(WAIT_TIME)



# im.show()
# # PIL.Image.save(im, "~/1.png")


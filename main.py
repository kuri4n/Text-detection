import cv2
import easyocr
import matplotlib.pyplot as plt
from skimage.color.rgb_colors import green

image_path = 'insert your image location'

img = cv2.imread(image_path)

reader = easyocr.Reader(['en'],gpu=True)

text = result = reader.readtext(img)

for i in text:
    bbox, text,score = i

    if score > 0.5:
        cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 2)
        cv2.putText(img,text, bbox[0],cv2.FONT_HERSHEY_COMPLEX,0.65, (255,0,0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

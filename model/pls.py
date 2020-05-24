import os
import cv2

for file in os.listdir("./data/custom/images/"):
    img = cv2.imread("./data/custom/images/" + file)
    print(img.shape)
    input()

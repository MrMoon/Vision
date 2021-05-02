import cv2
from cv2 import dnn_superres

super_resolution = dnn_superres.DnnSuperResImpl_create()

image = cv2.imread("./input.png")

path = "EDSR_x4.pb"
super_resolution.readModel(path)

super_resolution.setModel("edsr" , 4)

result = super_resolution.upsample(image)

cv2.imwrite("./upscaled.png" , result)


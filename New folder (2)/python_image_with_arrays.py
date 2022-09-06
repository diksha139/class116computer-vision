import numpy as np
import cv2

black = np.zeros([600,600])

# f_row=black[0:1]
# print(f_row)
black[200:400,200:400]= 255

cv2.imshow("black",black)

print(black)

cv2.waitKey(0)

# import bcrypt
# password = "moricyber12345"
# pass_byte = password.encode("utf-8")
# pass_hashed = bcrypt.hashpw(pass_byte , bcrypt.gensalt())
# print(pass_hashed)

# new_pass='omran1234'
# npass_byte = new_pass.encode("utf-8")

# if bcrypt.checkpw(npass_byte, pass_hashed):
#     print('yes')
# else:
#     print('no')
import cv2
from imread_from_url import imread_from_url

from ONNX.yolov8 import YOLOv8

# Initialize yolov8 object detector
model_path = "ONNX/yolov8m.onnx"
yolov8_detector = YOLOv8(model_path, conf_thres=0.2, iou_thres=0.3)

# Read image
img_url = "https://thumbs.dreamstime.com/z/wide-city-street-full-cars-yellow-taxi-car-highway-rush-hour-88000215.jpg?ct=jpeg"
img = imread_from_url(img_url)

# Detect Objects
boxes, scores, class_ids = yolov8_detector(img)

# Draw detections
combined_img = yolov8_detector.draw_detections(img)
cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
cv2.imshow("Detected Objects", combined_img)
cv2.imwrite("doc/img/detected_objects.jpg", combined_img)
cv2.waitKey(0)
